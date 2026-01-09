
import numpy as np
import pandas as pd
from typing import List, Union, Optional, Tuple, Dict
from scipy import stats

def calculate_power_based_n(
    m: int,
    effect_size_f2: float,
    alpha: float = 0.05,
    power: float = 0.80,
    is_partial: bool = False
) -> int:
    """
    Calculates the required sample size for multiple linear regression using the
    standard non-central F-test formula (Cohen, 1988).
    
    Parameters:
    -----------
    m : int
        Number of independent predictors (degrees of freedom for numerator).
        For partial correlation (single coefficient), this is effectively 1,
        but we account for the full model df in the denominator.
    effect_size_f2 : float
        Cohen's f-squared effect size.
    alpha : float, optional
        Significance level (Type I error). Default 0.05.
    power : float, optional
        Statistical power (1 - Type II error). Default 0.80.
    is_partial : bool, optional
        If True, computes power for a single regression coefficient (partial correlation)
        given a model with m total predictors.
        If False, computes power for the overall model R-squared (multiple correlation).
        
    Returns:
    --------
    int
        The calculation-based minimum sample size.
    """
    try:
        # Initial guess for N (must be > m + 1)
        # Low guess might fail, so start reasonable
        low = m + 5
        high = 50000
        
        target_beta = 1.0 - power
        
        # Binary search for minimum N
        # We search for the smallest N such that observed_power >= target_power
        
        # Test Function
        def get_beta(n_val):
            if n_val <= m + 1:
                return 1.0
            
            # Degrees of freedom for F-test
            df_denom = n_val - m - 1
            
            if is_partial:
                # Testing one coefficient (or subset, but usually 1 for "default" partial)
                # Numerator df = 1 (usually) for single coefficient test
                # But Green's "partial" rule usually implies checking individual predictors.
                # Standard t-test for coeff is equivalent to F(1, N-m-1).
                df_num = 1
            else:
                # Testing overall model R^2
                df_num = m
            
            # Non-centrality parameter (lambda)
            # lambda = f^2 * N (traditional for simple F-test approximation) or f^2 * (u + v + 1)?
            # Using Cohen's (1988) definition L = f^2 * v (denominator df) is common for tables,
            # but usually lambda = f^2 * N is used in G*Power for "Linear multiple regression: Fixed model".
            # For "Deviation from zero" (Multiple R^2): lambda = f^2 * N
            # For "Single regression coefficient": lambda = f^2 * N (approx) or adjusted.
            # G*Power uses f^2 * N for both roughly.
            # Let's use f^2 * N which is the standard asymptotic approximation.
            ncp = effect_size_f2 * n_val
            
            # Critical Value F_crit under Null
            f_crit = stats.f.ppf(1 - alpha, df_num, df_denom)
            
            # Power = 1 - CDF_noncentral(f_crit)
            # Beta = CDF_noncentral(f_crit)
            beta_val = stats.ncf.cdf(f_crit, df_num, df_denom, ncp)
            return beta_val

        # Find simple bound first
        best_n = high
        
        # Check high limit first to avoid infinite loop
        if get_beta(high) > target_beta:
             pass # Even 50000 is not enough? Probably tiny effect size.
                  # Just return 50000+ or expand search
        
        while low <= high:
            mid = (low + high) // 2
            current_beta = get_beta(mid)
            
            if current_beta <= target_beta:
                # We have enough power, try smaller N
                best_n = mid
                high = mid - 1
            else:
                # Not enough power, need larger N
                low = mid + 1
                
        return int(best_n)
        
    except Exception:
        # Fallback if calculation fails
        return -1


def calculate_green_rule(
    m: Union[int, List[int]],
    rule_type: str = "partial",
    alpha: float = 0.05,
    power: float = 0.80,
    effect_size: Union[str, float] = "medium",
    sensitivity_mode: bool = False
) -> pd.DataFrame:
    """
    Calculates minimum sample size based on Green's Rule (1991) and optionally performs
    a sensitivity analysis using power-based calculations.

    Parameters:
    -----------
    m : int or List[int]
        Number of predictor variables.
    rule_type : str, optional -- "partial" or "multiple" (default "partial")
        "partial": For testing partial correlations (individual coefficients).
                   Green's Formula: N >= 104 + m
        "multiple": For testing multiple correlation (R^2).
                    Green's Formula: N >= 50 + 8m
    alpha : float, optional
        Significance level. Default 0.05.
    power : float, optional
         Target power. Default 0.80.
    effect_size : str or float, optional
        Effect size (Cohen's f^2).
        Can be "small" (0.02), "medium" (0.15), "large" (0.35), or a specific float value.
    sensitivity_mode : bool, optional
        If True, calculates an 'adjusted_N' using exact power formulas (non-central F-test)
        based on the provided alpha, power, and effect size parameters, to compare against
        the heuristic Green's rule.

    Returns:
    --------
    pd.DataFrame
        Table containing:
        - m: Number of predictors
        - green_rule_N: Result from Green's formula
        - adjusted_N: (Optional) Result from power calculation
        - notes: Description of parameters used
    """
    
    # 1. Normalize Inputs
    if isinstance(m, int):
        m_values = [m]
    else:
        m_values = m
    
    # Validate Inputs
    valid_m = [max(1, int(x)) for x in m_values]
    
    # Resolve Effect Size
    # Cohen's f^2 conventions
    f2_map = {
        "small": 0.02,
        "medium": 0.15,
        "large": 0.35
    }
    
    f2_val = 0.15 # Default
    eff_desc = str(effect_size)
    
    if isinstance(effect_size, str):
        if effect_size.lower() in f2_map:
            f2_val = f2_map[effect_size.lower()]
        else:
            # Try parsing string as float
            try:
                f2_val = float(effect_size)
            except ValueError:
                f2_val = 0.15 # Fallback
    elif isinstance(effect_size, (int, float)):
        f2_val = float(effect_size)
        
    is_partial = (rule_type.lower() == "partial")
    
    # 2. Results Collection
    results = []
    
    for val_m in valid_m:
        # --- A. Green's Rule Calculation ---
        if is_partial:
            # N >= 104 + m
            green_n = 104 + val_m
            rule_desc = "Partial (104 + m)"
        else:
            # N >= 50 + 8m
            green_n = 50 + 8 * val_m
            rule_desc = "Multiple (50 + 8m)"
            
        row = {
            "m": val_m,
            "green_rule_N": green_n,
            "rule_type": rule_type
        }
        
        note_parts = [f"Green: {rule_desc}"]
        
        # --- B. Sensitivity Analysis (Power-based) ---
        if sensitivity_mode:
            adj_n = calculate_power_based_n(
                m=val_m, 
                effect_size_f2=f2_val, 
                alpha=alpha, 
                power=power,
                is_partial=is_partial
            )
            
            row["adjusted_N"] = adj_n
            # row["diff"] = adj_n - green_n
            
            # Descriptive note
            note_parts.append(f"Power-based (f2={f2_val}, a={alpha}, p={power})")
            
            # Check for very different results
            if adj_n > green_n * 1.5:
                 note_parts.append("[WARN: Green's rule may be underpowered]")
            elif green_n > adj_n * 1.5:
                 note_parts.append("[Note: Green's rule is conservative]")

        row["notes"] = "; ".join(note_parts)
        results.append(row)
        
    # 3. Build DataFrame
    df = pd.DataFrame(results)
    
    # Reorder columns for clarity
    cols = ["m", "green_rule_N"]
    if sensitivity_mode:
        cols.append("adjusted_N")
    cols.append("notes")
    
    # Filter only existing columns
    final_cols = [c for c in cols if c in df.columns]
    
    return df[final_cols]


if __name__ == "__main__":
    # --- Demo Routine ---
    print("=== Green's Rule Calculator Demo ===\n")
    
    test_m = [5, 10, 15, 20, 30]
    
    print("1. Standard Green's Rule (Partial Correlation):")
    df_std = calculate_green_rule(m=test_m, rule_type="partial")
    print(df_std.to_string(index=False))
    print("\n" + "-"*50 + "\n")
    
    print("2. Standard Green's Rule (Multiple Correlation):")
    df_mult = calculate_green_rule(m=test_m, rule_type="multiple")
    print(df_mult.to_string(index=False))
    print("\n" + "-"*50 + "\n")
    
    print("3. Sensitivity Analysis (Partial, Power=0.90, Small Effect):")
    # Green's rule assumes medium effect. Small effect requires much larger N.
    # We expect 'adjusted_N' to be much higher than 'green_rule_N'.
    df_sens = calculate_green_rule(
        m=test_m, 
        rule_type="partial", 
        alpha=0.05, 
        power=0.90, 
        effect_size="small", 
        sensitivity_mode=True
    )
    print(df_sens.to_string(index=False))
    print("\nDone.")

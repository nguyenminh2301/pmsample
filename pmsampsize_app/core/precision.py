
import numpy as np
import pandas as pd
from scipy.stats import norm, beta

def calculate_binom_size(p, half_width, confidence=0.95, method="wilson"):
    """
    Calculates sample size for binomial proportion CI width.
    Finds minimal N such that CI half-width <= half_width.
    
    Args:
        p (float): Expected proportion (0 < p < 1)
        half_width (float): Desired margin of error (d)
        confidence (float): Confidence level (e.g. 0.95)
        method (str): 'wald', 'wilson', 'clopper-pearson'
        
    Returns:
        dict: Result for single scenario
    """
    
    alpha = 1 - confidence
    z = norm.ppf(1 - alpha/2)
    
    # Grid search or closed form?
    # Wald is closed form
    if method == "wald":
        # n = z^2 * p(1-p) / d^2
        n_est = np.ceil((z**2 * p * (1-p)) / (half_width**2))
        return {
            "N": int(n_est),
            "Events": int(np.ceil(n_est * p)),
            "Method": "Wald",
            "Actual_Width": 2*half_width # Approximate
        }
        
    # Numerical search for Wilson / CP
    # Monotone search: Start at Wald estimate, check, expand if needed
    start_n = int((z**2 * p * (1-p)) / (half_width**2)) - 10
    if start_n < 5: start_n = 5
    
    # Simple linear scan upwards from guess (efficient enough for N < 100000)
    # Or binary search if needed. Linear is safer for edge cases.
    
    current_n = start_n
    while True:
        # Check conservative coverage
        # Options: x = round(n*p) -> Standard
        # Conservative: check x floor and ceil? 
        # Requirement: "Implement Option 2 (conservative) as default"
        
        x_floor = int(np.floor(current_n * p))
        x_ceil = int(np.ceil(current_n * p))
        
        candidates = sorted(list(set([x_floor, x_ceil])))
        
        max_half_width = 0
        
        for k in candidates:
            if method == "wilson":
                # Wilson score interval width
                # Center = (x + z^2/2) / (n + z^2)
                # HW = z / (n + z^2) * sqrt( x(n-x)/n + z^2/4 )
                
                denom = current_n + z**2
                term1 = (z * np.sqrt( k*(current_n-k)/current_n + z**2/4 )) / denom
                hw = term1
                # (Note: Wilson is often asymmetric, HW is (Upper-Lower)/2 or max(U-p, p-L)? 
                # Prompt says: "Compute half-width = (upper - lower)/2")
                # Wilson Bounds:
                # p_hat = k/n
                # center = (k + z*z/2) / (n + z*z)
                # hw_val = z / (n + z*z) * sqrt( k*(n-k)/n + z*z/4 )
                # Upper = center + hw_val, Lower = center - hw_val
                # So width = 2 * hw_val. Half-width = hw_val.
                pass
                
            elif method == "clopper-pearson":
                # Exact Beta
                # Lower = beta.ppf(alpha/2, k, n-k+1)
                # Upper = beta.ppf(1-alpha/2, k+1, n-k)
                # If k=0, lower=0. If k=n, upper=1.
                if k == 0: lower = 0
                else: lower = beta.ppf(alpha/2, k, current_n - k + 1)
                
                if k == current_n: upper = 1
                else: upper = beta.ppf(1 - alpha/2, k + 1, current_n - k)
                
                hw = (upper - lower) / 2
            
            if hw > max_half_width:
                max_half_width = hw
        
        if max_half_width <= half_width:
            return {
                "N": current_n,
                "Events": int(np.ceil(current_n * p)),
                "Method": method.title().replace("-", " "),
                "Actual_Half_Width": max_half_width
            }
            
        current_n += 1
        if current_n > 1000000: # Safety break
            return {"N": -1, "Error": "Not converged"}

def generate_binom_grid(p_list, width_list, conf_list, method):
    res = []
    for p in p_list:
        for w in width_list:
            for c in conf_list:
                r = calculate_binom_size(p, w, c, method)
                r.update({"P_expected": p, "Target_Half_Width": w, "Confidence": c})
                res.append(r)
    return pd.DataFrame(res)

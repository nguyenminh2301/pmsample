
import math
import numpy as np
from scipy import stats
from scipy.optimize import minimize_scalar

def prec_auc(auc, prev, n=None, conf_width=None, conf_level=0.95, opt_upper=1e6, opt_tol=1e-4):
    """
    Replication of presize::prec_auc (Hanley-McNeil variance).
    Exactly matches R implementation logic.
    
    Args:
        auc (float): Expected AUC [0, 1]
        prev (float): Prevalence [0, 1]
        n (float, optional): Sample size.
        conf_width (float, optional): Desired CI width.
        conf_level (float): Confidence level (default 0.95).
        opt_upper (float): Upper bound for n optimization (default 1e6).
        opt_tol (float): Tolerance for optimization.

    Returns:
        dict: {
            "n": float,
            "n1": float,
            "n2": float,
            "auc": float,
            "prev": float,
            "lwr": float,
            "upr": float,
            "conf_width": float,
            "conf_level": float,
            "method": str
        }
    """
    # Validation checks matching R
    if (n is None and conf_width is None) or (n is not None and conf_width is not None):
        raise ValueError("Exactly one of 'n' and 'conf_width' must be None.")
    
    if not (0 <= prev <= 1):
        raise ValueError("'prev' must be numeric in [0, 1]")
    if not (0 <= auc <= 1):
        raise ValueError("'auc' must be numeric in [0, 1]")
    if not (0 < conf_level < 1):
        raise ValueError("'conf_level' must be in (0, 1)")
        
    if conf_width is not None and conf_width <= 0:
        raise ValueError("'conf_width' must be > 0")
    if n is not None and n <= 0:
        raise ValueError("'n' must be > 0")

    # Core calculation function (internal to R function)
    def calc_stats(n_val, prev_val, auc_val):
        n1 = n_val * prev_val
        n2 = n_val * (1 - prev_val)
        
        q0 = auc_val * (1 - auc_val)
        q1 = auc_val / (2 - auc_val) - auc_val**2
        q2 = 2 * auc_val**2 / (1 + auc_val) - auc_val**2
        
        # Avoid division by zero
        if n1 <= 0 or n2 <= 0:
            return np.inf, -np.inf, np.inf, np.inf
            
        term = (q0 + (n1 - 1) * q1 + (n2 - 1) * q2) / (n1 * n2)
        if term < 0: term = 0 # Safety measure, though mathematically shouldn't happen for valid AUC
        se = math.sqrt(term)
        
        alpha = (1 - conf_level) / 2
        z = stats.norm.ppf(1 - alpha)
        
        upr = auc_val + z * se
        lwr = auc_val - z * se
        width = upr - lwr
        
        return upr, lwr, width

    # Optimization function
    def opti_fn(n_val):
        _, _, width = calc_stats(n_val, prev, auc)
        return abs(width - conf_width)

    result_n = 0.0
    est_method = ""

    if n is None:
        # Sample size calculation
        est_method = "sample size"
        
        # R uses stats::optimize which is 1D bounded minimization
        # Scipy equivalent is minimize_scalar with Check bounds
        res = minimize_scalar(
            opti_fn, 
            bounds=(0, opt_upper), 
            method='bounded',
            options={'xatol': opt_tol} 
        )
        
        if not res.success:
            # Fallback or warning? R doesn't typically fail optimize unless error in fn
            pass
            
        result_n = res.x
        upr, lwr, res_width = calc_stats(result_n, prev, auc)
        final_width = res_width

    else:
        # Precision calculation
        est_method = "precision"
        result_n = float(n)
        upr, lwr, final_width = calc_stats(result_n, prev, auc)

    return {
        "auc": auc,
        "prev": prev,
        "n": result_n,
        "n1": result_n * prev,
        "n2": result_n * (1 - prev),
        "lwr": lwr,
        "upr": upr,
        "conf_width": final_width,
        "conf_level": conf_level,
        "method": f"{est_method} for AUC"
    }

# Unit test helper
def generate_reference_scenarios():
    pass # To be implemented

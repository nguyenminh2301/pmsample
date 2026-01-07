
import numpy as np
import pandas as pd
import scipy.stats
from scipy.optimize import minimize_scalar, brentq

# -----------------------------------------------------------------------------
# 1. HELPERS: LP Generation & Miscalibration
# -----------------------------------------------------------------------------

def inverse_logit(x):
    return 1 / (1 + np.exp(-x))

def sim_lp_distribution(n, dist_type="normal", params=None, seed=None):
    """
    Generate LP vector of size n.
    params: dict with keys (mu, sd) for normal, (alpha, beta) for beta.
    """
    if seed is not None:
        np.random.seed(seed)
        
    if dist_type == "normal":
        mu = params.get("mu", 0)
        sd = params.get("sd", 1)
        return np.random.normal(mu, sd, n)
    elif dist_type == "beta":
        # Beta on PROBABILITY scale -> logit to LP
        a = params.get("alpha", 2)
        b = params.get("beta", 2)
        probs = np.random.beta(a, b, n)
        epsilon = 1e-9
        probs = np.clip(probs, epsilon, 1 - epsilon)
        return np.log(probs / (1 - probs))
    elif dist_type == "empirical":
        values = params.get("values", [])
        if len(values) == 0:
            raise ValueError("Empirical distribution requires 'values'")
        return np.random.choice(values, size=n, replace=True)
    else:
        raise ValueError(f"Unknown dist_type: {dist_type}")

def solve_gamma_for_target_p(target_p, slope, lp_dist_fn, n_integration=10000):
    """
    Find gamma such that mean(inverse_logit(gamma + slope * LP)) = target_p.
    Uses MC integration.
    """
    # Generate a large sample of LP
    lp_sample = lp_dist_fn(n_integration)
    
    def objective(g):
        p_vals = inverse_logit(g + slope * lp_sample)
        return np.mean(p_vals) - target_p
        
    # Root finding
    try:
        gamma_sol = brentq(objective, -10, 10)
    except ValueError:
        # Fallback if boundaries are not bracketing (rare for reasonable target_p)
        gamma_sol = 0
        
    return gamma_sol

# -----------------------------------------------------------------------------
# 2. METRICS HELPERS
# -----------------------------------------------------------------------------

def hanley_se_auc(auc, n1, n0):
    """
    Matches R function `hanley_se_auc` exactly.
    n1: events, n0: non-events
    """
    if n1 <= 1 or n0 <= 1: return np.inf
    
    q0 = auc * (1 - auc)
    q1 = auc / (2 - auc)
    q2 = 2 * auc**2 / (1 + auc)
    
    var = (q0 + (n1 - 1) * (q1 - auc**2) + (n0 - 1) * (q2 - auc**2)) / (n1 * n0)
    if var < 0: return 0
    return np.sqrt(var)

def fast_auc(y_true, y_score):
    """
    Compute AUC using Mann-Whitney U / Trapezoidal. 
    Using scipy rankdata or simple sort. 
    Use numpy for speed.
    """
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    
    n1 = np.sum(y_true)
    n0 = len(y_true) - n1
    if n1 == 0 or n0 == 0: return 0.5 # Undefined
    
    # Global rank
    order = np.argsort(y_score)
    rank = np.argsort(order) + 1 # 1-based rank
    
    # AUC = (Sum(Rank_cases) - n1(n1+1)/2) / (n1*n0)
    rank_sum_cases = np.sum(rank[y_true == 1])
    auc = (rank_sum_cases - n1 * (n1 + 1) / 2) / (n1 * n0)
    return auc

def fast_logistic_slope_se(y, lp):
    """
    Fit logistic regression y ~ a + b * LP.
    Return SE(b).
    Uses Newton-Raphson (IRLS) 1-step or few steps.
    Since we know beta ~ 1 (if calibrated), we can start close.
    """
    # Design matrix X: [1, LP]
    n = len(y)
    X = np.column_stack((np.ones(n), lp))
    
    # Init betas (0, 1) usually good if calibrated
    beta = np.zeros(2)
    
    # Newton-Raphson loop (usually converges in 4-5 steps)
    for _ in range(5):
        eta = np.dot(X, beta)
        mu = 1 / (1 + np.exp(-eta))
        w = mu * (1 - mu)
        
        # Gradient: X.T * (y - mu)
        grad = np.dot(X.T, (y - mu))
        
        # Hessian: X.T * W * X
        # W is diagonal, so X.T * (w[:, None] * X)
        H = np.dot(X.T, w[:, None] * X)
        
        # Invert Hessian
        try:
            H_inv = np.linalg.inv(H)
        except np.linalg.LinAlgError:
            return np.inf
            
        # Update
        delta = np.dot(H_inv, grad)
        beta += delta
        
        if np.max(np.abs(delta)) < 1e-5:
            break
            
    # SE of slope (beta[1]) is sqrt(H_inv[1, 1])
    se_slope = np.sqrt(H_inv[1, 1])
    slope = beta[1]
    return slope, se_slope

def calc_ln_oe_stats(y, probs):
    O = np.sum(y)
    E = np.sum(probs)
    if O == 0 or E == 0: return np.nan, np.inf
    
    ln_oe = np.log(O / E)
    # SE(ln(O/E)) approx sqrt( (1-p_bar)/E_events ) ?
    # Standard: sqrt(1/O) if O is Poisson count approx
    # Or Delta method: SE = sqrt( Var(O)/O^2 ) ~ sqrt(O/O^2) = sqrt(1/O)
    se_ln_oe = np.sqrt(1 / O)
    return ln_oe, se_ln_oe

# -----------------------------------------------------------------------------
# 3. MAIN SIMULATION ENGINE
# -----------------------------------------------------------------------------

def run_d10_simulation(
    n_list,
    dist_type="normal", dist_params=None,
    gamma=0, slope_true=1,
    n_sims=500,
    seed_start=12345,
    metrics=["c_stat", "slope", "ln_oe"],
    conf_level=0.95
):
    """
    Runs simulation for each N in n_list.
    Returns DataFrame with mean width and pass/fail status.
    """
    results_per_n = []
    
    # Pre-generate randomness if possible or just use independent seeds per N
    # For independent replicability per N, structure SEEDS
    
    rng_audit = {"seed_start": seed_start, "n_list": n_list}
    
    for n in n_list:
        # Use a distinct seed for each N block to ensure modifying N list doesn't change prior results
        # seed_n = seed_start + n logic (simple) or SeedSequence
        seed_n_seq = np.random.SeedSequence(seed_start)
        # Spawn off a child for this N
        # Ideally we want the seed to depend on N value to be robust?
        # Or just deterministic sequence?
        # Let's use seed_start + n_index * n_sims (classic approach)
        
        sim_metrics = {"c_width": [], "slope_width": [], "ln_oe_width": []}
        
        # Run Sims
        for i in range(n_sims):
            iter_seed = seed_start + n*10000 + i # Unique deterministic seed
            np.random.seed(iter_seed)
            
            # 1. Gen LP
            lp = sim_lp_distribution(n, dist_type, dist_params)
            
            # 2. Gen Outcome
            logit_p = gamma + slope_true * lp
            prob_true = inverse_logit(logit_p)
            y = np.random.binomial(1, prob_true)
            
            n1 = np.sum(y)
            n0 = n - n1
            
            z = scipy.stats.norm.ppf(1 - (1 - conf_level)/2)
            
            # 3. Metrics
            # C-Statistic
            if "c_stat" in metrics:
                if n1 > 0 and n0 > 0:
                    auc = fast_auc(y, prob_true) # Or use LP? Theoretically rank(LP) == rank(prob_true)
                    se_auc = hanley_se_auc(auc, n1, n0)
                    sim_metrics["c_width"].append(2 * z * se_auc)
                else:
                    sim_metrics["c_width"].append(np.nan)
                    
            # Slope
            if "slope" in metrics:
                 # Be careful: Fit y ~ LP. 
                 # If perfect separation, slope explodes.
                 if n1 > 5 and n0 > 5: # Limit stability
                     try:
                        s_val, se_s = fast_logistic_slope_se(y, lp)
                        width_s = 2 * z * se_s
                        # Filter crazy widths
                        if width_s < 20: 
                            sim_metrics["slope_width"].append(width_s)
                        else:
                            sim_metrics["slope_width"].append(np.nan) # Treat divergent as missing or large?
                     except:
                        sim_metrics["slope_width"].append(np.nan)
                 else:
                     sim_metrics["slope_width"].append(np.nan)

            # Ln(O/E)
            if "ln_oe" in metrics:
                # E = sum(prob_true)? No, in validation we calculate E based on the *model's* predictions.
                # Here we assume the "LP" comes from the model being validated.
                # So P_hat = inverse_logit(LP).
                # Wait. In generation: logit(p_true) = gamma + S * LP.
                # The model PREDICTION is P_hat = inverse_logit(LP) (i.e. assuming gamma=0, S=1).
                # So E = sum(inverse_logit(LP)).
                
                p_hat = inverse_logit(lp)
                _, se_oe = calc_ln_oe_stats(y, p_hat)
                sim_metrics["ln_oe_width"].append(2 * z * se_oe)

        # Aggregate
        # Snell usage: "Mean width"
        row = {"N": n}
        if "c_stat" in metrics:
            row["Mean_C_Width"] = np.nanmean(sim_metrics["c_width"])
        if "slope" in metrics:
            row["Mean_Slope_Width"] = np.nanmean(sim_metrics["slope_width"])
        if "ln_oe" in metrics:
            row["Mean_OE_Width"] = np.nanmean(sim_metrics["ln_oe_width"])
            
        results_per_n.append(row)
        
    return pd.DataFrame(results_per_n), rng_audit

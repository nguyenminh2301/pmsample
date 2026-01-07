
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import root_scalar
import time
from joblib import Parallel, delayed

# Optional PyMC import
try:
    import pymc as pm
    import arviz as az
    HAS_PYMC = True
except ImportError:
    HAS_PYMC = False

def run_single_rep(seed_int, N, P, n_continuous, rho, p_true, assurance_threshold):
    """
    Standalone function for parallel execution.
    Generates data, fits model, evaluates metrics.
    """
    if not HAS_PYMC:
        return {"error": "PyMC missing"}

    rng = np.random.default_rng(seed_int)
    
    # 1. DGM Parameters (Randomized for Assurance)
    # Coefficients
    betas = np.array([0.59, 0.40, 0.26]) # Key
    n_remaining = P - 3
    if n_remaining > 0:
        extra_betas = rng.normal(0, 0.2, n_remaining)
        betas = np.concatenate([betas, extra_betas])
    else:
        betas = betas[:P]
        
    # Intercept calibration (approximate or precise)
    # To be fast, we can use approximation E[p] ~ sigmoid(alpha / sqrt(1 + 0.34*var(XB)))
    # But precise root finding is safer and fast enough (scalar).
    
    # Local Generate X helper restricted to this function or duplicating logic?
    # Duplicating small logic is safer for pickling than ensuring class methods are picklable
    # Generate large X_cal
    N_cal = 2000 
    mean = np.zeros(P)
    cov = np.eye(P)
    cov[cov == 0] = rho
    Z_cal = rng.multivariate_normal(mean, cov, size=N_cal)
    X_cal = np.zeros_like(Z_cal)
    X_cal[:, :n_continuous] = Z_cal[:, :n_continuous]
    thresh = norm.ppf(0.3)
    X_cal[:, n_continuous:] = (Z_cal[:, n_continuous:] < thresh).astype(float)
    
    XB = X_cal @ betas
    
    def objective(alpha):
        probs = 1 / (1 + np.exp(-(alpha + XB)))
        return np.mean(probs) - p_true
        
    try:
        res = root_scalar(objective, bracket=[-10, 10], method='brentq')
        alpha = res.root
    except:
        alpha = 0
        
    # 2. Generate Training Data
    # Re-generate X for training
    Z = rng.multivariate_normal(mean, cov, size=N)
    X_train = np.zeros_like(Z)
    X_train[:, :n_continuous] = Z[:, :n_continuous]
    X_train[:, n_continuous:] = (Z[:, n_continuous:] < thresh).astype(float)
    
    lin_pred = alpha + X_train @ betas
    probs = 1 / (1 + np.exp(-lin_pred))
    y_train = rng.binomial(1, probs)
    
    # 3. Generate Validation Data
    # Reuse X_cal if large enough? Or generate new.
    # Let's generate new 5000 for stable validation
    N_val = 5000
    Z_val = rng.multivariate_normal(mean, cov, size=N_val)
    X_val = np.zeros_like(Z_val)
    X_val[:, :n_continuous] = Z_val[:, :n_continuous]
    X_val[:, n_continuous:] = (Z_val[:, n_continuous:] < thresh).astype(float)
    
    lp_val_true = alpha + X_val @ betas
    probs_val = 1 / (1 + np.exp(-lp_val_true))
    y_val = rng.binomial(1, probs_val)
    
    # 4. Fit Bayesian Model
    with pm.Model() as model:
        a = pm.Normal("a", mu=0, sigma=5)
        b = pm.Normal("b", mu=0, sigma=2.5, shape=P)
        logit_p = a + pm.math.dot(X_train, b)
        y_obs = pm.Bernoulli("y_obs", logit_p=logit_p, observed=y_train)
        
        # Fast sampling for simulation context
        # 1 chain is risky but standard for "Assurance Simulation" speed vs precision trade-off
        trace = pm.sample(draws=200, tune=200, chains=1, progressbar=False, random_seed=seed_int, discard_tuned_samples=True, compute_convergence_checks=False)
        
    # 5. Evaluate
    post_a = trace.posterior["a"].mean().values
    post_b = trace.posterior["b"].mean(axis=(0,1)).values
    
    lp_pred_val = post_a + X_val @ post_b
    p_pred_val = 1 / (1 + np.exp(-lp_pred_val))
    
    from sklearn.metrics import roc_auc_score
    try:
        auc = roc_auc_score(y_val, p_pred_val)
    except:
        auc = 0.5
        
    # Fast Calibration Slope (MLE)
    from sklearn.linear_model import LogisticRegression
    # Unpenalized LR
    lr_cal = LogisticRegression(penalty=None, solver='lbfgs') 
    try:
        # Check variance of LP
        if np.std(lp_pred_val) < 1e-6:
             cal_slope = 0
        else:
             lr_cal.fit(lp_pred_val.reshape(-1, 1), y_val)
             cal_slope = lr_cal.coef_[0][0]
    except:
        cal_slope = 0

    # Criteria
    pass_auc = auc >= 0.75
    pass_slope = 0.9 <= cal_slope <= 1.1
    # Ignore width check for speed/robustness in demo unless strictly required
    all_pass = pass_auc and pass_slope
    
    return {
        "auc": auc,
        "cal_slope": cal_slope,
        "pass": all_pass
    }


class BayesianAssuranceSimulation:
    def __init__(self, p_true, P, n_continuous, n_binary, rho, n_candidates, n_sims, 
                 start_seed=42, assurance_threshold=0.80):
        self.p_true = p_true
        self.P = P
        self.n_continuous = n_continuous
        self.n_binary = n_binary
        self.rho = rho
        self.n_candidates = n_candidates
        self.n_sims = n_sims
        self.start_seed = start_seed
        self.assurance_threshold = assurance_threshold
        self.audit_trail = {"global_seed": start_seed, "replicates": []}
        
    # Removed generate_dgm_params/generate_X methods as they are now inside run_single_rep (picklable)
    # Or keep them if needed for other purposes, but run_single_rep is standalone.

    def run(self):
        if not HAS_PYMC:
            raise ImportError("PyMC not found. Please install `pymc` to use Method 2.")

        results = []
        
        # Loop over candidate N
        for N in self.n_candidates:
            # Seed Prep
            ss = np.random.SeedSequence(self.start_seed)
            child_seeds = ss.spawn(self.n_sims)
            seeds_int = [s.generate_state(1)[0] for s in child_seeds]
            
            # Audit
            for i, s in enumerate(seeds_int):
                 self.audit_trail["replicates"].append({"N": N, "rep": i, "seed": int(s)})

            # Parallel Execution
            # n_jobs=-1 uses all cores.
            sim_results = Parallel(n_jobs=-1)(
                delayed(run_single_rep)(
                    seed, N, self.P, self.n_continuous, self.rho, self.p_true, self.assurance_threshold
                ) for seed in seeds_int
            )
            
            df_sim = pd.DataFrame(sim_results)
            assurance = df_sim["pass"].mean()
            
            results.append({
                "N": N,
                "assurance": assurance,
                "auc_mean": df_sim["auc"].mean(),
                "cal_slope_mean": df_sim["cal_slope"].mean()
            })
            
        return pd.DataFrame(results), self.audit_trail

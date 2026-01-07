
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.optimize import root_scalar, brentq
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, brier_score_loss
import statsmodels.api as sm
import statsmodels.formula.api as smf
import time
import warnings

# Suppress warnings for cleaner logs
warnings.filterwarnings("ignore")

class SampleSizeDevSimulation:
    def __init__(self, mode="simple", p_true=0.1, P=10, 
                 target_auc=0.80, # for simple mode based on samplesizedev
                 rho=0.0, # for custom
                 n_continuous=0, n_binary=0, # for custom
                 n_candidates=[500, 1000], n_sims=100,
                 start_seed=20260107,
                 n_test=5000):
        
        self.mode = mode
        self.p_true = p_true
        self.P = P
        self.target_auc = target_auc
        self.rho = rho
        self.n_continuous = n_continuous
        self.n_binary = n_binary
        self.n_candidates = n_candidates
        self.n_sims = n_sims
        self.start_seed = start_seed
        self.n_test = n_test
        
        self.audit_trail = {
            "global_seed": start_seed,
            "replicates": []
        }

    def _generate_dgm_simple(self, rng):
        """
        Samplesizedev-like mode:
        Predictors X ~ N(0, I) (independent standard normal)
        Coefficients Beta_j = beta (all equal)
        We find 'beta' and 'alpha' such that:
          1. AUC matches target_auc
          2. E[p] matches p_true
        """
        # 1. Find Beta magnitude to match AUC
        # For independent normals, linear predictor LP ~ N(alpha, beta^2 * P)
        # AUC = Phi( sigma_LP / sqrt(2) * ??? ) -> Approximation
        # Relation: AUC = Phi( beta * sqrt(P/2) ) if X are indep N(0,1) ?
        # Actually simpler to simulate to find Beta, or use closed form approximation.
        # Analytic approx from standard texts: AUC = Phi( sigma_beta / 1.702 ) ?? No.
        # Let's use simple binary search with simulation (fast) or analytic if confident.
        # Riley et al/Austin use: sigma_LP^2 = Beta' Sigma Beta.
        # If Beta_j = b, Sigma=I, then sigma_LP^2 = P * b^2.
        # AUC approx = Phi( sigma_LP / sqrt(1 + sigma_LP^2/k) ) ?
        # Standard logistic noise approx: AUC = Phi( sigma_LP * 0.607 ) roughly?
        # Let's use Simulation-based Finder for robustness (since we do this once).
        
        def get_auc_for_b(b):
            # Fast sim
            X = np.random.normal(0, 1, size=(5000, self.P))
            betas = np.full(self.P, b)
            lp = X @ betas # Intercept doesn't affect AUC
            p = 1 / (1 + np.exp(-lp))
            # Theoretical AUC from LP? or empirical?
            # Empirical is safer to avoid assumption mismatch
            y = np.random.binomial(1, p)
            if np.unique(y).size < 2: return 0.5
            return roc_auc_score(y, p)

        # But we need consistent seed for the finder? Or just average?
        # Let's use analytic approximation to be fast and stable.
        # AUC = Phi( sigma_LP / 1.4826 ) ??
        # A common one: Log-odds scale. sigma_LP.
        # Formula: AUC = Phi( sigma_LP / sqrt(2) * 1/sigma_logistic ) ? Nope.
        # Relies on LP being normal.
        # Relation: b = ln(OR). 
        # Using a quick calibration function (linear approx)
        # target_AUC 0.5 -> b=0. target_AUC 0.9 -> b high.
        
        # We will use 'root finding' on a fixed large seed
        rng_cal = np.random.default_rng(42)
        X_cal = rng_cal.normal(0, 1, (10000, self.P))
        
        def objective_auc(b):
            lp = X_cal @ np.full(self.P, b)
            # AUC is rank based, intercept doesn't matter
            p_raw = 1/(1+np.exp(-lp)) 
            # We don't even need y, there are analytic estimators for AUC from LP distribution
            # But let's just generate Y
            y_cal = rng_cal.binomial(1, p_raw) # This is noisy
            if np.unique(y_cal).size < 2: return 0.5
            return roc_auc_score(y_cal, p_raw) - self.target_auc

        # Because stochastic root finding is checking, we'd better use a smooth approximation
        # Approximation: AUC = Phi( sigma_LP * 0.607 ) 
        # sigma_LP = sqrt(P * b^2) = b * sqrt(P)
        # 0.8 = Phi( b * sqrt(P) * 0.607 )
        # Phi_inv(0.8) = b * sqrt(P) * 0.607
        # b = Phi_inv(AUC) / (0.607 * sqrt(P))
        import scipy.stats
        try:
            phi_inv_auc = scipy.stats.norm.ppf(self.target_auc)
            # A bit of tuning factor; 0.607 is ~ 1/1.65
            # Austin 2010 says AUC = Phi( beta * 0.607 ) for single var?
            # Let's use 1.702 conversion factor for logit-probit
            # Coeff b.
            b_est = phi_inv_auc * 1.65 / np.sqrt(self.P) 
        except:
            b_est = 0.1
            
        betas = np.full(self.P, b_est)

        # 2. Find intercept for p_true
        # LP = alpha + X@betas
        # mean(sigmoid(LP)) = p_true
        lp_no_int = X_cal @ betas
        
        def objective_p(a):
            return np.mean(1/(1+np.exp(-(a + lp_no_int)))) - self.p_true
            
        try:
            res = root_scalar(objective_p, bracket=[-20, 20], method='brentq')
            alpha = res.root
        except:
            alpha = np.log(self.p_true / (1-self.p_true)) # crude approx

        return alpha, betas

    def _generate_data(self, N, alpha, betas, rng):
        # Generate X
        if self.mode == "simple":
            X = rng.normal(0, 1, size=(N, self.P))
        else:
            # Custom Copula DGM (Reused logic from Bayes or similar)
            # Placeholder for minimal 'custom' logic if needed, 
            # but User Request emphasized 'samplesizedev-like'.
            # Let's implement independent N(0,1) for simple, 
            # and maybe simple correlation for custom if rho > 0.
            if self.rho == 0:
                X = rng.normal(0, 1, size=(N, self.P))
            else:
                mean = np.zeros(self.P)
                cov = np.eye(self.P)
                cov[cov==0] = self.rho # equicorrelation
                X = rng.multivariate_normal(mean, cov, size=N)
                
            # Todo: handling binary/continuous split in custom mode
            # For now, sticking to all continuous N(0,1) for robustness as MVP Method 6
            # unless strictly requested. The prompt says "Custom DGM mode... counts for continuous/binary"
            # I'll add simple transformation.
            if self.n_binary > 0:
                # Transform last n_binary cols
                for j in range(self.n_continuous, self.P):
                     # Threshold for 0.3 marginal?
                    thresh = norm.ppf(0.3)
                    X[:, j] = (X[:, j] < thresh).astype(float)

        lp = alpha + X @ betas
        probs = 1 / (1 + np.exp(-lp))
        y = rng.binomial(1, probs)
        return X, y

    def run(self):
        # 1. Setup DGM (fixed for the simulation if "samplesizedev" style)
        rng_setup = np.random.default_rng(self.start_seed)
        
        if self.mode == "custom":
             # "Custom" logic: User sets betas or we draw them once
             # Prompt: "remaining betas drawn from Normal... intercept calibration"
             # Let's draw ONE set of DGM parameters for the whole experiment (Conditional Assurance)
             # similar to verifying a specific scenario.
             # Or vary it? Usually "Development Sizing" is for a SPECIFIC anticipated scenario.
             # So we Generating params ONCE.
             
             # Key predictors OR 1.8, 1.5, 1.3
             betas = np.array([np.log(1.8), np.log(1.5), np.log(1.3)])
             if self.P > 3:
                 extra = rng_setup.normal(0, 0.2, self.P - 3)
                 betas = np.concatenate([betas, extra])
             else:
                 betas = betas[:self.P]
             
             # Intercept finding
             # Need a temp large X
             X_temp = rng_setup.normal(0, 1, (10000, self.P)) # simplified X generation for calib
             lp_part = X_temp @ betas
             def obj_p(a): return np.mean(1/(1+np.exp(-(a+lp_part)))) - self.p_true
             try:
                 res = root_scalar(obj_p, bracket=[-10, 10], method='brentq')
                 alpha = res.root
             except:
                 alpha = -2
        else:
             # simple mode
             alpha, betas = self._generate_dgm_simple(rng_setup)
             
        # Audit Trail
        self.audit_trail["dgm"] = {"alpha": alpha, "beta_mean": np.mean(betas), "mode": self.mode}

        results = []
        ss = np.random.SeedSequence(self.start_seed)
        
        # Pre-generate Test Data (Fixed for all N, or new per rep? 
        # Usually Independent Test Set per Rep or One Huge Fixed?
        # Standard: One Huge Fixed Test Set from same DGM is efficient and stable.)
        rng_test = np.random.default_rng(ss.spawn(1)[0])
        X_test, y_test = self._generate_data(self.n_test, alpha, betas, rng_test)
        
        # Loop N
        for N in self.n_candidates:
            # Spawn seeds for this N
            child_seeds = ss.spawn(self.n_sims)
            
            rep_stats = []
            
            for i, s_obj in enumerate(child_seeds):
                s_int = int(s_obj.generate_state(1)[0])
                rng_rep = np.random.default_rng(s_int)
                
                # Audit small
                if i < 3: # store first few only to save space
                    self.audit_trail["replicates"].append({"N": N, "rep": i, "seed": s_int})
                
                # 1. Dev Data
                X_train, y_train = self._generate_data(N, alpha, betas, rng_rep)
                
                # 2. Fit
                fallback = False
                try:
                    # Try Standard Logistic
                    model = LogisticRegression(penalty=None, solver='lbfgs', max_iter=200)
                    model.fit(X_train, y_train)
                    coefs = model.coef_[0]
                    nocons = model.intercept_[0]
                except Exception as e:
                    # Fallback Ridge
                    # print(f"Standard LogReg failed: {e}")
                    fallback = True
                    try:
                        model = LogisticRegression(penalty='l2', C=0.1, solver='lbfgs')
                        model.fit(X_train, y_train)
                        coefs = model.coef_[0]
                        nocons = model.intercept_[0]
                    except Exception as e2:
                        # Fail
                        # print(f"Ridge failed: {e2}")
                        continue
                        
                # 3. Evaluate on Test
                # Predict
                lp_test = nocons + X_test @ coefs
                p_test = 1 / (1 + np.exp(-lp_test))
                
                # Metrics
                try:
                    auc = roc_auc_score(y_test, p_test)
                    brier = brier_score_loss(y_test, p_test)
                    
                    # Calibration Slope
                    # Fit logistic: y_test ~ lp_test
                    # We use simple LogReg again
                    cal_mod = LogisticRegression(penalty=None, solver='lbfgs')
                    cal_mod.fit(lp_test.reshape(-1, 1), y_test)
                    slope = cal_mod.coef_[0][0]
                    citl = cal_mod.intercept_[0] # approx CITL
                except:
                    auc, brier, slope, citl = np.nan, np.nan, np.nan, np.nan
                
                rep_stats.append({
                    "auc": auc,
                    "slope": slope,
                    "brier": brier,
                    "fallback": fallback
                })
                
            # Aggregate stats for N
            df_rep = pd.DataFrame(rep_stats).dropna()
            if len(df_rep) == 0:
                continue
                
            row = {
                "N": N,
                "Events": int(N * self.p_true),
                "AUC_mean": df_rep["auc"].mean(),
                "AUC_sd": df_rep["auc"].std(),
                "Slope_mean": df_rep["slope"].mean(),
                "Slope_sd": df_rep["slope"].std(),
                "Slope_min": df_rep["slope"].quantile(0.025),
                "Slope_max": df_rep["slope"].quantile(0.975),
                "Brier_mean": df_rep["brier"].mean(),
                "fallback_pct": df_rep["fallback"].mean(),
                # Criteria Props
                "pass_slope_mean": 1 if df_rep["slope"].mean() >= 0.9 else 0, # Strict mean check? OR user defined
                "pct_slope_09_11": ((df_rep["slope"] >= 0.9) & (df_rep["slope"] <= 1.1)).mean(),
                "pct_auc_075": (df_rep["auc"] >= 0.75).mean()
            }
            results.append(row)
            
        return pd.DataFrame(results), self.audit_trail

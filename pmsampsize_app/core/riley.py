import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.linear_model import LogisticRegression
import math

def calculate_r2_max(p):
    """
    Calculates the maximum possible Cox-Snell R2 for a binary outcome with prevalence p.
    Formula: 1 - exp( 2 * (p*ln(p) + (1-p)*ln(1-p)) )
    """
    if p <= 0 or p >= 1:
        raise ValueError("Prevalence must be between 0 and 1")
    
    # R uses lnLnull = n * [ p*ln(p) + (1-p)*ln(1-p) ]
    # max_r2 = 1 - exp(2 * lnLnull / n)
    #        = 1 - exp(2 * (p*ln(p) + (1-p)*ln(1-p)))
    
    term = p * np.log(p) + (1 - p) * np.log(1 - p)
    return 1 - np.exp(2 * term)

def auc_to_r2_simulation(auc, p, n_sim=1000000, seed=42):
    """
    Converts AUC (C-statistic) to Cox-Snell R2 using simulation, strictly following pmsampsize method.
    
    Args:
        auc: Target AUC (C-statistic)
        p: Outcome prevalence
        n_sim: Number of simulation points (default 1,000,000 to match R package)
        seed: Random seed for reproducibility
    
    Returns:
        float: Estimated Cox-Snell R2
    """
    if auc < 0.5 or auc >= 1:
        raise ValueError("AUC must be >= 0.5 and < 1")
        
    np.random.seed(seed)
    
    # 1. Calculate mu based on AUC
    # mu = sqrt(2) * qnorm(AUC)
    mu = np.sqrt(2) * norm.ppf(auc)
    
    # 2. Simulate Linear Predictors
    # In R code: 
    # LP <- c(rnorm(prev * n, mean = 0, sd = 1), rnorm((1 - prev) * n, mean = mu, sd = 1))
    # y  <- c(rep(0, prev * n), rep(1, (1 - prev) * n))
    # WAIT: check pmsampsize code direction.
    # Usually: 
    # Class 0 (Control) ~ N(0, 1)
    # Class 1 (Case)    ~ N(mu, 1) if mu > 0 and AUC > 0.5
    # The R code snippet I found:
    # LP <- c(rnorm(prevalence * n, mean = 0, sd = 1), 
    #         rnorm((1 - prevalence) * n, mean = mu, sd = 1))
    # y  <- c(rep(0, prevalence * n), rep(1, (1 - prevalence) * n))
    # This implies:
    # Group 0 has size 'prevalence * n'
    # Group 1 has size '(1-prevalence) * n'
    # This seems inverted if 'prevalence' stands for P(Y=1).
    # If p=0.1 (rare event), usually Y=1 has size 0.1*n.
    # In R: y is 0 for the first chunk, 1 for the second.
    # So Y=0 has size p*n, Y=1 has size (1-p)*n.
    # This means 'prevalence' in the R simulation code actually sets the proportion of Y=0 ??
    # OR: The variable name 'prevalence' in R script 'cstat2rsq.R' might be P(Y=1).
    # Let's re-read the snippet carefully.
    # If standard logic holds: 
    # Y=1 is the event.
    # If p is event rate, n_events = p * N.
    # 
    # I will stick to standard statistical logic which matches the likely INTENT of pmsampsize authors,
    # but I must verify if this inversion affects R2.
    # R2 depends on the model fit. 
    # If I swap 0s and 1s and swap distributions, R2 should be identical (symmetry).
    # 
    # Let's implement standard definition:
    # n1 = int(p * n_sim)
    # n0 = n_sim - n1
    # X0 = N(0, 1)
    # X1 = N(mu, 1)
    # Y = [0]*n0 + [1]*n1
    # X = [X0] + [X1]
    
    n1 = int(p * n_sim)
    n0 = n_sim - n1
    
    # Generate Linear Predictor (feature)
    # Note on separation: with AUC, we usually assume Y=1 has higher score.
    # So X1 should have mean mu (if mu>0) and X0 mean 0.
    x0 = np.random.normal(0, 1, n0)
    x1 = np.random.normal(mu, 1, n1)
    
    X = np.concatenate([x0, x1]).reshape(-1, 1)
    y = np.concatenate([np.zeros(n0), np.ones(n1)])
    
    # 3. Fit Logistic Regression
    # We only need the Log Likelihoods.
    # Null model (intercept only): P(Y=1) is empirical p.
    # logL_null = n1 * ln(p_hat) + n0 * ln(1 - p_hat)
    # But let's use sklearn to be safe or analytical for null.
    
    p_hat = n1 / n_sim
    logL_null = n1 * np.log(p_hat) + n0 * np.log(1 - p_hat)
    
    clf = LogisticRegression(penalty=None, solver='lbfgs') # No regularization to match R glm
    clf.fit(X, y)
    
    # Calculate Log Likelihood of fitted model
    # predict_proba returns [prob_0, prob_1]
    probs = clf.predict_proba(X)[:, 1]
    
    # Avoid log(0)
    epsilon = 1e-15
    probs = np.clip(probs, epsilon, 1 - epsilon)
    
    logL_model = np.sum(y * np.log(probs) + (1 - y) * np.log(1 - probs))
    
    # 4. Calculate Cox-Snell R2
    # R2 = 1 - exp( (logL_null - logL_model) * 2 / n )
    # Note: (Dev_null - Dev_model) = 2 * (logL_model - logL_null)
    # So exp( - (Dev_null - Dev_model)/n ) 
    # = exp( - 2(logL_model - logL_null)/n )
    # = exp( 2(logL_null - logL_model)/n )
    # Matches formula.
    
    r2_cs = 1 - np.exp((logL_null - logL_model) * 2 / n_sim)
    
    return r2_cs


def calculate_sample_size(p, parameters, r2=None, auc=None, shrinkage=0.9, conservative=False):
    """
    Main function to calculate minimum sample size.
    Must provide either r2 or auc.
    """
    
    # 1. Handle Performance Input
    r2_max = calculate_r2_max(p)
    
    if r2 is None:
        if auc is not None:
            r2 = auc_to_r2_simulation(auc, p)
        elif conservative:
            # Conservative R2 = 0.15 * R2_max
            r2 = 0.15 * r2_max
        else:
            raise ValueError("Must provide either r2, auc, or set conservative=True")
            
    # 2. Criteria Calculation
    
    # Criterion 1: Shrinkage
    # N1 = ceil( P / ( (S-1) * ln(1 - R2/S) ) )
    # Note: If R2 < S*0.9?? No, just standard formula.
    # If R2 > S, this formula might be unstable or result in negative?
    # R2 is usually < S (0.9). 
    # If R2 is very high, shrinkage is less of an issue.
    # But usually R2 <= 1. S=0.9.
    # If R2 > 0.9, we need to handle it? 
    # Riley paper assumes S < 1. 
    # If R2 > S, the log becomes log(negative).
    # In prediction, R2 is rarely > 0.9.
    # If R2 is high, we simply need fewer samples?
    # Let's assume standard range.
    
    try:
        val1 = 1 - (r2 / shrinkage)
        if val1 <= 0:
            n1 = float('inf') # Impossible if R2 >= S
        else:
            denom1 = (shrinkage - 1) * np.log(val1)
            n1 = np.ceil(parameters / denom1)
    except:
        n1 = float('nan')

    # Criterion 2: Small Error
    # S_diff assuming difference <= 0.05
    # S_req = R2 / (R2 + 0.05 * R2_max)
    # Then plug S_req into N formula
    s_required = r2 / (r2 + 0.05 * r2_max)
    
    try:
        val2 = 1 - (r2 / s_required)
        if val2 <= 0:
            n2 = float('inf')
        else:
            denom2 = (s_required - 1) * np.log(val2)
            n2 = np.ceil(parameters / denom2)
    except:
        n2 = float('nan')

    # Criterion 3: Precision (Intercept)
    # N3 = (1.96/0.05)^2 * p * (1-p)
    n3 = np.ceil( ( (1.96 / 0.05) ** 2 ) * p * (1 - p) )
    
    # Final N
    n_final = max(n1, n2, n3)
    
    # Recalculate implied shrinkage at N_min
    # S = 1 + (P / N) / ln(1 - R2*(1 - (P/N)/... ) ??)
    # Easier: use the formula rearranged or just report target.
    # pmsampsize reports the S implied by N_final.
    # Formula: S = 1 + P / (N * ln(1 - R2/S)) -> transcendental equation.
    # The package often solves it or reports the bounding one.
    # We can skip exact implied shrinkage for now or implement a solver later.
    # Just return which criterion was max.
    
    criteria_map = {1: n1, 2: n2, 3: n3}
    binding_criterion = max(criteria_map, key=criteria_map.get)
    
    return {
        "n_total": int(n_final),
        "n_events": int(n_final * p),
        "r2_cs": r2,
        "r2_max": r2_max,
        "criteria": {
            "c1_shrinkage": n1,
            "c2_small_error": n2,
            "c3_precision": n3
        },
        "binding_criterion": binding_criterion,
        "epp": (n_final * p) / parameters
    }

def generate_scenarios(p_list, params_list, perf_list, perf_type='auc', shrinkage=0.9):
    """
    Generates a grid of results.
    """
    results = []
    
    for p in p_list:
        for param in params_list:
            for perf in perf_list:
                
                # Setup kwargs
                kwargs = {
                    'p': p,
                    'parameters': param,
                    'shrinkage': shrinkage
                }
                
                if perf_type == 'auc':
                    kwargs['auc'] = perf
                elif perf_type == 'r2':
                    kwargs['r2'] = perf
                elif perf_type == 'conservative':
                    kwargs['conservative'] = True
                    # perf is ignored or used as dummy
                
                res = calculate_sample_size(**kwargs)
                
                row = {
                    'Prevalence': p,
                    'Parameters': param,
                    'Performance': perf, # AUC or R2 value input
                    'Metric Type': perf_type,
                    'R2_CS': res['r2_cs'],
                    'N_Total': res['n_total'],
                    'N_Events': res['n_events'],
                    'EPP': res['epp'],
                    'Binding_Crit': res['binding_criterion'],
                    'N_Crit1': res['criteria']['c1_shrinkage'],
                    'N_Crit2': res['criteria']['c2_small_error'],
                    'N_Crit3': res['criteria']['c3_precision']
                }
                results.append(row)
                
    return pd.DataFrame(results)

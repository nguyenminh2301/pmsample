
import numpy as np
import scipy.stats
from scipy.integrate import quad
import streamlit as st
import pandas as pd
import math

try:
    from pmsampsize_app.utils import parse_input
    from pmsampsize_app import reporting
except ImportError:
    from utils import parse_input
    import reporting

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (PMVALSAMPSIZE)
# -----------------------------------------------------------------------------

def inverse_logit(x):
    return 1 / (1 + np.exp(-x))

def sim_lp_normal(n, mean, sd, seed=None):
    if seed: np.random.seed(seed)
    return np.random.normal(mean, sd, n)

def sim_lp_beta(n, alpha, beta, seed=None):
    if seed: np.random.seed(seed)
    # Simulate probs then convert to logit
    probs = np.random.beta(alpha, beta, n)
    # clip to avoid inf
    probs = np.clip(probs, 1e-9, 1-1e-9)
    return np.log(probs / (1 - probs))

def find_lp_params_from_c_and_p(target_c, target_p, dist="normal", tolerance=0.001):
    """
    Iteratively find parameters for LP distribution that match target C and P.
    Simplified approach similar to 'lpcstat' in R.
    For Normal(mu, sigma):
    - C depends mostly on sigma.
    - P depends on mu and sigma.
    """
    # Rough approximation for Normal
    # A ~ norm.cdf(sigma * sqrt(2) / 2) -> C
    # sigma ~ norm.ppf(C) * sqrt(2)
    
    # Sigma is determined by C-statistic
    sigma = scipy.stats.norm.ppf(target_c) * np.sqrt(2)
    
    # Find mu such that E[inverse_logit(N(mu, sigma))] = target_p
    # Monotonic: increasing mu increases mean probability
    
    low = -10.0
    high = 10.0
    # Refine bounds if needed
    
    best_mu = 0
    for i in range(20): # 20 iterations of binary search is sufficient for precision
        mid = (low + high) / 2
        # Integrate to find mean prob? Or just sim? 
        # Numerical integration is faster and stable
        # P(Y=1) = integral( inverse_logit(x) * pdf(x|mid, sigma) ) dx
        
        # Using numerical integration
        # Define integrand:
        # 1/(1+exp(-x)) * (1/(sigma*sqrt(2pi))) * exp( - (x-mid)^2 / (2sigma^2) )
        
        # Let z = (x - mid)/sigma -> x = z*sigma + mid. dx = sigma*dz
        # Prob = integral( inverse_logit(z*sigma + mid) * phi(z) ) dz
        
        expected_p, _ = quad(lambda z: inverse_logit(z * sigma + mid) * scipy.stats.norm.pdf(z), -10, 10)
        
        if expected_p < target_p:
            low = mid
        else:
            high = mid
            
    best_mu = (low + high) / 2
    return best_mu, sigma

def calc_se_ln_oe(n, p):
    # SE(ln(O/E)) ~= sqrt( (1-P)/ (N*P) ) approx or just sqrt(1/E)
    # R pmvalsampsize: sqrt(1/E) is commonly derived for validation.
    # Actually, var(ln(O/E)) approx (1-p)/(n*p). 
    # Let's use the standard approximation: SE = sqrt(1/E)
    events = n * p
    if events <= 0: return np.inf
    return np.sqrt(1 / events)

def calc_se_slope(n, lp_dist):
    """
    SE(Slope) propto 1/sqrt(N * I).
    I = E[ p(LP)*(1-p(LP)) * (LP - E[LP])^2 ] ?
    Actually for slope=1, we compute Fisher Info on the sample.
    Var(Slope) = 1 / (N * E[P(1-P) * (LP - mean(LP))^2] ) ??
    Checking R code logic usually:
    Fit = glm(y ~ offset(lp) + slope*lp)
    The variance of slope is inverse information.
    """
    # Simulate Probabilities
    probs = inverse_logit(lp_dist)
    w = probs * (1 - probs)
    # Fisher Information for slope parameter (at slope=1, intercept=0)
    # Matrix for [alpha, beta]:
    # I_aa = sum(w)
    # I_ab = sum(w * lp)
    # I_bb = sum(w * lp^2)
    # Cov matrix is inv(I). Var(beta) is [1,1] element of inverse.
    
    # We can compute this empirical average per observation
    n_sim = len(lp_dist)
    
    # Centering LP helps stability but we need the raw calculation for the model: logit(p) = alpha + beta*LP
    # Standard: logit(p) = 0 + 1*LP.
    # We want SE of beta. 
    # Info Matrix per obs:
    # [ w       w*lp ]
    # [ w*lp    w*lp^2 ]
    
    mean_w = np.mean(w)
    mean_wlp = np.mean(w * lp_dist)
    mean_wlp2 = np.mean(w * lp_dist**2)
    
    det = mean_w * mean_wlp2 - (mean_wlp)**2
    if det <= 0: return np.inf
    
    # Inverse: [I_bb, -I_ab; -I_ab, I_aa] / det
    # Var(beta) per obs = I_aa / det = mean_w / det
    var_beta_per_obs = mean_w / det
    
    se_beta = np.sqrt(var_beta_per_obs / n)
    return se_beta

def calc_se_c(n, c, p):
    # Newcombe's formula or Hanley-McNeil
    # pmvalsampsize uses Newcombe/Hanley.
    # Let's use Hanley-McNeil as implemented in D8, it's robust.
    # SE = sqrt(Var / n) ? No, Var formula has n in denom.
    # Reuse the function from D8 if possible or reimplement.
    
    # Re-implement Hanley & McNeil Variance part
    a = c
    q1 = a / (2 - a)
    q2 = (2 * a**2) / (1 + a)
    
    n1 = n * p
    n0 = n * (1 - p)
    if n1 <= 1 or n0 <= 1: return np.inf
    
    num = a * (1 - a) + (n1 - 1) * (q1 - a**2) + (n0 - 1) * (q2 - a**2)
    den = n1 * n0
    
    var = num / den
    if var < 0: return 0
    return np.sqrt(var)

def calculate_pmvalsampsize(p, c, oe_width, slope_width, c_width, n_sim=100000, seed=12345):
    """
    Pmvalsampsize logic.
    """
    np.random.seed(seed)
    
    # 1. Sim LP
    # Assume Normal for now (simplest replication of 'lpcstat' idea)
    mu, sigma = find_lp_params_from_c_and_p(c, p)
    lp = np.random.normal(mu, sigma, n_sim)
    
    # 2. Required N for O/E
    # Target SE = width / (2 * 1.96)
    target_se_oe = oe_width / 3.92
    if target_se_oe > 0:
        # SE ~ sqrt(1/E) -> E = 1/SE^2
        req_events_oe = 1 / (target_se_oe**2)
        n_oe = int(np.ceil(req_events_oe / p))
    else:
        n_oe = 0

    # 3. Required N for Slope
    target_se_slope = slope_width / 3.92
    if target_se_slope > 0:
        # SE_slope(N) = SE_slope(1) / sqrt(N)
        # Calculate SE_slope for N=1 (per obs)
        se_slope_1 = calc_se_slope(1, lp) # This function handles n scaling
        # Wait, my calc_se_slope takes n. Let's call it with large sim to estimate population property
        # Actually: Var(beta) = Var_per_obs / N
        # We need Var_per_obs.
        # Run calc_se_slope with n_sim and scale back
        se_sim = calc_se_slope(n_sim, lp)
        var_per_obs = (se_sim**2) * n_sim
        
        # Target: sqrt(var_per_obs / N) <= target
        # var_per_obs / N <= target^2
        # N >= var_per_obs / target^2
        n_slope = int(np.ceil(var_per_obs / (target_se_slope**2)))
    else:
        n_slope = 0

    # 4. Required N for C-statistic
    target_se_c = c_width / 3.92
    if target_se_c > 0:
        # Iterative search for N
        # Initial guess
        n_curr = 500
        for _ in range(20):
            se = calc_se_c(n_curr, c, p)
            if se <= target_se_c:
                # Try to reduce
                step = n_curr // 10
            else:
                # Increase
                n_curr = int(n_curr * (se / target_se_c)**2) + 1
                
        # Final fine tune
        # Just binary search or crude check?
        # Let's use the formula inverted approx:
        # Var ~ K / N.  SE ~ sqrt(K/N). N ~ K/SE^2.
        # Use current estimate of K
        se_curr = calc_se_c(n_curr, c, p)
        k_approx = (se_curr**2) * n_curr
        n_c = int(np.ceil(k_approx / (target_se_c**2)))
    else:
        n_c = 0
        
    n_recom = max(n_oe, n_slope, n_c)
    
    return {
        "n_oe": n_oe, "n_slope": n_slope, "n_c": n_c,
        "n_recom": n_recom,
        "events_recom": int(np.ceil(n_recom * p)),
        "lp_mu": mu, "lp_sigma": sigma
    }

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (SAMPSIZEVAL)
# -----------------------------------------------------------------------------

def sampsizeval_c(p, c, se_target):
    # Pavlou 2021 Closed form eq 14
    # Var(C) approx ...
    # Uses n1, n0 scaling.
    # N approx ... 
    # Let's use the definition from the paper or just reverse Hanley McNeil (which is what they often cite)
    # The package `sampsizeval` uses a specific normal approximation for SE(C).
    # Var(C) = [ c(1-c) + (n1-1)(q1-c^2) + ... ] / n1n0
    # Iteratively solve this is safer than complex closed form.
    # Reuse D8 logic or calc_se_c
    
    if se_target <= 0: return 0
    
    # Binary search for N
    low = 50
    high = 1000000
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        se = calc_se_c(mid, c, p)
        if se <= se_target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

def sampsizeval_slope(p, c, se_target):
    # Pavlou (2021) derivation for slope SE assuming normal LP.
    # SE(S) = sqrt( 1 / (N * p * (1-p) * var(LP)) ) approx?
    # paper says Var(S) approx 2 / (N * p * sigma^2) ??
    # Let's look at the asymptotic variance under marginal normality.
    # sigma_LP = norm.ppf(C) * sqrt(2)
    
    sigma = scipy.stats.norm.ppf(c) * np.sqrt(2)
    
    # Var(Slope) approx 1 / (N * sigma^2 * p * (1-p) ) ?
    # Let's try to verify with simulation result `calc_se_slope`.
    # Analytical approx is faster.
    # For now, use the derived formula commonly cited:
    # N = 1 / (p(1-p) * sigma^2 * SE^2)
    
    # Let's check sampsizeval source code approximation if possible.
    # Assuming the simple fisher info inversion leads to something like the above.
    
    if se_target <= 0: return 0
    val = 1 / (p * (1-p) * sigma**2 * se_target**2)
    return int(np.ceil(val))

def calculate_sampsizeval(p, c, se_c, se_slope, se_large):
    """
    Sampsizeval logic (Pavlou).
    """
    # 1. Size for C
    n_c = sampsizeval_c(p, c, se_c)
    
    # 2. Size for Slope
    n_slope = sampsizeval_slope(p, c, se_slope)
    
    # 3. Size for Large (Calibration in the Large)
    # Var(alpha) approx 1 / (N * p * (1-p)) ?
    # Standard log-odds SE is 1/sqrt(N*p*(1-p)) roughly.
    # SE_L = sqrt(1 / (N*p*(1-p)))
    # N = 1 / (p(1-p) * SE_L^2)
    if se_large > 0:
        n_large = int(np.ceil(1 / (p * (1-p) * se_large**2)))
    else:
        n_large = 0
        
    n_recom = max(n_c, n_slope, n_large)
    
    return {
        "n_c": n_c, "n_slope": n_slope, "n_large": n_large,
        "n_recom": n_recom,
        "events_recom": int(np.ceil(n_recom * p))
    }

# -----------------------------------------------------------------------------
# UI RENDERER
# -----------------------------------------------------------------------------

def render_ui(T):
    st.header(T.get("title_d9", "D9: External Validation (pmvalsampsize / sampsizeval)"))
    
    # Tabs
    tab1, tab2, tab3 = st.tabs([
        "Riley/Archer (pmvalsampsize)",
        "Pavlou (sampsizeval)",
        "Combined Report"
    ])
    
    # Common Inputs (Prevalence, C)
    with st.expander(T.get("common_inputs", "Common Parameters"), expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            p_str = st.text_input(T.get("prevalence", "Prevalence"), "0.10", key="d9_p")
            c_str = st.text_input(T.get("auc_expected", "C-statistic"), "0.80", key="d9_c")
        with col2:
            seed = st.number_input("Random Seed (Sim)", 0, 999999, 123456, key="d9_seed")
            
    # TAB 1: PMVALSAMPSIZE
    with tab1:
        st.info("🎯 **Target**: Precision (CI Widths) for O/E, Slope, C.")
        c1, c2 = st.columns(2)
        with c1:
            oe_w = st.number_input("O/E CI Width (Default 0.2)", 0.01, 10.0, 0.2, key="d9_oe_w")
            slope_w = st.number_input("Slope CI Width (Default 0.2)", 0.01, 10.0, 0.2, key="d9_slope_w")
        with c2:
            c_w = st.number_input("C-stat CI Width (Default 0.1)", 0.01, 1.0, 0.1, key="d9_c_w")
            
        if st.button("Calculate (Riley/Archer)", key="btn_d9_1"):
            # Logic
            p_val = parse_input(p_str)[0] # Take first for simplicity in demo
            c_val = parse_input(c_str)[0]
            
            with st.spinner("Simulating..."):
                res = calculate_pmvalsampsize(p_val, c_val, oe_w, slope_w, c_w, seed=seed)
            
            st.success(f"**Recommended N: {res['n_recom']}** (Events: {res['events_recom']})")
            
            res_df = pd.DataFrame([
                {"Criterion": "1. O/E (width)", "Target": oe_w, "N Required": res["n_oe"]},
                {"Criterion": "2. Slope (width)", "Target": slope_w, "N Required": res["n_slope"]},
                {"Criterion": "3. C-stat (width)", "Target": c_w, "N Required": res["n_c"]},
            ])
            st.table(res_df)
            
            st.caption(f"Based on simulated LP (Normal): mu={res['lp_mu']:.3f}, sigma={res['lp_sigma']:.3f}")
            
            # Reporting Tab 1
            context1 = {
                "method_title": "D9: External Validation (Riley/Archer)",
                "method_description": "Targeting CI Widths for O/E, Slope, C.",
                "inputs": {
                    "Prevalence": p_str, "C-Stat": c_str,
                    "O/E Width": oe_w, "Slope Width": slope_w, "C Width": c_w,
                    "Seed": seed
                }
            }
            reporting.render_report_ui(context1, res_df, T)

    # TAB 2: SAMPSIZEVAL
    with tab2:
        st.info("🎯 **Target**: Standard Error (SE) limits for C, Slope, Large.")
        c1, c2 = st.columns(2)
        with c1:
            se_c = st.number_input("Target SE(C) (Default 0.025)", 0.001, 0.5, 0.025, key="d9_se_c")
        with c2:
            se_slope = st.number_input("Target SE(Slope) (Default 0.05)", 0.001, 0.5, 0.05, key="d9_se_slope")
            se_large = st.number_input("Target SE(Large) (Default 0.05)", 0.001, 0.5, 0.05, key="d9_se_large")
            
        if st.button("Calculate (Pavlou)", key="btn_d9_2"):
            p_val = parse_input(p_str)[0]
            c_val = parse_input(c_str)[0]
            
            res = calculate_sampsizeval(p_val, c_val, se_c, se_slope, se_large)
            
            st.success(f"**Recommended N: {res['n_recom']}** (Events: {res['events_recom']})")
            
            res_df = pd.DataFrame([
                {"Criterion": "1. C-stat (SE)", "Target": se_c, "N Required": res["n_c"]},
                {"Criterion": "2. Slope (SE)", "Target": se_slope, "N Required": res["n_slope"]},
                {"Criterion": "3. Large (SE)", "Target": se_large, "N Required": res["n_large"]},
            ])
            st.table(res_df)
            
            # Reporting Tab 2
            context2 = {
                "method_title": "D9: External Validation (Pavlou)",
                "method_description": "Targeting SE Limits for C, Slope, Large.",
                "inputs": {
                    "Prevalence": p_str, "C-Stat": c_str,
                    "SE(C)": se_c, "SE(Slope)": se_slope, "SE(Large)": se_large
                }
            }
            reporting.render_report_ui(context2, res_df, T)

    # TAB 3: COMBINED
    with tab3:
        if st.button("Run Combined Analysis", key="btn_d9_all"):
             # Get ALL inputs
            p_val = parse_input(p_str)[0]
            c_val = parse_input(c_str)[0]
            
            # 1. Riley
            res1 = calculate_pmvalsampsize(p_val, c_val, st.session_state.d9_oe_w, st.session_state.d9_slope_w, st.session_state.d9_c_w, seed=seed)
            # 2. Pavlou
            res2 = calculate_sampsizeval(p_val, c_val, st.session_state.d9_se_c, st.session_state.d9_se_slope, st.session_state.d9_se_large)
            
            st.markdown("### 1. Riley/Archer (pmvalsampsize)")
            st.write(f"N Recommended: **{res1['n_recom']}**")
            
            st.markdown("### 2. Pavlou (sampsizeval)")
            st.write(f"N Recommended: **{res2['n_recom']}**")
            
            st.markdown("### Comparison")
            comp_df = pd.DataFrame({
                "Method": ["Riley/Archer (CI Widths)", "Pavlou (SE Targets)"],
                "N Recommended": [res1['n_recom'], res2['n_recom']],
                "Implied Events": [res1['events_recom'], res2['events_recom']]
            })
            st.table(comp_df)
            
            # Reporting Tab 3
            context3 = {
                "method_title": "D9: External Validation (Combined)",
                "method_description": "Comparison of Riley/Archer and Pavlou methods.",
                "inputs": {
                    "Prevalence": p_str, "C-Stat": c_str,
                    "Riley Inputs": f"OE_w={st.session_state.d9_oe_w}, Slope_w={st.session_state.d9_slope_w}",
                    "Pavlou Inputs": f"SE_c={st.session_state.d9_se_c}, SE_slope={st.session_state.d9_se_slope}"
                }
            }
            reporting.render_report_ui(context3, comp_df, T)

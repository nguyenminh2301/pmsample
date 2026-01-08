
import numpy as np
import scipy.stats
import streamlit as st
import pandas as pd
try:
    from pmsampsize_app import reporting
except ImportError:
    import reporting

def calculate_n_hsieh(alpha, power, p0, odds_ratio, predictor_type, q=0.5, sd=1.0, r2=0.0):
    """
    Hsieh et al (1998) Statistics in Medicine.
    Sample size for logistic regression.
    
    Args:
        alpha: two-sided significance level
        power: 1 - beta
        p0: event rate at mean of X (or baseline)
        odds_ratio: target OR per unit change (or binary 0->1)
        predictor_type: 'binary' or 'continuous'
        q: prevalence of binary predictor X=1
        sd: standard deviation of continuous predictor
        r2: R-squared of X with other covariates
    """
    
    z_alpha = scipy.stats.norm.ppf(1 - alpha/2)
    z_beta = scipy.stats.norm.ppf(power)
    
    # Baseline event rate P_bar (overall average event rate)
    # Hsieh formula uses P_bar for the inflation factor?
    # Actually Hsieh 1998 Eq (1) for binary X:
    # n = (z_a + z_b)^2 / [ P*(1-P) * B^2 ] ?? No.
    
    # Let's use the explicit Hsieh formula.
    # log(OR) = beta
    beta = np.log(odds_ratio)
    
    # Event probability at mean
    # If p0 is "baseline event probability when X=0", that is specific.
    # Hsieh usually defines 'p' as the OVERALL event rate for the "univariate" calculation first.
    # Let's use the P1 formula.
    
    if predictor_type == 'binary':
        # Binary X (Bernoulli(q))
        # P_overall approx = (1-q)*P(Y=1|X=0) + q*P(Y=1|X=1)
        # P(Y=1|X=0) = p0
        # P(Y=1|X=1) = 1 / (1 + exp(-(logit(p0) + beta)))
        p1 = 1 / (1 + np.exp(-(np.log(p0/(1-p0)) + beta)))
        p_bar = (1-q)*p0 + q*p1
        
        # Hsieh Eq (1) for univariate binary:
        # n1 = (z_a + z_b)^2 / [p_bar * (1-p_bar) * q * (1-q) * beta^2] <-- This is Wald approx?
        # Better formula (Whittemore 1981, Hsieh 1998 refined):
        # n = (z_a*sqrt(V0) + z_b*sqrt(V1))^2 / (p1 - p0)^2 ? No, that's comparison of proportions.
        
        # Hsieh 1998:
        # P_bar = overall.
        # N = (Z_a + Z_b)^2 / [ P_bar(1-P_bar) * q(1-q) * beta^2 ] is too simple?
        # Actually Hsieh recommends using the comparison of proportions formula for binary X, 
        # then adjusting for multiple regression.
        # But let's use the formula commonly cited (Eq 1 in Hsieh 1998):
        # N = (Za + Zb)^2 / [ (1 - rho^2) * P(1-P) * sigma^2 * beta^2 ] ??? No that's continuous.
        
        # Correct approach for Binary from Hsieh 1998:
        # 1. Calculate n_univariate using comparison of two independent proportions formula (Fleiss).
        #    n_one_group = ...
        #    Total n = n_one_group / q + n_one_group / (1-q) ?
        
        # Streamlined approach often used in software (e.g. G*Power for Logistic, Hsieh):
        # Pr(Y=1|H0) = p_bar
        # N ~ (Za + Zb)^2 / (P(1-P) B^2 var(X)) ??
        
        # Let's stick to Hsieh 1998 EXACT steps for "Binary Covariate (B = 0 or 1)":
        # p1 = event rate at B=1 = p0*OR / (1 - p0 + p0*OR)
        # p_bar = (1-q)p0 + q*p1
        # N_univariate = [ (Z_a * sqrt( p_bar(1-p_bar)/q/(1-q) ) + Z_b * sqrt( p0(1-p0)/(1-q) + p1(1-p1)/q ) )^2 ] / (p0 - p1)^2
        # This is strictly the 2-prop test. Hsieh says this is valid for logistic too.
        
        term_num = (z_alpha * np.sqrt(p_bar*(1-p_bar)/(q*(1-q))) + 
                    z_beta * np.sqrt(p0*(1-p0)/(1-q) + p1*(1-p1)/q))**2
        term_den = (p0 - p1)**2
        n_uni = term_num / term_den
        
        # Adjustment for R2 (Multivariate)
        # N_multi = N_uni / (1 - R2)
        n_total = n_uni / (1 - r2)
        
        return int(np.ceil(n_total)), int(np.ceil(n_total * p_bar))

    else:
        # Continuous X (Normal(0, sd?))
        # Hsieh 1998 Eq (2):
        # N = (Za + Zb)^2 / [ P*(1-P) * beta^2 ]  where P is event rate at mean of X.
        # If X is standardized, var(X)=1. If not, multiply by sigma^2.
        # Adjusted N = N / (1 - rho^2).
        
        # P_bar = p0 (assuming p0 is at mean of X)
        # Beta = log(OR) per 1 SD change? User inputs OR per "unit".
        # If user says "OR per unit" and "SD=1", then Beta=log(OR).
        # If SD != 1, effective Beta* = Beta * SD. 
        # Actually formula is:
        # N = (Za + Zb)^2 / [ p_0(1-p_0) * (beta * sigma)^2 ]
        
        eff_beta = beta * sd
        
        num = (z_alpha + z_beta)**2
        den = p0 * (1 - p0) * (eff_beta**2)
        
        # Correction factor VIF
        n_uni = num / den
        n_total = n_uni / (1 - r2)
        
        return int(np.ceil(n_total)), int(np.ceil(n_total * p0))

def render_ui(T):
    st.header(T["title_b3"])
    
    col1, col2 = st.columns(2)
    with col1:
        alpha = st.number_input("Alpha (2-sided)", 0.001, 0.20, 0.05, step=0.005)
        power = st.number_input("Power", 0.1, 0.99, 0.80, step=0.05)
        p0 = st.number_input("Baseline Event Rate (p0)", 0.01, 0.99, 0.10, help="Event rate when X=mean (continuous) or X=0 (binary)")
        
    with col2:
        or_target = st.number_input("Target Odds Ratio (OR)", 0.1, 10.0, 1.5, help="Effect size to detect")
        pred_type = st.radio("Predictor Type", ["Binary", "Continuous"], horizontal=True)
        
    if pred_type == "Binary":
        q = st.number_input("Prevalence of X=1 (q)", 0.01, 0.99, 0.30)
        sd = 1.0
    else:
        q = 0.5
        sd = st.number_input("Standard Deviation of X", 0.1, 100.0, 1.0)
        
    r2 = st.number_input("R-squared with other covariates", 0.0, 0.9, 0.0, help="Variance Inflation Factor adjustment: N_adj = N / (1-R2)")
    
    
    if st.button("Calculate B3"):
        n_req, ev_req = calculate_n_hsieh(alpha, power, p0, or_target, pred_type.lower(), q, sd, r2)
        st.session_state["b3_result"] = {"n_req": n_req, "ev_req": ev_req}
        st.session_state["b3_inputs"] = {
            "alpha": alpha, "power": power, "p0": p0, "or_target": or_target,
            "pred_type": pred_type, "q": q, "sd": sd, "r2": r2
        }

    if "b3_result" in st.session_state:
        res = st.session_state["b3_result"]
        inp = st.session_state["b3_inputs"]
        
        n_req = res["n_req"]
        ev_req = res["ev_req"]
        
        st.success(f"Required Sample Size: **{n_req}**")
        st.info(f"Expected Events: ~{ev_req}")
        
        # Provide interpretation
        st.markdown(f"""
        **{T.get('interpretation', 'Interpretation')}**:
        To detect an OR of {inp['or_target']} with {int(inp['power']*100)}% power at alpha={inp['alpha']}, 
        assuming baseline rate {inp['p0']} and predictor properties defined, 
        you need {n_req} subjects.
        """)
        
        # Reporting
        df = pd.DataFrame({
            "Required_N": [n_req],
            "Expected_Events": [ev_req],
            "Alpha": [inp['alpha']],
            "Power": [inp['power']],
            "OR_Target": [inp['or_target']],
            "Baseline_P0": [inp['p0']]
        })
        
        context = {
            "method_title": T.get("title_b3", "Method B3: Hsieh (Logistic)"),
            "method_description": f"Hsieh et al. (1998) calculation for {inp['pred_type']} predictor.",
            "inputs": {
                "Alpha": inp['alpha'],
                "Power": inp['power'],
                "Baseline Rate (p0)": inp['p0'],
                "Target OR": inp['or_target'],
                "Predictor Type": inp['pred_type'],
                "X Prevalence (q)" if inp['pred_type'] == "Binary" else "SD": inp['q'] if inp['pred_type'] == "Binary" else inp['sd'],
                "R-squared": inp['r2']
            },
            "refresh_key": ["b3_result", "b3_inputs"]
        }
        reporting.render_report_ui(context, df, T)

    st.markdown("---")
    with st.expander(T.get("formulas_header", "Formulas & Technical Details")):
        st.markdown(T.get("b3_content_md", "Content not found."))


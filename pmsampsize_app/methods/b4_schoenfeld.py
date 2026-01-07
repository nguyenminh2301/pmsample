
import numpy as np
import scipy.stats
import streamlit as st
import pandas as pd

def calculate_n_schoenfeld(alpha, power, hr, predictor_type, q=0.5, sd=1.0, f_event=0.20):
    """
    Schoenfeld (1983) Biometrics.
    Sample size for Cox proportional hazards model.
    
    Args:
        alpha: two-sided significance level
        power: 1 - beta
        hr: hazard ratio
        predictor_type: 'binary' or 'continuous'
        q: prevalence of binary predictor X=1
        sd: standard deviation of continuous predictor
        f_event: expected probability of event (events / N_total)
    """
    
    z_alpha = scipy.stats.norm.ppf(1 - alpha/2)
    z_beta = scipy.stats.norm.ppf(power)
    
    log_hr = np.log(hr)
    
    # Required Events (d)
    # Schoenfeld formula:
    # d = (Za + Zb)^2 / (p * (1-p) * logHR^2)
    # where p is proportion of subjects in group 1 (for binary)
    # Or p_var * logHR^2 where p_var is variance of covariate?
    
    if predictor_type == 'binary':
        # Variance of binary X is q*(1-q)
        # d = (Za + Zb)^2 / (q * (1-q) * logHR^2)
        variance_x = q * (1-q)
    else:
        # Variance of continuous X is sd^2
        variance_x = sd**2
        
    num = (z_alpha + z_beta)**2
    den = variance_x * (log_hr**2)
    
    d_events = np.ceil(num / den)
    
    # Total Sample Size N
    # N = d / f_event
    N_total = np.ceil(d_events / f_event)
    
    return int(d_events), int(N_total)

def render_ui(T):
    st.header(T["title_b4"])
    
    col1, col2 = st.columns(2)
    with col1:
        alpha = st.number_input("Alpha (2-sided)", 0.001, 0.20, 0.05, step=0.005, key="b4_alpha")
        power = st.number_input("Power", 0.1, 0.99, 0.80, step=0.05, key="b4_power")
        hr = st.number_input("Hazard Ratio (HR)", 0.1, 10.0, 1.5, help="Effect size to detect", key="b4_hr")
        
    with col2:
        pred_type = st.radio("Predictor Type", ["Binary", "Continuous"], horizontal=True, key="b4_type")
        
        if pred_type == "Binary":
            q = st.number_input("Prevalence of X=1 (q)", 0.01, 0.99, 0.50, key="b4_q")
            sd = 1.0
        else:
            q = 0.5
            sd = st.number_input("Standard Deviation of X", 0.1, 100.0, 1.0, key="b4_sd")
            
        f_event = st.number_input("Expected Event Fraction (Prob(Event))", 0.01, 1.0, 0.20, help="Overall probability of observing an event during follow-up", key="b4_f")
    
    if st.button("Calculate B4", key="b4_btn"):
        d_req, n_req = calculate_n_schoenfeld(alpha, power, hr, pred_type.lower(), q, sd, f_event)
        
        st.success(f"Required Events: **{d_req}**")
        st.info(f"Required Total N: **{n_req}** (assuming {f_event*100:.1f}% event rate)")
        
        # Provide interpretation
        st.markdown(f"""
        **interpretation**:
        To detect a Hazard Ratio of {hr} with {int(power*100)}% power at alpha={alpha}, 
        you need {d_req} events. Given the event rate of {f_event}, this requires {n_req} total subjects.
        """)

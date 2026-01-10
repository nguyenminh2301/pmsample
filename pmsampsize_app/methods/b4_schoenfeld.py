
import numpy as np
import scipy.stats
import streamlit as st
import pandas as pd
try:
    from pmsampsize_app import reporting
except ImportError:
    import reporting

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
    
    # Import parser
    try:
        from pmsampsize_app.utils import parse_input
    except ImportError:
        from utils import parse_input

    col1, col2 = st.columns(2)
    with col1:
        alpha = st.number_input("Alpha (2-sided)", 0.001, 0.20, 0.05, step=0.005, key="b4_alpha")
        # Multi-value inputs
        power_str = st.text_input("Power #", "0.8, 0.9", help=T.get("input_help_multivalue"), key="b4_power")
        hr_str = st.text_input("Hazard Ratio (HR) #", "1.5, 2.0", help="Effect size to detect. " + T.get("input_help_multivalue"), key="b4_hr")
        
    with col2:
        pred_type = st.radio("Predictor Type", ["Binary", "Continuous"], horizontal=True, key="b4_type")
        
        if pred_type == "Binary":
            q = st.number_input("Prevalence of X=1 (q)", 0.01, 0.99, 0.50, key="b4_q")
            sd = 1.0
        else:
            q = 0.5
            sd = st.number_input("Standard Deviation of X", 0.1, 100.0, 1.0, key="b4_sd")
            
        f_event_str = st.text_input("Expected Event Fraction (Prob(Event)) #", "0.2, 0.3", help="Overall probability of observing an event. " + T.get("input_help_multivalue"), key="b4_f")
    
    
    st.caption(T.get("multivalue_note", "Note: Fields marked with # allow multiple values."))
    if st.button("Calculate", key="b4_btn"):
        try:
            # Parse inputs
            power_list = parse_input(power_str, float)
            hr_list = parse_input(hr_str, float)
            f_event_list = parse_input(f_event_str, float)
            
            results = []
            import itertools
            
            for power_val, hr_val, f_val in itertools.product(power_list, hr_list, f_event_list):
                d_req, n_req = calculate_n_schoenfeld(alpha, power_val, hr_val, pred_type.lower(), q, sd, f_val)
                results.append({
                    "Required_Events": d_req,
                    "Required_Total_N": n_req,
                    "Alpha": alpha,
                    "Power": power_val,
                    "HR_Target": hr_val,
                    "Event_Rate": f_val
                })
            
            df = pd.DataFrame(results)
            st.session_state["b4_result_df"] = df
            st.session_state["b4_inputs"] = {
                "alpha": alpha, "power_str": power_str, "hr_str": hr_str, "pred_type": pred_type,
                "q": q, "sd": sd, "f_event_str": f_event_str
            }
            
        except Exception as e:
            st.error(f"Error: {e}")

    if "b4_result_df" in st.session_state:
        df = st.session_state["b4_result_df"]
        inp = st.session_state["b4_inputs"]
        
        st.subheader("Results")
        st.dataframe(df, use_container_width=True)
        
        # Interpretation (single row)
        if len(df) == 1:
            row = df.iloc[0]
            st.success(f"Required Events: **{row['Required_Events']}**")
            st.info(f"Required Total N: **{row['Required_Total_N']}**")
            st.markdown(f"To detect HR={row['HR_Target']} with {int(row['Power']*100)}% power, you need {row['Required_Events']} events.")
        
        # Visualization (multiple rows)
        if len(df) > 1:
            st.markdown("### Visualization")
            
            import altair as alt
            x_axis = st.selectbox("X Axis", ["HR_Target", "Power", "Event_Rate"], key="b4_x")
            color_axis = st.selectbox("Color By", ["Power", "HR_Target", "Event_Rate"], key="b4_color")
            
            c = alt.Chart(df).mark_line(point=True).encode(
                x=alt.X(x_axis),
                y=alt.Y('Required_Total_N'),
                color=alt.Color(f'{color_axis}:O'),
                tooltip=['Required_Total_N', 'Required_Events', 'Power', 'HR_Target', 'Event_Rate']
            ).interactive()
            
            st.altair_chart(c, use_container_width=True)

        # Reporting
        context = {
            "method_title": T.get("title_b4", "Method B4: Schoenfeld (Cox)"),
            "method_description": f"Sensitivity analysis for {inp['pred_type']} predictor in Cox.",
            "inputs": {
                "Alpha": str(inp['alpha']),
                "Power": inp['power_str'],
                "Hazard Ratio": inp['hr_str'],
                "Predictor Type": inp['pred_type'],
                "X Prevalence (q)" if inp['pred_type'] == "Binary" else "SD": str(inp['q']) if inp['pred_type'] == "Binary" else str(inp['sd']),
                "Event Rate": inp['f_event_str']
            },
            "refresh_key": ["b4_result_df", "b4_inputs"]
        }
        reporting.render_report_ui(context, df, T)

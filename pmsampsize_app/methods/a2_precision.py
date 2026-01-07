
import streamlit as st
try:
    from pmsampsize_app.core import precision as core_precision
    from pmsampsize_app.utils import parse_input
except ImportError:
    from core import precision as core_precision
    from utils import parse_input

def render_ui(T):
    st.header(T["quick_mode_risk"])
    st.info(T["risk_help"])
    
    col1, col2 = st.columns(2)
    with col1:
        p_str = st.text_input(T["prevalence"], "0.1, 0.2, 0.5", key="q2_p")
        method = st.selectbox(T["ci_method"], ["wilson", "wald", "clopper-pearson"], 
                              format_func=lambda x: T[f"ci_method_{x.replace('clopper-pearson', 'cp')}"], key="q2_method")
    with col2:
        width_str = st.text_input(T["ci_half_width"], "0.01, 0.02, 0.03", key="q2_w")
        conf_str = st.text_input(T["ci_level"], "0.95, 0.99", key="q2_c")
        
    if st.button(T["calc_btn"], key="btn_q2"):
        try:
            p_list = parse_input(p_str)
            w_list = parse_input(width_str)
            c_list = parse_input(conf_str)
            
            df = core_quick_binom_precision.generate_binom_grid(p_list, w_list, c_list, method)
            st.dataframe(df.style.format({"P_expected": "{:.3f}", "Actual_Half_Width": "{:.4f}"}))
            st.download_button("Download CSV", df.to_csv(index=False).encode('utf-8'), "precision_results.csv")
        except Exception as e:
            st.error(f"Error: {e}")

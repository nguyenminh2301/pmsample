
import streamlit as st
try:
    from pmsampsize_app.core import precision as core_precision
    from pmsampsize_app.utils import parse_input
    from pmsampsize_app import reporting
except ImportError:
    from core import precision as core_precision
    from utils import parse_input
    import reporting

def render_ui(T):
    st.header(T["quick_mode_risk"])
    st.info(T["risk_help"])
    
    col1, col2 = st.columns(2)
    with col1:
        p_str = st.text_input(T["prevalence"], "0.1, 0.2", help=T.get("input_help_multivalue"), key="q2_p")
        method = st.selectbox(T["ci_method"], ["wilson", "wald", "clopper-pearson"], 
                              format_func=lambda x: T[f"ci_method_{x.replace('clopper-pearson', 'cp')}"], key="q2_method")
    with col2:
        width_str = st.text_input(T["ci_half_width"], "0.05, 0.1", help=T.get("input_help_multivalue"), key="q2_w")
        conf_str = st.text_input(T["ci_level"], "0.95", help=T.get("input_help_multivalue"), key="q2_c")
        
    if st.button(T["calc_btn"], key="btn_q2"):
        try:
            p_list = parse_input(p_str)
            w_list = parse_input(width_str)
            c_list = parse_input(conf_str)
            
            df = core_precision.generate_binom_grid(p_list, w_list, c_list, method)
            st.session_state["q2_result_df"] = df
            st.session_state["q2_inputs"] = {
                "p_str": p_str,
                "method": method,
                "width_str": width_str,
                "conf_str": conf_str
            }
        except Exception as e:
            st.error(f"Error: {e}")

    if "q2_result_df" in st.session_state:
        df = st.session_state["q2_result_df"]
        inputs = st.session_state["q2_inputs"]

        st.dataframe(df.style.format({"P_expected": "{:.3f}", "Actual_Half_Width": "{:.4f}"}))
        
        # Reporting & Download UI
        context = {
            "method_title": T["quick_mode_risk"],
            "method_description": T["risk_help"],
            "inputs": {
                T["prevalence"]: inputs["p_str"],
                T["ci_method"]: inputs["method"],
                T["ci_half_width"]: inputs["width_str"],
                T["ci_level"]: inputs["conf_str"]
            },
            "refresh_key": ["q2_result_df", "q2_inputs"]
        }
        reporting.render_report_ui(context, df, T)

    st.markdown("---")
    with st.expander(T["formulas_header"]):
        st.markdown(T["a2_content_md"])


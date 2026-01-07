
import streamlit as st
try:
    from pmsampsize_app.core import riley as core_riley
    from pmsampsize_app.utils import parse_input
except ImportError:
    # Fallback/Test context
    from core import riley as core_riley
    from utils import parse_input

def render_ui(T):
    st.header(T["method1_tab"])
    
    # Mode selection for Riley
    mode_riley = st.radio(T["mode"], [T["mode_single"], T["mode_batch"]], horizontal=True, key="riley_mode")
    is_batch = mode_riley == T["mode_batch"]
    
    col1, col2 = st.columns(2)
    with col1:
        if is_batch:
            p_input = st.text_input(T["prevalence"], value="0.1", help=T["prevalence_help"])
        else:
            p_val = st.number_input(T["prevalence"], min_value=0.001, max_value=0.999, value=0.1, step=0.01, format="%.3f", help=T["prevalence_help"], key="riley_p")
            p_input = str(p_val)
            
    with col2:
        if is_batch:
            param_input = st.text_input(T["parameters"], value="10", help=T["parameters_help"])
        else:
            param_val = st.number_input(T["parameters"], min_value=1, value=10, step=1, help=T["parameters_help"], key="riley_params")
            param_input = str(param_val)
            
    st.subheader(T["perf_measure"])
    perf_mode = st.radio("Performance Metric", ["AUC", "R2", "Conservative"], 
                            format_func=lambda x: {"AUC": T["perf_auc"], "R2": T["perf_r2"], "Conservative": T["perf_cons"]}[x], key="riley_perf_mode")
    
    perf_input = None
    if perf_mode != "Conservative":
        label = "AUC Value" if perf_mode == "AUC" else "R2 Value"
        default_val = "0.8" if perf_mode == "AUC" else "0.15"
        
        if is_batch:
            perf_input_raw = st.text_input(label, value=default_val, key="riley_perf_batch")
        else:
            val = st.number_input(label, value=float(default_val), step=0.01, key="riley_perf_single")
            perf_input_raw = str(val)
    else:
        perf_input_raw = "0"
        
    shrinkage = st.number_input(T["shrinkage"], value=0.9, min_value=0.5, max_value=0.99, step=0.05, help=T["shrinkage_help"], key="riley_shrink")
    
    if st.button(T["calc_btn"], type="primary", key="btn_riley"):
        try:
            p_list = parse_input(p_input, float)
            param_list = parse_input(param_input, int)
            perf_list = parse_input(perf_input_raw, float)
            
            # Validation
            if any(p <= 0 or p >= 1 for p in p_list):
                st.error(T["error_p"])
                return
            if perf_mode == "AUC" and any(a <= 0.5 or a >= 1 for a in perf_list):
                st.error(T["error_auc"])
                return
            
            perf_type_map = {"AUC": "auc", "R2": "r2", "Conservative": "conservative"}
            df = core_riley.generate_scenarios(p_list, param_list, perf_list, perf_type_map[perf_mode], shrinkage)
            
            st.divider()
            st.subheader(T["results"])
            st.info(f"ℹ️ **{T['sanity']}**: N(180 events) = {180/min(p_list):.0f} | N(250 events) = {250/min(p_list):.0f}")
            st.dataframe(df.style.format({"Prevalence": "{:.3f}", "R2_CS": "{:.3f}", "Performance": "{:.3f}", "EPP": "{:.1f}"}))
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(label=T["download_csv"], data=csv, file_name='riley_results.csv', mime='text/csv')

            st.markdown("---")
            with st.expander(T.get("formulas_header", "Formulas & Technical Details")):
                st.markdown(T.get("c5_content_md", "Content not found."))
            
        except Exception as e:
            st.error(f"{T['error_parse']} {e}")

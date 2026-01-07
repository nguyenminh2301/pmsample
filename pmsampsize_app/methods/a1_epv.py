
import streamlit as st

try:
    from pmsampsize_app.core import epv as core_epv
    from pmsampsize_app.utils import parse_input
except ImportError:
    from core import epv as core_epv
    from utils import parse_input

def render_ui(T):
    st.header(T["quick_mode_epv"])
    st.warning(f"**{T['epv_warning_title']}**: {T['epv_warning_text']}")
    
    col1, col2 = st.columns(2)
    with col1:
        p_str = st.text_input(T["prevalence"], "0.05-0.15", key="q1_p")
    with col2:
        P_str = st.text_input(T["parameters"], "10, 15, 20", key="q1_P")
        epv_str = st.text_input(T["target_epv"], "10, 15, 20", help=T["target_epv_help"], key="q1_epv")
        
    if st.button(T["calc_btn"], key="btn_q1"):
        try:
            # Helper to parse input (duplicated from app.py, maybe move to utils?)
            # For now defined locally or imported if we had a utils module
            from pmsampsize_app.app import parse_input
            
            p_list = parse_input(p_str)
            P_list = parse_input(P_str, int)
            epv_list = parse_input(epv_str)
            
            df = core_quick_epv.calculate_epv_size(p_list, P_list, epv_list)
            st.dataframe(df)
            st.download_button("Download CSV", df.to_csv(index=False).encode('utf-8'), "epv_results.csv")
        except Exception as e:
            st.error(f"Error: {e}")

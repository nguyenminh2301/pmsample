
import streamlit as st
import json
try:
    from pmsampsize_app.utils import parse_input
    from pmsampsize_app import reporting
except ImportError:
    from utils import parse_input
    import reporting

def render_ui(T):
    st.header(T["method2_tab"])
    
    st.warning("⚠️ **Beta Feature**: This method requires significantly more computational power and may take minutes to run. Ensure you have `pymc` and `statsmodels` installed.")
    
    with st.expander(T["formulas_header"]):
        st.markdown(T["c7_content_md"])
    
    # 1. DGM
    with st.expander(T["dgm_settings"], expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            p_true = st.number_input(T["prevalence"], 0.01, 0.99, 0.1, help=T["prevalence_help"], key="bayes_p")
            P = st.number_input(T["parameters"], 2, 100, 15, key="bayes_P")
        with col2:
            rho = st.number_input(T["correlation"], 0.0, 0.9, 0.1, key="bayes_rho")
            n_candidates_str = st.text_input(T["n_candidates"] + " #", "500, 1000, 1500, 2000", help=T["n_candidates_help"])
            
    # 2. Sim Settings
    with st.expander(T["sim_settings"], expanded=False):
        n_sims = st.number_input(T["n_sims"], 10, 1000, 50, key="bayes_nsims") # Default low for speed
        assurance_target = st.number_input(T["assurance_threshold"], 0.5, 0.99, 0.80, key="bayes_assur_thresh")
        
    start_seed = st.sidebar.number_input("Global Random Seed", 0, 999999999, 42, key="bayes_seed")
    
    st.caption(T.get("multivalue_note", "Note: Fields marked with # allow multiple values."))
    if st.button(T["run_simulation"], type="primary"):
        # Import bayes core here to handle load errors
        try:
            try:
                from pmsampsize_app.core.bayes import BayesianAssuranceSimulation, HAS_PYMC
            except ImportError:
                from core.bayes import BayesianAssuranceSimulation, HAS_PYMC
            
            if not HAS_PYMC:
                st.error("❌ **PyMC not found.** Please install PyMC to use this feature.")
                return
                
            n_cands = parse_input(n_candidates_str, int)
            n_bin = int(P / 3)
            n_cont = P - n_bin
            
            sim = BayesianAssuranceSimulation(
                p_true=p_true, P=P, n_continuous=n_cont, n_binary=n_bin, rho=rho,
                n_candidates=n_cands, n_sims=n_sims, start_seed=start_seed, assurance_threshold=assurance_target
            )
            
            
            with st.spinner(T["simulation_running"]):
                df_res, audit = sim.run()
                
            st.session_state["c7_data"] = {
                "df_res": df_res,
                "audit": audit,
                "inputs": {
                    "p_true": p_true, "P": P, "rho": rho,
                    "n_candidates": n_candidates_str, "n_sims": n_sims, 
                    "assurance_target": assurance_target, "seed": start_seed
                }
            }

        except Exception as e:
            st.error(f"Simulation Failed: {e}")
            # raise e # Don't raise in UI

    if "c7_data" in st.session_state:
        data = st.session_state["c7_data"]
        df_res = data["df_res"]
        audit = data["audit"]
        inp = data["inputs"]
        
        st.success("Analysis Complete!")
        st.dataframe(df_res)
        
        # Plot
        st.line_chart(df_res, x="N", y="assurance")
        
        # Reporting
        context = {
            "method_title": T.get("method2_tab", "Method C7: Bayesian Assurance"),
            "method_description": "Bayesian assurance simulation for sample size.",
            "inputs": {
                T["prevalence"]: inp["p_true"],
                T["parameters"]: inp["P"],
                T["correlation"]: inp["rho"],
                T["n_candidates"]: inp["n_candidates"],
                T["n_sims"]: inp["n_sims"],
                T.get("assurance_threshold", "Assurance Target"): inp["assurance_target"],
                "Global Seed": inp["seed"]
            },
            "refresh_key": ["c7_data"]
        }
        reporting.render_report_ui(context, df_res, T)
        
        # Extra JSON Download
        res_json = json.dumps({"results": df_res.to_dict(orient="records"), "audit": audit}, indent=2)
        st.download_button("Download JSON Report (with Audit)", res_json, "bayes_assurance_results.json", "application/json")
            


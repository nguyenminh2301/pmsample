
import streamlit as st
import json
import json
import matplotlib.pyplot as plt

try:
    from pmsampsize_app.core import dev_sim as core_dev_sim
    from pmsampsize_app.utils import parse_input
except ImportError:
    from core import dev_sim as core_dev_sim
    from utils import parse_input

def render_ui(T):
    st.header(T["method6_tab"])
    st.info(T["dev_sim_intro"])
    
    mode = st.radio(T["mode"], [T["dev_mode_simple"], T["dev_mode_custom"]], horizontal=True, key="dev_mode")
    is_simple = mode == T["dev_mode_simple"]
    
    col1, col2 = st.columns(2)
    with col1:
        p_true = st.number_input(T["prevalence"], 0.01, 0.99, 0.1, key="dev_p")
        P = st.number_input(T["parameters"], 2, 100, 10, key="dev_P")
        
    with col2:
        if is_simple:
            target_auc = st.number_input(T["target_auc"], 0.51, 0.99, 0.80, help=T["target_auc_help"], key="dev_auc")
            rho = 0.0
        else:
            target_auc = 0.8 # unused
            rho = st.number_input(T["correlation"], 0.0, 0.9, 0.2, key="dev_rho")
            
    n_candidates_str = st.text_input(T["n_candidates"], "1000, 1500, 2000, 3000, 5000", key="dev_n_cands")
    n_sims = st.number_input(T["n_sims"], 10, 5000, 200, key="dev_nsims")
    
    # Criteria Selector
    st.subheader(T["criteria_settings"])
    c1 = st.checkbox(T["crit_slope_mean"], True, key="c_mean")
    c2 = st.checkbox(T["crit_slope_ci"], True, key="c_ci")
    c3 = st.checkbox(T["crit_auc"], True, key="c_auc")
    
    start_seed = st.sidebar.number_input("Global Random Seed (Dev)", 0, 999999999, 20260107, key="dev_seed")
    
    if st.button(T["run_simulation"], type="primary", key="btn_dev"):
        try:
            n_cands = parse_input(n_candidates_str, int)
            
            sim_mode = "simple" if is_simple else "custom"
            
            sim = core_dev_sim.SampleSizeDevSimulation(
                mode=sim_mode, p_true=p_true, P=P, 
                target_auc=target_auc, rho=rho,
                n_candidates=n_cands, n_sims=n_sims,
                start_seed=start_seed
            )
            
            with st.spinner(T["simulation_running"]):
                df_res, audit = sim.run()
                
            # Construct a "Final Pass" column
            def check_row(r):
                passes = []
                if c1: passes.append(r["Slope_mean"] >= 0.9) # Simple check
                if c2: passes.append(r["pct_slope_09_11"] >= 0.8) # >80% in range
                if c3: passes.append(r["AUC_mean"] >= 0.75) # Fixed 0.75 or target?
                return all(passes) if passes else True
            
            df_res["MEETS_CRITERIA"] = df_res.apply(check_row, axis=1)
            
            st.success("Simulation Complete")
            
            # Plot
            fig, ax = plt.subplots(1, 2, figsize=(10, 4))
            ax[0].errorbar(df_res["N"], df_res["Slope_mean"], yerr=df_res["Slope_sd"], fmt='-o')
            ax[0].set_title("Mean Calibration Slope (+/- SD)")
            ax[0].axhline(1.0, color='gray', linestyle='--')
            ax[0].axhline(0.9, color='r', linestyle=':')
            
            ax[1].plot(df_res["N"], df_res["pct_slope_09_11"], '-o')
            ax[1].set_title("% Slope within [0.9, 1.1]")
            ax[1].axhline(0.8, color='r', linestyle='--')
            
            st.pyplot(fig)
            
            # Highlight N*
            passed = df_res[df_res["MEETS_CRITERIA"]]
            if not passed.empty:
                n_star = passed["N"].min()
                st.info(f"✅ **Recommended N = {n_star}** (First size meeting all active criteria)")
            else:
                st.warning("⚠️ No sample size met all criteria. Consider increasing N.")
                
            st.dataframe(df_res.style.format({
                "AUC_mean": "{:.3f}", "Slope_mean": "{:.3f}", "fallback_pct": "{:.2%}", "pct_slope_09_11": "{:.1%}"
            }))
            
            col_d1, col_d2 = st.columns(2)
            col_d1.download_button("Download CSV", df_res.to_csv(index=False).encode('utf-8'), "dev_sim_results.csv", "text/csv")
            col_d2.download_button(T["audit_trail"], json.dumps({"audit": audit}, default=str), "dev_sim_audit.json", "application/json")
            
        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")
    with st.expander(T.get("formulas_header", "Formulas & Technical Details")):
        st.markdown(T.get("c6_content_md", "Formulas not found."))

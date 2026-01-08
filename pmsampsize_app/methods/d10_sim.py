
import streamlit as st
import pandas as pd
import numpy as np
import time

try:
    from pmsampsize_app.utils import parse_input
    from pmsampsize_app.core.d10_sim import run_d10_simulation, solve_gamma_for_target_p, sim_lp_distribution
    from pmsampsize_app import reporting
except ImportError:
    from utils import parse_input
    from core.d10_sim import run_d10_simulation, solve_gamma_for_target_p, sim_lp_distribution
    import reporting

def render_ui(T):
    st.header(T.get("title_d10", "D10: External Validation Simulation"))
    
    # 1. LP Distribution Inputs
    with st.expander("1. " + T.get("d10_lp_dist", "LP Distribution"), expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            dist_type = st.selectbox(
                T.get("d10_lp_type", "LP Distribution Type"), 
                ["Normal (Log-Odds)", "Beta (Probabilities)"],
                index=0
            )
        
        lp_params = {}
        with col2:
            if "Normal" in dist_type:
                mu = st.number_input("Mean (mu)", value=-1.75, step=0.1)
                sd = st.number_input("SD (sigma)", value=1.47, min_value=0.1, step=0.1)
                lp_params = {"mu": mu, "sd": sd}
                lp_type_code = "normal"
            else:
                alpha = st.number_input("Alpha", value=2.0, min_value=0.1)
                beta_val = st.number_input("Beta", value=2.0, min_value=0.1)
                lp_params = {"alpha": alpha, "beta": beta_val}
                lp_type_code = "beta"

    # 2. Miscalibration Settings
    with st.expander("2. " + T.get("d10_miscal", "Miscalibration Assumptions"), expanded=True):
        miscal_mode = st.radio(
            "Miscalibration Mode", 
            ["Direct Input (Gamma, Slope)", "Solve for Target Prevalence"],
            horizontal=True
        )
        
        c1, c2 = st.columns(2)
        if "Direct" in miscal_mode:
            with c1:
                gamma = st.number_input("Gamma (Intercept)", value=0.0, step=0.1, help="0 means calibrated intercept if LP matches.")
            with c2:
                slope = st.number_input("Slope (S)", value=1.0, step=0.1, help="1 means calibrated slope.")
        else:
            with c1:
                target_p = st.number_input("Target Prevalence (p)", value=0.10, min_value=0.001, max_value=0.999)
            with c2:
                slope = st.number_input("Slope (S)", value=1.0, step=0.1)
                
            # Solve Gamma Button (Optional preview)
            gamma = 0 # Placeholder
            if st.button("Solve Gamma Preview"):
                def lp_gen(n): return sim_lp_distribution(n, lp_type_code, lp_params, seed=42)
                gamma = solve_gamma_for_target_p(target_p, slope, lp_gen)
                st.info(f"Solved Gamma: {gamma:.4f}")

    # 3. Targets
    with st.expander("3. " + T.get("d10_targets", "Precision Targets (CI Width)"), expanded=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            target_c = st.number_input("C-Stat Width", value=0.10, step=0.01)
        with c2:
            target_slope = st.number_input("Slope Width", value=0.20, step=0.01)
        with c3:
            target_oe = st.number_input("ln(O/E) Width", value=0.20, step=0.01)
            
        metrics = []
        if target_c > 0: metrics.append("c_stat")
        if target_slope > 0: metrics.append("slope")
        if target_oe > 0: metrics.append("ln_oe")

    # 4. Simulation Settings
    with st.expander("4. " + T.get("d10_sim_settings", "Simulation Settings")):
        c1, c2 = st.columns(2)
        with c1:
            n_start = st.number_input("Start N", value=200, step=50)
            n_end = st.number_input("End N", value=2000, step=50)
            n_step = st.number_input("Step N", value=100, step=50)
        with c2:
            n_sims = st.number_input("Repetitions (R)", value=200, step=100)
            seed = st.number_input("Seed", value=12345)

    # Run
    if st.button(T.get("calc_btn", "Calculate"), key="btn_d10"):
        st.info("Running simulation... This may take a moment.")
        prog = st.progress(0)
        
        # Resolve Gamma if needed
        if "Solve" in miscal_mode:
            def lp_gen(n): return sim_lp_distribution(n, lp_type_code, lp_params, seed=seed)
            gamma = solve_gamma_for_target_p(target_p, slope, lp_gen)
            st.write(f"**Solved Gamma**: {gamma:.4f} (Target P={target_p})")
            
        n_list = list(range(int(n_start), int(n_end)+1, int(n_step)))
        
        # Run
        t0 = time.time()
        res_df, audit = run_d10_simulation(
            n_list, 
            dist_type=lp_type_code, 
            dist_params=lp_params,
            gamma=gamma, 
            slope_true=slope,
            n_sims=int(n_sims),
            seed_start=int(seed),
            metrics=metrics
        )
        t1 = time.time()
        
        st.success(f"Simulation completed in {t1-t0:.2f}s")
        
        # Analysis
        # Check pass
        res_df["Pass_C"] = (res_df["Mean_C_Width"] <= target_c) if "c_stat" in metrics else True
        res_df["Pass_Slope"] = (res_df["Mean_Slope_Width"] <= target_slope) if "slope" in metrics else True
        res_df["Pass_OE"] = (res_df["Mean_OE_Width"] <= target_oe) if "ln_oe" in metrics else True
        
        res_df["ALL_PASS"] = res_df["Pass_C"] & res_df["Pass_Slope"] & res_df["Pass_OE"]
        
        # Find first pass
        pass_df = res_df[res_df["ALL_PASS"]]
        if not pass_df.empty:
            rec_n = pass_df.iloc[0]["N"]
            st.success(f"**Recommended Minimal N: {rec_n}**")
        else:
            st.warning("No candidate N met all targets. Increase N range.")
            
        st.dataframe(res_df.style.format("{:.3f}", subset=[c for c in res_df.columns if "Width" in c]))
        
        # Plot
        st.line_chart(res_df, x="N", y=[c for c in res_df.columns if "Mean" in c])
        
        st.line_chart(res_df, x="N", y=[c for c in res_df.columns if "Mean" in c])
        
        # Reporting
        context = {
            "method_title": T.get("title_d10", "D10: Sim Validation"),
            "method_description": "Simulation for external validation sample size.",
            "inputs": {
                "LP Type": dist_type,
                "LP Params": str(lp_params),
                "Miscal Mode": miscal_mode,
                "Gamma": gamma,
                "Slope": slope,
                "Targets": f"C={target_c}, S={target_slope}, OE={target_oe}",
                "Sim": f"R={n_sims}, Seed={seed}"
            }
        }
        reporting.render_report_ui(context, res_df, T)

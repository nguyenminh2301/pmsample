
import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats
try:
    from pmsampsize_app.utils import parse_input
    from pmsampsize_app.core.d8_auc import prec_auc
except ImportError:
    from utils import parse_input
    from core.d8_auc import prec_auc

def render_ui(T):
    st.header(T["title_d8"])
    st.info(T["d8_desc"])
    
    # Mode Selection
    mode = st.radio(
        T["mode"], 
        [T["d8_mode_width_to_n"], T["d8_mode_n_to_width"]],
        index=0,
        key="d8_mode_selection"
    )
    
    is_finding_n = (mode == T["d8_mode_width_to_n"])
    
    col1, col2 = st.columns(2)
    with col1:
        auc_str = st.text_input(T["auc_expected"], "0.80", key="d8_auc")
        p_str = st.text_input(T["prevalence"], "0.10", key="d8_p")
        
    with col2:
        if is_finding_n:
            target_str = st.text_input(T["d8_width_input"], "0.10", key="d8_width")
        else:
            target_str = st.text_input(T["d8_n_input"], "500", key="d8_n")
            
        conf_str = st.text_input(T["ci_level"], "0.95", key="d8_conf")

    # Advanced Options
    with st.expander(T["d8_opt_settings"]):
        opt_upper = st.number_input(T["d8_opt_bound"], 1000.0, 10000000.0, 1000000.0, step=1000.0, key="d8_opt_upper")
        opt_tol = st.number_input(T["d8_opt_tol"], 1e-6, 1e-2, 1e-4, format="%.5f", key="d8_opt_tol")
        
        show_rounding = False
        if is_finding_n:
            show_rounding = st.checkbox(T["d8_practical_rounding"], value=False, key="d8_round")

    # Calculate Button
    if st.button(T["calc_btn"], key="btn_d8"):
        try:
            auc_list = parse_input(auc_str)
            p_list = parse_input(p_str)
            target_list = parse_input(target_str)
            conf_list = parse_input(conf_str)
            
            results = []
            
            for auc in auc_list:
                for p in p_list:
                    for target in target_list:
                        for conf in conf_list:
                            # Prepare inputs for prec_auc
                            n_val = None
                            width_val = None
                            
                            if is_finding_n:
                                width_val = target
                            else:
                                n_val = target
                                
                            try:
                                res = prec_auc(
                                    auc=auc, 
                                    prev=p, 
                                    n=n_val, 
                                    conf_width=width_val, 
                                    conf_level=conf,
                                    opt_upper=opt_upper,
                                    opt_tol=opt_tol
                                )
                                
                                # Format for DataFrame
                                row = {
                                    "AUC": res["auc"],
                                    "Prev": res["prev"],
                                    "Conf.Level": res["conf_level"],
                                    "Method": res["method"]
                                }
                                
                                if is_finding_n:
                                    row["Target Width"] = target
                                    row["N (Float)"] = res["n"]
                                    row["Achieved Width"] = res["conf_width"]
                                    
                                    if show_rounding:
                                        n_int = int(np.ceil(res["n"]))
                                        row["N (Pract)"] = n_int
                                        # Re-calc for integer N
                                        res_int = prec_auc(auc, p, n=n_int, conf_level=conf)
                                        row["Width (Pract)"] = res_int["conf_width"]
                                else:
                                    row["N"] = res["n"]
                                    row["Achieved Width"] = res["conf_width"]
                                    
                                row["Lwr"] = res["lwr"]
                                row["Upr"] = res["upr"]
                                row["N1"] = res["n1"]
                                row["N2"] = res["n2"]
                                
                                results.append(row)
                                
                            except Exception as e_inner:
                                st.error(f"Error for (AUC={auc}, Prev={p}): {e_inner}")

            if results:
                df = pd.DataFrame(results)
                
                # Column Ordering
                base_cols = ["AUC", "Prev", "Conf.Level"]
                if is_finding_n:
                    cols = base_cols + ["Target Width", "N (Float)", "Achieved Width"]
                    if show_rounding:
                        cols += ["N (Pract)", "Width (Pract)"]
                else:
                    cols = base_cols + ["N", "Achieved Width"]
                    
                cols += ["Lwr", "Upr", "Method"]
                
                # Available columns only
                final_cols = [c for c in cols if c in df.columns]
                df = df[final_cols]

                st.success(f"Calculated {len(df)} scenarios.")
                
                # Format for display
                st.dataframe(df.style.format({
                    "AUC": "{:.2f}",
                    "Prev": "{:.2f}",
                    "Conf.Level": "{:.2f}",
                    "N (Float)": "{:.2f}",
                    "Target Width": "{:.3f}",
                    "Achieved Width": "{:.4f}",
                    "Lwr": "{:.3f}",
                    "Upr": "{:.3f}",
                    "N (Pract)": "{:.0f}",
                    "Width (Pract)": "{:.4f}",
                    "N": "{:.2f}"
                }))
                
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(T["download_csv"], csv, "d8_auc_presize.csv")
                
        except Exception as e:
            st.error(f"{T['error_parse']} {e}")
            
    st.markdown("---")
    with st.expander(T["formulas_header"]):
        st.latex(r"SE(AUC) = \sqrt{ \frac{A(1-A) + (n_1-1)(Q_1 - A^2) + (n_0-1)(Q_2 - A^2)}{n_1 n_0} }")
        st.latex(r"Q_1 = \frac{A}{2-A}, \quad Q_2 = \frac{2A^2}{1+A}")
        st.markdown(T["d8_assumptions"])
        st.markdown("**Reference**: Hanley JA, McNeil BJ (1982). Radiology. *presize* R package (v0.3.9).")

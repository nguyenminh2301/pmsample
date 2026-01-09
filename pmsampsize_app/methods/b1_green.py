
import streamlit as st
import pandas as pd
import altair as alt

try:
    from pmsampsize_app.core.green_rule_calculator import calculate_green_rule
    from pmsampsize_app.utils import parse_input
    import pmsampsize_app.reporting as reporting
except ImportError:
    from core.green_rule_calculator import calculate_green_rule
    from utils import parse_input
    import reporting

def render_ui(T):
    st.header(T.get("title_b1", "Method B1: Green's Rule"))
    
    st.markdown(f"""
    **{T.get("b1_desc", "Heuristic sample size for multiple linear regression.")}**
    
    Green (1991) suggests simple rules of thumb based on the number of predictors ($m$).
    """)
    
    # --- Inputs ---
    col1, col2 = st.columns(2)
    
    with col1:
        # Rule Type
        rule_options = ["Partial Correlation (104 + m)", "Multiple Correlation (50 + 8m)"]
        rule_sel = st.radio(
            "Rule Type", 
            rule_options, 
            index=0,
            help="Choose 'Partial' for testing individual coefficients (more conservative) or 'Multiple' for overall model R-squared."
        )
        is_partial = "Partial" in rule_sel
        rule_code = "partial" if is_partial else "multiple"
        
        # Predictors (m)
        m_str = st.text_input(
            "Number of Predictors (m)", 
            "5, 10, 15", 
            help=T.get("input_help_multivalue", "Supports multiple values separated by commas.")
        )
        
    with col2:
        # Sensitivity Analysis Parameters
        st.markdown("##### Sensitivity Adjustment")
        use_sensitivity = st.checkbox("Compare with Power Calculation", value=True)
        
        if use_sensitivity:
            alpha = st.number_input("Alpha", 0.001, 0.20, 0.05, step=0.005, key="b1_alpha")
            power = st.number_input("Power", 0.1, 0.99, 0.80, step=0.05, key="b1_power")
            
            es_mode = st.selectbox(
                "Effect Size (f²)", 
                ["Medium (0.15)", "Small (0.02)", "Large (0.35)", "Custom"],
                index=0
            )
            
            if "Custom" in es_mode:
                effect_size = st.number_input("Custom f²", 0.001, 10.0, 0.15, step=0.01)
            elif "Small" in es_mode: effect_size = 0.02
            elif "Large" in es_mode: effect_size = 0.35
            else: effect_size = 0.15
        else:
            alpha = 0.05
            power = 0.80
            effect_size = 0.15

    # --- Calculation ---
    if st.button(T.get("calc_btn", "Calculate"), key="btn_b1"):
        try:
            # Parse m
            m_list = parse_input(m_str, int)
            
            # Backend Call
            df = calculate_green_rule(
                m=m_list,
                rule_type=rule_code,
                alpha=alpha,
                power=power,
                effect_size=effect_size,
                sensitivity_mode=use_sensitivity
            )
            
            # Save to session
            st.session_state["b1_result"] = df
            st.session_state["b1_inputs"] = {
                "m_str": m_str, "rule_sel": rule_sel, 
                "use_sensitivity": use_sensitivity,
                "alpha": alpha, "power": power, "es": effect_size
            }
            
        except Exception as e:
            st.error(f"Error: {e}")
            
    # --- Results Display ---
    if "b1_result" in st.session_state:
        df = st.session_state["b1_result"]
        inp = st.session_state["b1_inputs"]
        
        st.divider()
        st.subheader("Results")
        
        # 1. Main Table
        st.dataframe(df, use_container_width=True)
        
        # 2. Key Insights
        if inp["use_sensitivity"] and len(df) > 0:
            # Check for large discrepancies
            diffs = df["adjusted_N"] - df["green_rule_N"]
            max_diff = diffs.max()
            
            if max_diff > 50:
                 st.warning(f"⚠️ Power-based calculation suggests significantly higher Sample Size than Green's Rule for some scenarios (up to +{int(max_diff)}). Green's Rule may be underpowered for small effect sizes.")
            elif diffs.min() < -50:
                 st.info("ℹ️ Green's Rule appears conservative (suggests higher N) compared to the specific power calculation.")
        
        # 3. Visualization
        if len(df) > 0:
            st.markdown("### Visualization")
            
            # Reshape for easier plotting (Long format)
            plot_df = df.copy()
            # We want to plot 'm' vs 'N', differentiated by 'Type' (Green vs Adjusted)
            
            melted = []
            for _, row in plot_df.iterrows():
                melted.append({"m": row["m"], "N": row["green_rule_N"], "Source": "Green's Rule"})
                if "adjusted_N" in row:
                    melted.append({"m": row["m"], "N": row["adjusted_N"], "Source": "Power-Adjusted"})
            
            df_long = pd.DataFrame(melted)
            
            c = alt.Chart(df_long).mark_line(point=True).encode(
                x=alt.X('m:Q', title="Number of Predictors (m)"),
                y=alt.Y('N:Q', title="Required Sample Size"),
                color='Source:N',
                tooltip=['m', 'N', 'Source']
            ).interactive()
            
            st.altair_chart(c, use_container_width=True)
            
        # 4. Report Generation
        context = {
            "method_title": T.get("title_b1", "Method B1: Green's Rule"),
            "method_description": f"Green's Rule ({inp['rule_sel']}) with sensitivity check.",
            "inputs": {
                "Predictors (m)": inp["m_str"],
                "Rule Type": inp["rule_sel"],
                "Compare Power": str(inp["use_sensitivity"]),
                "Alpha": str(inp["alpha"]),
                "Power": str(inp["power"]),
                "Effect Size (f2)": str(inp["es"])
            },
            "refresh_key": ["b1_result", "b1_inputs"]
        }
        reporting.render_report_ui(context, df, T)
        
        # 5. Technical Notes
        st.markdown("---")
        with st.expander("Method Details"):
            st.markdown(r"""
            **Green's Rule (1991):**
            *   **Multiple Correlation ($R^2$)**: $N \ge 50 + 8m$
            *   **Partial Correlation ($\beta_j$)**: $N \ge 104 + m$
            
            **Power Adjustment:**
            Calculated using the non-central $F$-distribution:
            *   $F(df_{num}, df_{denom}, \lambda)$
            *   $\lambda = f^2 \times N$
            *   Iterative search to find minimum $N$ satisfying Power $1 - \beta$.
            """)

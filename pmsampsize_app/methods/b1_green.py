
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
            "Number of Predictors (m) #", 
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
    st.caption(T.get("multivalue_note", "Note: Fields marked with # allow multiple values."))
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

    # 5. Documentation Section
    st.divider()
    with st.expander(T.get("formulas_header", "📚 Formulas & technical details")):
        lang = st.session_state.get("lang", "EN")
        if lang == "VI":
            render_vi_docs()
        else:
            render_en_docs()

def render_en_docs():
    st.markdown(r"""
### B1: Green's Rule (1991) — English

#### What this is
**Green's rule** is a heuristic (rule-of-thumb) approach to sample size planning for **multiple linear regression**, expressed purely as a function of the number of predictors ($m$) — no assumed effect size, variance, or pilot data is required up front.

#### The two rules
*   **Testing the overall model (multiple correlation, $R^2$):**
    $$ N \ge 50 + 8m $$
*   **Testing individual predictors (partial correlation, $\beta_j$):**
    $$ N \ge 104 + m $$

where $m$ is the number of predictors in the model. Use the **partial correlation** rule when your primary interest is testing/estimating individual predictor coefficients; use the **multiple correlation** rule when your primary interest is the overall model $R^2$.

---

#### Power-based cross-check (in this calculator)
To sanity-check Green's heuristic against a formal power calculation, the calculator also computes the $N$ required to reach a target power for the same overall $F$-test, using the **non-central $F$-distribution**:
$$ F \sim F(df_{num}, df_{denom}, \lambda), \qquad \lambda = f^2 \times N $$
where $f^2$ is Cohen's effect size ($df_{num}=m$, $df_{denom}=N-m-1$), and the app searches iteratively for the smallest $N$ with $\Pr(F > F_{crit}(\alpha, df_{num}, df_{denom})\mid \lambda) \ge$ target power.

**Interpreting the comparison:**
*   If the power-based $N$ is **much larger** than Green's $N$, Green's rule may be **under-powered** for the assumed effect size — consider a larger sample.
*   If the power-based $N$ is **smaller**, Green's rule is the more **conservative** choice.

---

#### Practical guidance
*   $f^2 = 0.02$ (small), $0.15$ (medium), $0.35$ (large) follow Cohen's (1988) conventions; "medium" is a reasonable default with no pilot data.
*   Green's rule does not account for multicollinearity among predictors; if predictors are highly correlated, treat its result as a lower bound.

#### Key references
1. Green SB. *How many subjects does it take to do a regression analysis?* Multivariate Behavioral Research. 1991;26(3):499–510.
2. Cohen J. *Statistical Power Analysis for the Behavioral Sciences.* 2nd ed. Lawrence Erlbaum Associates; 1988.
""")

def render_vi_docs():
    st.markdown(r"""
### B1: Quy tắc Green (1991) — Tiếng Việt

#### Mục đích và bản chất
**Quy tắc Green** là cách ước tính nhanh (heuristic) cỡ mẫu cho **hồi quy tuyến tính đa biến**, chỉ phụ thuộc vào số biến dự báo ($m$) — không cần giả định trước về cỡ hiệu ứng, phương sai, hay dữ liệu pilot.

#### Hai quy tắc
*   **Kiểm định mô hình tổng thể (hệ số tương quan bội, $R^2$):**
    $$ N \ge 50 + 8m $$
*   **Kiểm định từng biến dự báo riêng lẻ (hệ số tương quan riêng phần, $\beta_j$):**
    $$ N \ge 104 + m $$

trong đó $m$ là số biến dự báo trong mô hình. Dùng quy tắc **tương quan riêng phần** khi quan tâm chính là kiểm định/ước lượng từng hệ số hồi quy; dùng quy tắc **tương quan bội** khi quan tâm chính là $R^2$ của toàn mô hình.

---

#### Đối chiếu với tính công suất (trong công cụ này)
Để kiểm tra chéo quy tắc kinh nghiệm của Green với một phép tính công suất chính thức, công cụ này cũng tính $N$ cần thiết để đạt công suất mục tiêu cho cùng kiểm định $F$ tổng thể, dùng **phân phối $F$ không trung tâm**:
$$ F \sim F(df_{num}, df_{denom}, \lambda), \qquad \lambda = f^2 \times N $$
trong đó $f^2$ là cỡ hiệu ứng của Cohen ($df_{num}=m$, $df_{denom}=N-m-1$), và ứng dụng tìm lặp $N$ nhỏ nhất sao cho $\Pr(F > F_{crit}(\alpha, df_{num}, df_{denom})\mid \lambda) \ge$ công suất mục tiêu.

**Cách diễn giải khi so sánh:**
*   Nếu $N$ theo công suất **lớn hơn nhiều** so với $N$ của Green, quy tắc Green có thể **chưa đủ công suất** với cỡ hiệu ứng giả định — nên cân nhắc cỡ mẫu lớn hơn.
*   Nếu $N$ theo công suất **nhỏ hơn**, quy tắc Green là lựa chọn **bảo thủ hơn** (an toàn hơn).

---

#### Hướng dẫn thực hành
*   $f^2 = 0.02$ (nhỏ), $0.15$ (trung bình), $0.35$ (lớn) theo quy ước của Cohen (1988); "trung bình" là lựa chọn hợp lý khi chưa có dữ liệu pilot.
*   Quy tắc Green không tính đến đa cộng tuyến (multicollinearity) giữa các biến dự báo; nếu các biến tương quan mạnh với nhau, nên xem kết quả này là cận dưới.

#### Tài liệu tham khảo
1. Green SB. *How many subjects does it take to do a regression analysis?* Multivariate Behavioral Research. 1991;26(3):499–510.
2. Cohen J. *Statistical Power Analysis for the Behavioral Sciences.* 2nd ed. Lawrence Erlbaum Associates; 1988.
""")

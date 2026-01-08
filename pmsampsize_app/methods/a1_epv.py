
import streamlit as st

try:
    from pmsampsize_app.core import epv as core_epv
    from pmsampsize_app.utils import parse_input
    from pmsampsize_app import reporting
except ImportError:
    from core import epv as core_epv
    from utils import parse_input
    import reporting

def render_ui(T):
    st.header(T["quick_mode_epv"])
    st.warning(f"**{T['epv_warning_title']}**: {T['epv_warning_text']}")
    
    col1, col2 = st.columns(2)
    with col1:
        p_str = st.text_input(T["prevalence"], "0.05-0.15", key="q1_p")
    with col2:
        P_str = st.text_input(T["parameters"], "10, 15, 20", key="q1_P")
        epv_str = st.text_input(T["target_epv"], "10, 15, 20", help=T["target_epv_help"], key="q1_epv")
        
    
    if st.button(T["calc_btn"]):
        try:
            # Parse inputs for the simplified A1 calculation
            # Assuming we take the first value from each list for this simplified A1
            p_list = parse_input(p_str, float)
            P_list = parse_input(P_str, int)
            epv_list = parse_input(epv_str, float)

            # Use the first value for the simplified A1 calculation
            # This is an interpretation based on the requested change's `calculate_epv(n_events, n_epv)`
            # and the original UI inputs.
            n_prevalence = p_list[0] if p_list else 0.05 # Default if input is empty
            n_parameters = P_list[0] if P_list else 10 # Default if input is empty
            n_epv = epv_list[0] if epv_list else 10 # Default if input is empty

            # Store in session state
            # The `calculate_epv` function needs `prevalence` as well to calculate N.
            # The requested snippet only had `n_events` and `n_epv`.
            # I'm interpreting `n_events` here as `n_parameters` (P) from the UI.
            # This is a significant deviation from the original `core_epv.calculate_epv_size`
            # which used `p_list`, `P_list`, `epv_list` to calculate `df`.
            # The requested `calculate_epv(n_events, n_epv)` seems to imply a different formula.
            # I will use `n_parameters` as `events_val` for the `calculate_epv` placeholder.
            # This is a best guess to make the provided snippet work.
            # Correct calculation (N = ceil( P * EPV / p ))
            import math
            req_events = n_parameters * n_epv
            req_n = math.ceil(req_events / n_prevalence)

            # Store in session state
            st.session_state["a1_result"] = req_n
            st.session_state["a1_inputs"] = {"prevalence": n_prevalence, "parameters": n_parameters, "epv": n_epv}
        except Exception as e:
            st.error(f"Error processing inputs for A1 calculation: {e}")

    # Display if result exists
    if "a1_result" in st.session_state:
        req_n = st.session_state["a1_result"]
        prevalence = st.session_state["a1_inputs"]["prevalence"]
        parameters = st.session_state["a1_inputs"]["parameters"]
        epv = st.session_state["a1_inputs"]["epv"]
        
        st.success(f"{T.get('result_a1', 'Required Sample Size')}: **{req_n}**")
        # The interpretation string needs to be adapted to the new inputs.
        # Original: ({events} events * {epv} EPV) = {req_n} subjects
        # New: (P parameters * t EPV) / p prevalence = N subjects
        st.info(f"{T.get('interpretation_a1', 'Interpretation')}: ({parameters} {T['parameters_short']} * {epv} {T['target_epv_short']}) / {prevalence} {T['prevalence_short']} = {req_n} {T['subjects_short']}")
        
        # Reporting
        df = pd.DataFrame({
            "Required_N": [req_n],
            "Prevalence": [prevalence],
            "Parameters": [parameters],
            "Target_EPV": [epv]
        })
        
        context = {
            "method_title": T.get("title_a1", "Method A1: EPV Rules"),
            "method_description": "Rules of thumb calculation based on EPV.",
            "inputs": {
                T["prevalence"]: str(prevalence),
                T["parameters"]: str(parameters),
                T["target_epv"]: str(epv)
            },
            "refresh_key": ["a1_result", "a1_inputs"]
        }
        reporting.render_report_ui(context, df, T)

    st.divider()
    
    # Documentation Section
    with st.expander(T.get("formulas_header", "📚 Formulas & technical details")):
        lang = st.session_state.get("lang", "EN")
        if lang == "VI":
            render_vi_docs()
        else:
            render_en_docs()

def render_en_docs():
    st.markdown("""
### A1: Rules of Thumb (EPV/EPP) — English

#### What this is
**EPV/EPP rules** are simple, *heuristic* checks that relate the **number of outcome events** to the **size/complexity of the model**. They were popularized from simulation work in logistic/Cox regression and are often used as a quick planning shortcut. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/8970487/))

**Important limitation:** EPV/EPP does **not** guarantee good **calibration**, **discrimination**, or low **optimism**—especially when you use non-linear terms (splines), interactions, variable selection, or have rare events. For prediction model development, modern guidance recommends principled approaches (e.g., Riley’s criteria) rather than relying on EPV alone. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29966490/))

---

#### Definitions: EPV vs EPP
*   **EPV (Events Per Variable):**
    $$ \\text{EPV} = \\frac{E}{K} $$
    where $E$ is the number of events and $K$ is the **number of candidate predictors (variables)**.

*   **EPP (Events Per Parameter / df):**
    $$ \\text{EPP} = \\frac{E}{P} $$
    where $P$ is the **number of predictor parameters (degrees of freedom)**, i.e., the number of regression coefficients to estimate **excluding the intercept**.

**Why EPP is preferred:** Many “variables” consume multiple parameters:
*   Categorical variable with $L$ levels $\\rightarrow$ $L-1$ parameters
*   Restricted cubic spline with $K$ knots $\\rightarrow$ $K-1$ parameters
*   Interaction between terms $\\rightarrow$ multiplies degrees of freedom (e.g., $df(A \\times B) = df(A) \\cdot df(B)$)

So, **EPP is usually more faithful** to true model complexity than EPV.

---

#### Inputs in the calculator
1.  **Outcome prevalence / event rate ($p$):** Expected proportion of events in the target dataset (e.g., 0.05–0.15).
2.  **Number of predictor parameters (df) ($P$):** Total degrees of freedom for all predictors **excluding intercept**.
3.  **Target EPP (or EPV) ($t$):** Common trial values: $t \\in \\{10, 15, 20\\}$.

---

#### Calculation (core formulas)
Let:
*   $N$ = total sample size
*   $E$ = number of events
*   $p$ = event rate
*   $P$ = number of parameters (df)
*   $t$ = target EPP

Expected events: $E \\approx N \\cdot p$  
Required events to meet target EPP: $E_{\\text{req}} = t \\cdot P$  
Required sample size:
$$ N_{\\text{req}} = \\lceil \\frac{E_{\\text{req}}}{p} \\rceil = \\lceil \\frac{t \\cdot P}{p} \\rceil $$

---

#### What values should you choose (typical conventions)?
Common practice is:
*   **10 EPP/EPV**: historical minimum starting point. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/8970487/))
*   **15–20 EPP/EPP**: more conservative for small/rare event rates, many parameters, or non-linear terms. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29966490/))

---

#### Key references
1. Peduzzi P, et al. *A simulation study of the number of events per variable in logistic regression analysis.* **J Clin Epidemiol**. 1996. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/8970487/))
2. Vittinghoff E, McCulloch CE. *Relaxing the rule of ten events per variable in logistic and Cox regression.* **Am J Epidemiol**. 2007. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/17182981/))
3. van Smeden M, et al. *Sample size for binary logistic prediction models: Beyond events per variable criteria.* **Stat Methods Med Res**. 2019. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29966490/))
4. Riley RD, et al. *Minimum sample size for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* **Stat Med**. 2019. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30357870/))
""")

def render_vi_docs():
    st.markdown("""
### A1: Quy tắc kinh nghiệm (EPV/EPP) — Tiếng Việt

#### Mục đích và bản chất
Quy tắc **EPV/EPP** là cách **ước tính nhanh (heuristic)** mối quan hệ giữa **số biến cố** và **độ phức tạp mô hình**. Quy tắc này xuất phát từ các nghiên cứu mô phỏng trong hồi quy logistic/Cox và thường được dùng như một “điểm xuất phát” khi lập kế hoạch. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/8970487/))

**Hạn chế quan trọng:** EPV/EPP **không bảo đảm** mô hình sẽ có **hiệu năng dự báo tốt** (calibration/discrimination) hoặc **ít lạc quan (optimism)**, đặc biệt khi có spline, tương tác, chọn biến, hoặc biến cố hiếm. Với nghiên cứu phát triển mô hình dự báo, nên ưu tiên các phương pháp có cơ sở hơn (ví dụ Riley/pmsampsize hoặc mô phỏng). ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29966490/))

---

#### EPV khác EPP như thế nào?
*   **EPV (Events Per Variable — biến cố trên mỗi biến):**
    $$ \\text{EPV} = \\frac{E}{K} $$
    Trong đó $E$ là số biến cố, $K$ là **số biến dự báo (variables)**.

*   **EPP (Events Per Parameter/df — biến cố trên mỗi tham số/bậc tự do):**
    $$ \\text{EPP} = \\frac{E}{P} $$
    Trong đó $P$ là **tổng số tham số (df)** cần ước lượng (**không tính intercept**).

**Vì sao nên dùng EPP?** Một “biến” có thể tiêu tốn nhiều tham số:
*   Biến phân loại có $L$ mức $\\rightarrow$ $L-1$ tham số
*   Spline RCS có $K$ nút $\\rightarrow$ $K-1$ tham số
*   Tương tác làm tăng df theo tích: $df(A \\times B) = df(A) \\cdot df(B)$

Do đó, **EPP phản ánh đúng độ phức tạp mô hình hơn EPV** trong đa số tình huống.

---

#### Chú giải các giá trị đầu vào (inputs)
1.  **Tỷ lệ biến cố ($p$):** Tỷ lệ kết cục xảy ra trong quần thể nghiên cứu (ví dụ 0,05–0,15).
2.  **Số tham số mô hình (df) ($P$):** Tổng bậc tự do của tất cả biến dự báo **không tính intercept**.
3.  **Ngưỡng EPP (hoặc EPV) mục tiêu ($t$):** Thường thử: $t \\in \\{10, 15, 20\\}$.

---

#### Cách tính (công thức cốt lõi)
Gọi:
*   $N$: cỡ mẫu
*   $E$: số biến cố
*   $p$: tỷ lệ biến cố
*   $P$: số tham số (df)
*   $t$: EPP mục tiêu

Số biến cố kỳ vọng: $E \\approx N \\cdot p$  
Số biến cố tối thiểu theo EPP mục tiêu: $E_{\\text{req}} = t \\cdot P$  
Suy ra cỡ mẫu tối thiểu:
$$ N_{\\text{req}} = \\lceil \\frac{E_{\\text{req}}}{p} \\rceil = \\lceil \\frac{t \\cdot P}{p} \\rceil $$

---

#### Nên chọn EPV/EPP bao nhiêu theo thông lệ?
Thông lệ hay dùng:
*   **10 EPV/EPP**: ngưỡng kinh điển từ các mô phỏng cổ điển. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/8970487/))
*   **15–20 EPV/EPP**: bảo thủ hơn, phù hợp khi tỷ lệ biến cố thấp, nhiều tham số, hoặc có spline/phi tuyến. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29966490/))

---

#### Tài liệu tham khảo quan trọng
1. Peduzzi P, et al. *A simulation study of the number of events per variable in logistic regression analysis.* **J Clin Epidemiol**. 1996. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/8970487/))
2. Vittinghoff E, McCulloch CE. *Relaxing the rule of ten events per variable in logistic and Cox regression.* **Am J Epidemiol**. 2007. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/17182981/))
3. van Smeden M, et al. *Sample size for binary logistic prediction models: Beyond events per variable criteria.* **Stat Methods Med Res**. 2019. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29966490/))
4. Riley RD, et al. *Minimum sample size for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* **Stat Med**. 2019. ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30357870/))
""")

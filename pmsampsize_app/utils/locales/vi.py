VI = {
        "title": "Prognostic Research Sample Size Tool",
        "sidebar_title": "Cấu hình",
        "language": "Ngôn ngữ / Language",
        "mode": "Chọn Phương pháp",
        "mode_riley": "Phương pháp 1: Riley et al. (Công thức)",
        "mode_bayes": "Phương pháp 2: Bayesian Assurance (Mô phỏng)",
        "mode_single": "Kịch bản đơn (Single)",
        "mode_batch": "Phân tích độ nhạy (Nhiều giá trị)",
        "method1_tab": "Phương pháp 1 (Riley)",
        "method2_tab": "Phương pháp 2 (Bayesian)",
        "nav_title": "Điều hướng",
        "nav_readme": "Tài liệu Chi tiết (README)",
        "nav_intro": "Giới thiệu & Công thức",
        "nav_calc": "Công cụ tính toán",
        "intro_heading": "Giới thiệu",
        "intro_text": "Ứng dụng hỗ trợ ước tính cỡ mẫu tối thiểu cho mô hình dự báo lâm sàng (biến nhị phân).",
        "formula_heading": "Cơ sở Toán học (Phương pháp 1)",
        "formula_intro": "Phương pháp 1 dùng công thức giải tích (Riley), Phương pháp 2 dùng mô phỏng Bayesian MCMC.",
        "sens_guide_title": "💡 Hướng dẫn nhập Phân tích Độ nhạy",
        "sens_guide_text": """
        - **Khoảng giá trị**: Nhập `min-max` (VD: `0.05-0.10`).
        - **Danh sách giá trị**: Nhập dấu phẩy (VD: `0.05, 0.10, 0.15`).
        """,
        "detail_view": "Xem chi tiết",
        "footer_refs": "Tài liệu tham khảo: Riley et al. (2018, 2020), BayesAssurance.",
        "calc_btn": "Tính toán",
        "results": "Kết quả",
        "sanity": "Kiểm tra nhanh (EPV)",
        "download_csv": "Tải xuống CSV",
        "download_report": "Tải Báo cáo Đầy đủ",
        "error_p": "Tỷ lệ phải từ 0 đến 1.",
        "error_auc": "AUC phải từ 0.5 đến 1.",
        "error_parse": "Lỗi nhập liệu.",
        
        # Riley specific
        "riley_inputs": "Tham số đầu vào (Riley)",
        "prevalence": "Tỷ lệ biến cố (Prevalence)",
        "prevalence_help": "Tỷ lệ người có biến cố (0 < p < 1).",
        "parameters": "Số tham số dự báo (df)",
        "parameters_help": "Tổng bậc tự do của các biến (trừ intercept).",
        "shrinkage": "Hệ số co trượt (Shrinkage)",
        "shrinkage_help": "Hệ số S mong muốn (mặc định 0.9).",
        "perf_measure": "Hiệu năng dự kiến",
        "perf_auc": "AUC (C-statistic)",
        "perf_r2": "Cox-Snell R-squared",
        "perf_cons": "Thận trọng (Conservative)",
        
        # Bayesian specific
        "bayes_inputs": "Cài đặt Mô phỏng (Bayesian Assurance)",
        "dgm_settings": "Cơ chế Sinh Dữ liệu (DGM)",
        "sim_settings": "Cài đặt Mô phỏng & MCMC",
        "eval_settings": "Tiêu chuẩn Đánh giá",
        "n_candidates": "Các mức Cỡ mẫu thử nghiệm (cách nhau bởi dấu phẩy)",
        "n_candidates_help": "Danh sách N muốn kiểm tra, VD: 500, 1000, 1500.",
        "correlation": "Hệ số tương quan (rho)",
        "n_sims": "Số lần mô phỏng cho mỗi N",
        "assurance_threshold": "Ngưỡng Assurance (Xác suất đạt yêu cầu)",
        "run_simulation": "Chạy Mô phỏng",
        "simulation_running": "Đang chạy mô phỏng... Vui lòng đợi.",
        "assurance_result": "Phân tích Assurance",

        # Method 6 (Dev Sim)
        "mode_dev_sim": "Phương pháp 6: Mô phỏng Phát triển (Freq)",
        "method6_tab": "PP 6 (Mô phỏng)",
        "dev_sim_intro": "Tính cỡ mẫu phát triển mô hình dựa trên mô phỏng (theo phương pháp `samplesizedev`).",
        "dev_mode_simple": "Chế độ A: Đơn giản (theo AUC)",
        "dev_mode_custom": "Chế độ B: DGM Tùy chỉnh",
        "target_auc": "AUC Mục tiêu (C-statistic trung bình)",
        "target_auc_help": "Thuật toán sẽ tự tìm hệ số Beta để đạt AUC này.",
        "criteria_settings": "Tiêu chí Đạt (Pass/Fail)",
        "crit_slope_mean": "Calibration Slope TB >= 0.9",
        "crit_slope_ci": "Pr(0.9 <= Slope <= 1.1) >= 80%",
        "crit_auc": "AUC TB >= Mục tiêu",
        "audit_trail": "RNG Audit Trail (JSON)",
        "future_methods": "Sắp ra mắt...",

        # Quick Methods
        "method_quick_tab": "A. Nhanh / Cơ bản",
        "quick_mode_epv": "A1: Quy tắc EPV / EPP (Kinh nghiệm)",
        "quick_mode_risk": "A2: Ước lượng Tỷ lệ nền (Độ rộng CI)",
        "target_epv": "Số biến cố trên tham số mục tiêu (EPP)",
        "target_epv_help": "Giá trị thường dùng: 10, 15, 20. EPP tốt hơn EPV.",
        "epv_warning_title": "⚠️ Cảnh báo Quan trọng",
        "epv_warning_text": "EPV/EPP chỉ là quy tắc kinh nghiệm thô. Nó KHÔNG đảm bảo độ chính xác, phân biệt hay ngăn ngừa overfitting. Rất nhạy cảm với việc chọn biến và đa cộng tuyến.",
        "ci_level": "Độ tin cậy (Confidence Level)",
        "ci_half_width": "Bán kính CI mong muốn (Sai số biên)",
        "ci_method": "Phương pháp CI",
        "ci_method_wilson": "Wilson Score (Khuyên dùng)",
        "ci_method_wald": "Wald (Đơn giản)",
        "ci_method_cp": "Clopper-Pearson (Thận trọng)",
        "risk_help": "Tính N để ước lượng tỷ lệ p với độ chính xác nhất định. KHÔNG đảm bảo hiệu năng mô hình dự báo.",
        
        # Power Methods (B)
        "title_b3": "B3: Logistic Power (Hsieh)",
        "title_b4": "B4: Cox Power (Schoenfeld)",
        "interpretation": "Giải thích kết quả",
        
        # Validations (D)
        "title_d8": "D8: AUC Precision (Hanley-McNeil)",
        "d8_desc": "Calculate sample size for estimating AUC with desired precision (CI width).",
        "auc_expected": "AUC dự kiến (C-statistic)",
        "formulas_header": "📚 Công thức & Chi tiết kỹ thuật",
        "d8_assumptions": "**Giả định**: Sử dụng xấp xỉ phương sai Hanley & McNeil (1982). Giả định phân phối chuẩn đối xứng cho AUC. Tối ưu hóa số học để tìm N.",
        "d8_mode_n_to_width": "Tính độ rộng CI từ N",
        "d8_mode_width_to_n": "Tính N từ độ rộng CI",
        "d8_opt_settings": "Cài đặt Tối ưu hóa Nâng cao",
        "d8_practical_rounding": "Hiển thị làm tròn số nguyên (Thực tế)",
        "d8_n_input": "Cỡ mẫu (N)",
        "d8_width_input": "Độ rộng CI (Tổng)",
        "d8_opt_bound": "Cận trên tìm kiếm (Upper Limit)",
        "d8_opt_tol": "Dung sai (Tolerance)",
        
        # D9
        "title_d9": "D9: Thẩm định ngoài (Tailored)",
        "common_inputs": "Tham số chung",
        
        # UI Basics
        "intro_heading": "Chào mừng đến với Prognostic Research Sample Size Tool",
        "search_placeholder": "Tìm phương pháp...",
        "settings": "Cài đặt",

        # Footer
        "footer_copyright": "© 2026 Prognostic Research Sample Size Tool. Dành cho nghiên cứu/học thuật. Không bán thương mại.",
        "footer_author": "Tác giả & Bảo trì: Minh Nguyen (minhnt@ump.edu.vn)",
        "footer_disclaimer": "Miễn trừ trách nhiệm: Không đảm bảo tính ứng dụng lâm sàng; người dùng tự chịu trách nhiệm kiểm định.",

        "intro_complete_md": """
### Chào mừng

Ứng dụng này giúp các nhà lâm sàng và nhà nghiên cứu tính toán cỡ mẫu tối thiểu cho nghiên cứu tiên lượng, bao gồm:
* Nghiên cứu yếu tố tiên lượng (power để phát hiện liên quan),
* Xây dựng mô hình dự báo lâm sàng (prediction model development), và
* Thẩm định/ngoại kiểm & cập nhật mô hình (validation/updating).

Ứng dụng phù hợp cho kết cục nhị phân (có/không biến cố) và một số mô-đun cho kết cục thời gian sống (Cox PH).

Mã nguồn (tải về): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)
hoặc [https://github.com/nguyenminh2301/pmsample.git](https://github.com/nguyenminh2301/pmsample.git)

### Hướng dẫn nhanh cho người mới

#### 1. Xác định mục tiêu nghiên cứu
* Bạn muốn kiểm định một yếu tố tiên lượng (liên quan OR/HR)?
* Bạn muốn xây dựng mô hình dự báo?
* Bạn muốn ngoại kiểm mô hình có sẵn ở quần thể mới?

#### 2. Ước tính tỷ lệ biến cố $p$ (hoặc tỷ lệ biến cố tích lũy cho sống còn)
* Ưu tiên lấy từ dữ liệu bệnh viện (best).
* Nếu chưa chắc, nhập khoảng giá trị và chạy độ nhạy.

#### 3. Đếm đúng độ phức tạp mô hình (tham số/df)
Cần dùng số tham số (df), không chỉ "số biến". Quy tắc cơ bản:
* Biến nhị phân: 1 df
* Biến phân loại $L$ mức: $L-1$ df
* Spline RCS $K$ nút: $K-1$ df
* Tương tác: $df(A \\times B) = df(A) \\cdot df(B)$

#### 4. Chọn phương pháp phù hợp
* **"Quick tools"** chỉ để kiểm tra sơ bộ.
* Nếu xây dựng mô hình dự báo: ưu tiên **Riley / mô phỏng / assurance**.

---

### Khi nào nên dùng (và khi nào không nên dùng)

**Nên dùng khi:**
* Lập kế hoạch đoàn hệ hồi cứu/tiến cứu trong tiên lượng/dự báo
* Xây dựng/ngoại kiểm mô hình dự báo nguy cơ
* Cần ước tính cỡ mẫu theo độ chính xác (độ rộng KTC) cho tỷ lệ hoặc AUC
* Thiết kế ngoại kiểm với mục tiêu calibration + discrimination

**Không nên dùng như công cụ chính khi:**
* Thiết kế thử nghiệm ngẫu nhiên (RCT) (cần phương pháp cỡ mẫu riêng cho RCT)
* Nghiên cứu độ chính xác chẩn đoán (Se/Sp) không gắn với mô hình dự báo
* Mong muốn "một con số đúng tuyệt đối": cỡ mẫu phụ thuộc giả định và cần phân tích độ nhạy

---

### Danh mục phương pháp (tóm tắt)

#### A. Quick / Basic (nhanh, xấp xỉ)

**A1 — Quy tắc kinh nghiệm (EPV/EPP) (heuristic)**
* **Dùng khi:** cần kiểm tra sơ bộ "số biến cố có đủ tương đối không" theo độ phức tạp mô hình.
* **Không dùng khi:** có spline/tương tác/chọn biến/biến cố hiếm—EPV/EPP không đảm bảo calibration hoặc ít optimism.
* **Đầu vào:** tỷ lệ biến cố $p$, số tham số $P$ (df), EPP mục tiêu (10/15/20)
* **Đầu ra:** $E=t \\cdot P$, $N=\\lceil E/p \\rceil$
* **Mạnh:** rất đơn giản, nhanh
* **Yếu:** dễ gây lạc quan, không dựa trên hiệu năng

**A2 — Độ chính xác nguy cơ nền (KTC cho tỷ lệ)**
* **Dùng khi:** mục tiêu là ước tính tỷ lệ biến cố $p$ với KTC đủ hẹp (±d).
* **Không dùng khi:** muốn đảm bảo hiệu năng mô hình dự báo.
* **Đầu vào:** $p$, phương pháp KTC (Wilson khuyến nghị), mức tin cậy, nửa độ rộng $d$
* **Đầu ra:** $N$ tối thiểu đạt nửa độ rộng KTC $\\le d$
* **Mạnh:** minh bạch, trực tiếp theo mục tiêu độ chính xác
* **Yếu:** chỉ cho $p$, không nói về AUC/slope

#### B. Prognostic factor (power) (tập trung liên quan, không phải sizing cho mô hình dự báo)

**B3 — Logistic OR Power (Hsieh)**
* **Dùng khi:** cần power để phát hiện OR mục tiêu của một yếu tố tiên lượng trong logistic regression.
* **Không dùng khi:** mục tiêu chính là xây dựng mô hình dự báo.
* **Đầu vào:** $p_0$, OR mục tiêu, alpha, power, tỷ lệ phơi nhiễm (nếu nhị phân) hoặc SD (nếu liên tục), tùy chọn $R^2$ với đồng biến
* **Đầu ra:** $N$ (và số biến cố kỳ vọng)
* **Mạnh:** khung power kinh điển
* **Yếu:** không nhắm calibration/discrimination

**B4 — Cox HR Power (Schoenfeld)**
* **Dùng khi:** kết cục sống còn, cần phát hiện HR mục tiêu theo Cox PH.
* **Không dùng khi:** khó ước lượng tỷ lệ biến cố theo dõi hoặc PH không hợp lý.
* **Đầu vào:** HR, alpha, power, tỷ lệ phân bổ (nhị phân) hoặc SD (liên tục), tỷ lệ biến cố kỳ vọng trong thời gian theo dõi
* **Đầu ra:** số biến cố cần thiết → suy ra $N$
* **Mạnh:** phổ biến, trực quan theo số biến cố
* **Yếu:** phụ thuộc mạnh vào giả định theo dõi/censoring

#### C. Prediction model development (khuyến nghị cho xây dựng mô hình dự báo)

**C5 — Riley et al. (phân tích; pmsampsize-like)**
* **Dùng khi:** phát triển mô hình dự báo, cần hạn chế overfitting và bảo đảm độ chính xác.
* **Không dùng khi:** không có giả định hợp lý về $p$ và hiệu năng dự kiến (AUC hoặc $R^2$); khi đó dùng độ nhạy/mô phỏng.
* **Đầu vào:** $p$, $P$ (df), shrinkage mục tiêu (ví dụ 0,90), hiệu năng dự kiến (AUC hoặc Cox–Snell $R^2$)
* **Đầu ra:** $N$ tối thiểu thỏa các tiêu chí (overfitting + precision)
* **Mạnh:** có cơ sở, dựa trên hiệu năng
* **Yếu:** phụ thuộc giả định; cần đếm df chuẩn

**C6 — Development Simulation (Frequentist; samplesizedev/custom DGM)**
* **Dùng khi:** muốn mô phỏng theo đúng cách bạn dự kiến xây dựng mô hình (phi tuyến/tương tác).
* **Không dùng khi:** không mô tả được DGM hợp lý hoặc cần kết quả tức thì.
* **Đầu vào:** danh sách $N$, giả định DGM, tiêu chí hiệu năng, số mô phỏng, seed
* **Đầu ra:** $N$ nhỏ nhất đạt tiêu chí
* **Mạnh:** linh hoạt, phù hợp mô hình phức tạp
* **Yếu:** tốn tính toán, nhạy giả định

**C7 — Bayesian Assurance (MCMC)**
* **Dùng khi:** mô hình cuối cùng ước lượng bằng Bayes/MCMC và muốn sizing theo assurance.
* **Không dùng khi:** không xác định được prior hợp lý hoặc hạn chế compute.
* **Đầu vào:** DGM, prior, $N$, tiêu chí assurance, cài đặt MCMC
* **Đầu ra:** $N$ nhỏ nhất đạt assurance
* **Mạnh:** nhất quán với Bayes
* **Yếu:** compute cao, cần prior

#### D. Validation / Updating (cho mô hình có sẵn)

**D8 — Độ chính xác AUC (Hanley–McNeil / presize)**
* **Dùng khi:** mục tiêu ngoại kiểm là KTC AUC đủ hẹp.
* **Không dùng khi:** calibration là trọng tâm.
* **Đầu vào:** AUC kỳ vọng, $p$ hoặc tỷ lệ case-control, mức tin cậy, độ rộng KTC mục tiêu
* **Đầu ra:** $N$ tối thiểu cho độ chính xác AUC
* **Mạnh:** nhanh, dễ dùng
* **Yếu:** chỉ AUC, xấp xỉ

**D9 — External Validation (Tailored; pmvalsampsize / sampsizeval)**
* **Dùng khi:** sizing ngoại kiểm theo nhiều thước đo (calibration + discrimination), thường cần giả định phân bố LP.
* **Không dùng khi:** không biện minh được giả định LP/case-mix.
* **Đầu vào:** $p$, AUC kỳ vọng, mục tiêu slope/CITL, độ rộng KTC/SE, giả định phân bố LP
* **Đầu ra:** $N$ khuyến nghị
* **Mạnh:** "tailored", chú trọng calibration
* **Yếu:** phức tạp, phụ thuộc giả định

**D10 — External Validation (Simulation; LP-based)**
* **Dùng khi:** có thể mô tả/ước lượng phân bố LP ở quần thể ngoại kiểm và muốn mô phỏng độ chính xác.
* **Không dùng khi:** không ước lượng được LP distribution.
* **Đầu vào:** phân bố LP, tham số miscalibration, mục tiêu độ rộng KTC, số mô phỏng, seed
* **Đầu ra:** $N$ tối thiểu theo mô phỏng
* **Mạnh:** linh hoạt
* **Yếu:** tốn compute, nhạy giả định

**D11 — Updating / Recalibration (intercept/slope)**
* **Dùng khi:** cần cập nhật intercept/slope khi triển khai ở bệnh viện mới.
* **Không dùng khi:** phát triển mô hình mới hoàn toàn.
* **Đầu vào:** kiểu cập nhật, $p$, mục tiêu độ chính xác
* **Đầu ra:** $N$ đủ ổn định cho cập nhật
* **Mạnh:** thực dụng khi triển khai
* **Yếu:** phụ thuộc case-mix và transportability

---

#### Disclaimer

No clinical warranty; users are responsible for validation and interpretation. Always document assumptions and run sensitivity analyses.

#### Contact

Author & Maintenance: Minh Nguyen (minhnt@ump.edu.vn)
""",

        "a2_content_md": """
### Nguyên tắc

Chức năng này tính **cỡ mẫu tối thiểu (n)** để ước tính **tỷ lệ biến cố / nguy cơ nền** (p) (prevalence) với **độ chính xác mong muốn**, biểu diễn bằng **nửa độ rộng khoảng tin cậy (KTC)** (margin of error).

Ứng dụng:
* mô tả tỷ lệ biến cố trong đoàn hệ với KTC đủ hẹp,
* lập kế hoạch khả thi và báo cáo dịch tễ,
* hỗ trợ các phân tích liên quan calibration.

**Hạn chế:** Phương pháp này **không đảm bảo** hiệu năng mô hình dự báo (AUC, calibration slope, optimism). Nó chỉ đảm bảo độ chính xác khi **ước tính (p)**.

---

### Chú giải các giá trị đầu vào

1. **Tỷ lệ biến cố** (p)
   Tỷ lệ kết cục xảy ra dự kiến trong quần thể nghiên cứu (ví dụ 0,10).
   * Nếu chưa rõ, nên nhập một **khoảng giá trị** và chạy phân tích độ nhạy.
   * Nếu cần “bảo thủ” cho bài toán ước tính tỷ lệ, dùng $p=0.50$ (phương sai lớn nhất).

2. **Nửa độ rộng KTC mục tiêu** (d)
   Mục tiêu sao cho KTC xấp xỉ: $p \pm d$
   Ví dụ: $d = 0.01, 0.02, 0.03$ tương ứng ±1%, ±2%, ±3%.

3. **Mức tin cậy** (1-$\\alpha$)
   Thường dùng 0,95 hoặc 0,99.

4. **Phương pháp tính KTC**
* **Wilson score (khuyến nghị):** độ bao phủ tốt hơn Wald, nhất là khi (p) gần 0 hoặc 1 hoặc cỡ mẫu vừa/nhỏ.
* **Wald (xấp xỉ chuẩn):** công thức đóng đơn giản nhưng có thể kém chính xác khi (n) nhỏ hoặc (p) cực trị.
* **Clopper–Pearson (exact):** bảo thủ (KTC thường rộng hơn → cần (n) lớn hơn).

---

### Cách tính (công thức và ý tưởng)

Giả sử $X \sim \\text{Binomial}(n,p)$, $\hat p = X/n$. Mục tiêu là tìm (n) nhỏ nhất sao cho:
$$ \\frac{\\text{Upper}(n) - \\text{Lower}(n)}{2} \le d $$

#### A) Wald (xấp xỉ)
$$ n \\approx \\frac{z^2 p(1-p)}{d^2} $$

#### B) Wilson score (khuyến nghị)
Sử dụng công thức khoảng tin cậy Wilson.

#### C) Clopper–Pearson (exact)
Dùng phân vị Beta. Đây là phương pháp bảo thủ.

---

### Nên chọn giá trị bao nhiêu theo thông lệ?

* **Mức tin cậy:** 95% là chuẩn.
* **Nửa độ rộng (d):** ±0,01 đến ±0,03 (1%–3%) là mức hay gặp.
* **Phương pháp:** Wilson là lựa chọn mặc định hợp lý.

### Tài liệu tham khảo quan trọng
1. **Wilson EB.** Probable inference... *JASA.* 1927.
2. **Newcombe RG.** Two-sided confidence intervals... *Stat Med.* 1998.
""",

        "b3_content_md": """
### Mục đích (phương pháp này là gì)

Chức năng này ước tính **cỡ mẫu tối thiểu** để phát hiện mối liên quan giữa biến dự báo (X) và **kết cục nhị phân** (Y) bằng **hồi quy logistic**, với **OR mục tiêu**, **($\\alpha$) hai phía**, và **power** đã chọn.

Đây là phương pháp **power cho nghiên cứu yếu tố tiên lượng / kiểm định liên quan** (kiểm định hệ số hồi quy), **không phải** phương pháp đảm bảo hiệu năng của **mô hình dự báo**. Nó **không đảm bảo** calibration/discrimination của mô hình đa biến.

---

### Khi nào nên dùng

Dùng B3 khi:

* Bạn cần power để phát hiện **OR có ý nghĩa lâm sàng** cho **một biến** (nhị phân hoặc liên tục) trong logistic regression.
* Mục tiêu là **kiểm định giả thuyết** (biến có liên quan kết cục hay không), không phải xây dựng mô hình dự báo nguy cơ.

### Khi nào không nên dùng

Không dùng B3 làm phương pháp chính khi:

* Mục tiêu là **xây dựng mô hình dự báo** (nên dùng Riley/pmsampsize hoặc mô phỏng/assurance).
* Bạn dự định **chọn biến theo dữ liệu**, dùng nhiều spline/tương tác, hoặc tuning mô hình phức tạp (power cho 1 hệ số không còn là mục tiêu phù hợp).
* Dữ liệu có **phụ thuộc/cụm** (đa trung tâm/khoa/phòng) mà chưa tính design effect.
* Thiết kế **case–control** với số ca/chứng cố định (giá trị ($p_0$) không phản ánh nguy cơ nền quần thể).

---

## Mô hình và tham số

Mô hình logistic:
$$
\\text{logit}{P(Y=1\\mid X)}=\\beta_0+\\beta_1 X
$$

* Nếu ($X$) nhị phân 0/1:
  $$
  \\mathrm{OR}=\\exp(\\beta_1)
  $$
* Nếu ($X$) liên tục: OR phải gắn với một mức thay đổi của ($X$) (thông dụng nhất: **tăng 1 SD**).

Kiểm định:
$$
H_0:\\beta_1=0 \\quad \\text{vs}\\quad H_1:\\beta_1\\neq 0
$$

---

## Chú giải các đầu vào

1. **Alpha (2 phía)** ($\\alpha$): thường 0,05; 0,01 nếu nghiêm ngặt hơn.
2. **Power** ($1-\\beta$): thường 0,80; 0,90 nếu cần thận trọng.
3. **Tỷ lệ biến cố nền** ($p_0$)

   * Với ($X$) nhị phân: ($p_0=P(Y=1\\mid X=0)$).
   * Với ($X$) liên tục: ($p_0$) thường hiểu là tỷ lệ biến cố tại **giá trị trung bình** của ($X$) (sau khi center).
4. **OR mục tiêu**: mức OR nhỏ nhất có ý nghĩa lâm sàng.
5. **Loại biến dự báo**

   * Nhị phân: cần ($q=P(X=1)$).
   * Liên tục: cần OR cho **tăng 1 SD** (hoặc phải quy đổi từ OR theo 1 đơn vị).
6. **($R^2$) với các đồng biến khác**

   * ($R^2$) là mức độ ($X$) được giải thích bởi các đồng biến khác (khi hồi quy ($X$) theo các biến khác).
   * ($R^2$) càng lớn → cần cỡ mẫu càng lớn (vì thông tin “độc lập” của ($X$) giảm).

---

# Cách tính (công thức)

## Bước 1 — Quy đổi OR và ($p_0$) sang ($p_1$) (khi ($X$) nhị phân)

$$
\\text{odds}_0=\\frac{p_0}{1-p_0},\\quad \\text{odds}_1=\\mathrm{OR}\\cdot \\text{odds}_0,\\quad
p_1=\\frac{\\text{odds}_1}{1+\\text{odds}_1}
$$

Tỷ lệ biến cố chung:
$$
p=(1-q)p_0+q p_1
$$

## Bước 2 — Z-score

$$
z_{\\alpha}=z_{1-\\alpha/2}, \\qquad z_{\\beta}=z_{1-\\beta}=z_{\\text{power}}
$$

## A) Cỡ mẫu với biến dự báo nhị phân

$$
n_0=
\\frac{
\\left[
z_{\\alpha}\\sqrt{\\frac{p(1-p)}{q(1-q)}}
+
z_{\\beta}\\sqrt{\\frac{p_1(1-p_1)}{q}+\\frac{p_0(1-p_0)}{1-q}}
\\right]^2
}
{(p_1-p_0)^2}
$$

### Hiệu chỉnh khi có nhiều đồng biến (tương quan với biến khác)

$$
n=\\frac{n_0}{1-R^2}
$$

### Số biến cố kỳ vọng

$$
E \\approx n\\cdot p
$$

---

## B) Cỡ mẫu với biến dự báo liên tục

Giả định OR được định nghĩa cho **tăng 1 SD** của ($X$) (ký hiệu ($\\mathrm{OR}_{SD}$)), và ($p_0$) là tỷ lệ biến cố tại trung bình của ($X$):

$$
n_0=\\frac{(z_{\\alpha}+z_{\\beta})^2}{p_0(1-p_0) [\\log(\\mathrm{OR}_{SD})]^2}
$$

Nếu OR nhập theo **tăng 1 đơn vị** là ($\\mathrm{OR}_{unit}$), và SD của ($X$) là ($\\sigma_X$), thì:
$$
\\log(\\mathrm{OR}_{SD})=\\log(\\mathrm{OR}_{unit})\\cdot \\sigma_X
$$

Sau đó hiệu chỉnh tương quan đồng biến:
$$
n=\\frac{n_0}{1-R^2}
$$

---

## Nên chọn giá trị bao nhiêu theo thông lệ?

* **($\\alpha$)**: 0,05 (hai phía) là phổ biến; giảm ($\\alpha$) nếu có nhiều kiểm định.
* **Power**: 0,80 (thường dùng); 0,90 (thận trọng hơn).
* **OR mục tiêu**: chọn OR nhỏ nhất có ý nghĩa lâm sàng (thường 1,2–2,0 tùy bối cảnh).
* **($p_0$)**: ưu tiên dữ liệu bệnh viện; nếu chưa có, dùng y văn và chạy độ nhạy.
* **($q$)**: lấy từ tỷ lệ phơi nhiễm thực tế; ($q$) gần 0,5 thường cho cỡ mẫu nhỏ hơn; ($q$) rất thấp/cao làm tăng ($n$).
* **($R^2$)**: nếu chưa chắc, chạy độ nhạy (0; 0,1; 0,25; 0,5).
* **Biến liên tục**: nên chuẩn hóa ($X$) (mean 0, SD 1) để OR theo 1 SD dễ hiểu.

---

## Tài liệu tham khảo

1. Hsieh FY, Bloch DA, Larsen MD. *A simple method of sample size calculation for linear and logistic regression.* Statistics in Medicine. 1998;17(14):1623–1634.
2. Hsieh FY. *Sample size tables for logistic regression.* Statistics in Medicine. 1989;8(7):795–802.
3. Whittemore AS. *Sample size for logistic regression with small response probability.* Journal of the American Statistical Association. 1981;76:27–32.
""",
        "c5_content_md": """
### C5: Riley et al. (Phân tích)

### Phương pháp này là gì?

C5 triển khai các **tiêu chí cỡ mẫu tối thiểu của Riley và cộng sự** cho **xây dựng mô hình dự báo đa biến** với **kết cục nhị phân** (hồi quy logistic). Mục tiêu là bảo đảm cỡ mẫu đủ để:

1. **Hạn chế overfitting** (nhắm tới hệ số co rút toàn cục / calibration slope mục tiêu),
2. Bảo đảm **độ chính xác** của hiệu năng mô hình (giới hạn mức “lạc quan” của $R^2$), và
3. Ước tính **nguy cơ nền/tỷ lệ biến cố chung** (intercept) đủ chính xác.

Đây là phương pháp cho **phát triển mô hình** (không phải ngoại kiểm). Đặc biệt phù hợp khi bạn xây dựng mô hình logistic với **danh sách biến và cách mã hóa được xác định trước**, và muốn thay thế quy tắc EPV đơn giản bằng phương pháp có cơ sở hơn.

---

### Khi nào nên dùng

Dùng C5 khi:

* Bạn đang **xây dựng** mô hình dự báo cho **kết cục nhị phân**.
* Bạn có thể ước lượng (dù gần đúng) **tỷ lệ biến cố** và **hiệu năng dự kiến** (Cox–Snell $R^2$ hoặc AUC).
* Bạn muốn nhắm tới **ít overfitting** (ví dụ $S \\ge 0{,}90$) và độ chính xác hợp lý.

### Khi nào không nên dùng (hoặc cần thận trọng)

Không nên chỉ dựa vào C5 khi:

* Bạn dự định **chọn biến theo dữ liệu**, dùng nhiều tương tác/spline/tinh chỉnh phức tạp mà chưa quy đổi đúng **df hiệu dụng**.
* Dữ liệu có **cụm/đa trung tâm** mà chưa tính design effect.
* Phương pháp mô hình hóa khác xa logistic chuẩn (ML phức tạp) mà không có cách quy đổi độ phức tạp sang **df hiệu dụng**; khi đó nên cân nhắc mô phỏng.
* Bạn không thể biện minh bất kỳ giả định nào về AUC/$R^2$; khi đó nên chạy độ nhạy rộng và/hoặc dùng mô phỏng.

---

## Chú giải các đầu vào

1. **Tỷ lệ biến cố** (p)
   Tỷ lệ (Y=1) dự kiến trong bộ dữ liệu phát triển mô hình.

2. **Số tham số mô hình (df)** (P)
   Tổng bậc tự do của tất cả biến dự báo **không tính intercept**.
   Bao gồm: dummy của biến phân loại, basis spline, tương tác, và mọi biến đổi tạo thêm hệ số.

3. **Hiệu năng dự kiến** (chọn một)

* **Cox–Snell ($R^2_{CS}$)**: ưu tiên nếu có từ nghiên cứu liên quan (lý tưởng là đã hiệu chỉnh lạc quan).
* **AUC (C-statistic)**: nếu không có $R^2_{CS}$, có thể xấp xỉ $R^2_{CS}$ từ AUC và ($p$) theo phương pháp đã công bố.
* **Bảo thủ (15% của $R^2$ tối đa)**: dùng khi không có AUC/$R^2$; chỉ nên dùng cho ước tính sơ bộ và luôn chạy phân tích độ nhạy.

4. **Mục tiêu shrinkage toàn cục** (S)
   Thước đo kiểm soát overfitting (thường diễn giải gần với calibration slope kỳ vọng sau nội kiểm).

* Mặc định hay dùng: $S=0{,}90$ (tương đương cần shrink ~10%).
* Bảo thủ hơn: $S=0{,}95$.

---

## Khái niệm và công thức

### Cox–Snell ($R^2$) và giá trị tối đa

$$
R^2_{CS} = 1-\\exp!\\left(\\frac{2}{n}(\\ell_0-\\ell_1)\\right),
$$
trong đó $\\ell_0$ là log-likelihood mô hình chỉ có intercept và $\\ell_1$ là log-likelihood mô hình đầy đủ.

Với kết cục nhị phân, $R^2_{CS}$ không đạt 1. Giá trị tối đa phụ thuộc ($p$):
$$
\\ell_0 = n\\Big[p\\ln(p) + (1-p)\\ln(1-p)\\Big],
$$
$$
R^2_{CS,\\max}=1-\\exp!\\left(\\frac{2\\ell_0}{n}\\right)
=1-\\exp!\\Big(2[p\\ln(p) + (1-p)\\ln(1-p)]\\Big).
$$

Nagelkerke ($R^2$):
$$
R^2_{Nag}=\\frac{R^2_{CS}}{R^2_{CS,\\max}}.
$$

---

## Ba tiêu chí Riley (kết cục nhị phân)

### Tiêu chí 1 — Giới hạn overfitting bằng shrinkage mục tiêu (S)

$$
n_1=\\left\\lceil
\\frac{P}{(S-1),\\ln!\\left(1-\\frac{R^2_{CS}}{S}\\right)}
\\right\\rceil.
$$

### Tiêu chí 2 — Giới hạn mức lạc quan của ($R^2$) (mặc định 0,05)

Tiêu chí này nhắm tới chênh lệch tuyệt đối (mặc định $\\delta=0{,}05$) giữa ($R^2$) biểu kiến và ($R^2$) hiệu chỉnh trên thang **Nagelkerke**. Shrinkage tương ứng:
$$
S_{\\delta}=\\frac{R^2_{CS}}{R^2_{CS}+\\delta,R^2_{CS,\\max}}.
$$
Sau đó:
$$
n_2=\\left\\lceil
\\frac{P}{(S_{\\delta}-1),\\ln!\\left(1-\\frac{R^2_{CS}}{S_{\\delta}}\\right)}
\\right\\rceil.
$$

### Tiêu chí 3 — Ước tính chính xác nguy cơ nền (intercept)

Nhắm tới ước tính ($p$) trong khoảng ($\\pm d$) (mặc định $d=0{,}05$ ở mức 95%):
$$
n_3=\\left\\lceil
\\left(\\frac{z_{1-\\alpha/2}}{d}\\right)^2 p(1-p)
\\right\\rceil,
\\quad \\text{mặc định } z_{0.975}=1.96,; d=0.05.
$$

### Kết quả cuối cùng

$$
n_{\\min}=\\max(n_1,n_2,n_3),\\qquad
E = n_{\\min},p,\\qquad
EPP=\\frac{E}{P}.
$$

---

## Gợi ý chọn giá trị theo thông lệ

* **Shrinkage (S)**: thường chọn **0,90**; cân nhắc **0,95** nếu mô hình phức tạp hoặc muốn giảm overfitting mạnh hơn.
* **$\\delta=0{,}05$** (Tiêu chí 2): thường giữ mặc định.
* **Độ chính xác intercept (d=0{,}05)**: mặc định tương ứng ước tính nguy cơ nền trong ±5%. Nếu cần chính xác hơn (d nhỏ hơn) thì cần (n) lớn hơn.
* **$R^2_{CS}$ dự kiến**:

  * Ưu tiên giá trị **đã hiệu chỉnh lạc quan** từ nghiên cứu phát triển tương tự, hoặc giá trị biểu kiến từ ngoại kiểm.
  * Nếu chỉ có AUC, dùng phương pháp xấp xỉ AUC→$R^2_{CS}$ theo bài báo hướng dẫn.
  * Nếu không có AUC/$R^2$, tùy chọn **15% của $R^2_{CS,\\max}$** chỉ nên dùng để ước tính sơ bộ và luôn chạy phân tích độ nhạy.

---

## Tài liệu tham khảo

1. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: PART II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
2. Riley RD, Ensor J, Snell KIE, et al. *Calculating the sample size required for developing a clinical prediction model.* BMJ. 2020.
3. Riley RD, Van Calster B, Collins GS. *A note on estimating the Cox–Snell ($R^2$) from a reported C statistic (AUROC) to inform sample size calculations for developing a prediction model with a binary outcome.* Statistics in Medicine. 2021.
4. Harrell FE Jr, Lee KL, Mark DB. *Multivariable prognostic models: issues in developing models, evaluating assumptions and adequacy, and measuring and reducing errors.* Statistics in Medicine. 1996.
""",
        "c6_content_md": """
## C6: Mô phỏng phát triển mô hình (Frequentist; DGM tùy biến) 

### Phương pháp này là gì?

C6 là phương pháp **ước tính cỡ mẫu bằng mô phỏng** cho **xây dựng mô hình dự báo** (kết cục nhị phân), theo triết lý gần với **samplesizedev** và các hướng dẫn mô phỏng trong prediction modeling.

Thay vì một công thức đóng, C6 trả lời câu hỏi:

> “Nếu lặp lại nhiều lần quá trình xây dựng mô hình trên dữ liệu cỡ mẫu (N), mô hình có đạt tiêu chí hiệu năng mong muốn trên dữ liệu mới với xác suất đủ cao không?”

Do đó C6 nhắm tới **hiệu năng kỳ vọng** (và/hoặc xác suất đạt hiệu năng chấp nhận được) dưới một **cơ chế sinh dữ liệu (DGM)** mô tả quần thể lâm sàng dự kiến.

---

## Khi nào nên dùng

Dùng C6 khi:

* Muốn “**mô phỏng đúng cách bạn sẽ làm**”, đặc biệt khi:

  * biến dự báo tương quan,
  * có spline/phi tuyến, tương tác,
  * tỷ lệ biến cố vừa/không chắc,
  * muốn tiêu chí dựa trên **calibration** và **discrimination**.
* Có thể mô tả DGM hợp lý dựa trên dữ liệu bệnh viện hoặc y văn.
* Chấp nhận chạy mô phỏng và cần phương pháp linh hoạt hơn công thức phân tích.

## Khi nào không nên dùng (hoặc cần thận trọng)

Không nên chỉ dựa vào C6 khi:

* Không biện minh được DGM (phân bố biến, tương quan, hiệu ứng).
* Hạn chế tài nguyên tính toán.
* Pipeline phát triển mô hình mang tính “data-adaptive” phức tạp (chọn biến/tuning) nhưng không mô phỏng đầy đủ pipeline đó.
* Quần thể đích khác biệt mạnh theo trung tâm/case-mix nhưng mô phỏng không phản ánh cụm/khác biệt.

---

# Quy trình mô phỏng (tổng quan)

### Bước 1 — Chọn DGM

$$
Y \mid X \sim \\text{Bernoulli}(\\pi), \\qquad
\\pi = \\text{logit}^{-1}(\\eta),
$$
$$
\\eta = \\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_j),
$$
trong đó (P) là **df**, còn (f_j(\\cdot)) là cách mã hóa (tuyến tính, spline, dummy…).

Chọn (\\beta_0) để đạt tỷ lệ biến cố mục tiêu (p):
$$
\\mathbb{E}[\\pi] = p.
$$
(Trong thực hành dùng root-finding dựa trên mô phỏng (X).)

### Bước 2 — Sinh dữ liệu phát triển

Với mỗi lần mô phỏng (r):

* Sinh (X^{(r)}) kích thước (N),
* Sinh (Y^{(r)}) theo Bernoulli ở trên.

### Bước 3 — Fit mô hình phát triển

$$
\\widehat{\\eta} = \\widehat{\\beta}*0 + \\sum*{j=1}^{P}\\widehat{\\beta}_j f_j(X_j).
$$
Nếu xảy ra separation/không hội tụ, thường dùng ridge-penalized fallback và báo cáo tỷ lệ xảy ra.

### Bước 4 — Đánh giá trên dữ liệu mới

Sinh tập test độc lập (thường (N_{\\text{test}}) lớn 5000–10000) và tính:

**(a) AUC**
$$
\\mathrm{AUC}=\\Pr(\\widehat{\\eta}_1 > \\widehat{\\eta}_0).
$$

**(b) Calibration slope**
Fit mô hình hiệu chỉnh:
$$
\\text{logit}(Y) = a + b \\cdot \\text{logit}(\\widehat{p})
$$
hoặc:
$$
\\text{logit}(Y) = a + b \\cdot \\widehat{\\eta}.
$$
Trong đó (b\\approx 1) là tốt; (b<1) thường gợi ý overfitting.

### Bước 5 — Tiêu chí đạt/không đạt và chọn (N)

Tóm tắt theo (R) lần mô phỏng:

$$
\\overline{b} = \\frac{1}{R}\\sum_{r=1}^R b^{(r)},
\\quad
\\widehat{\\Pr}(b \\in [L,U]) = \\frac{1}{R}\\sum_{r=1}^R \\mathbf{1}{b^{(r)}\\in[L,U]},
$$
$$
\\overline{\\mathrm{AUC}}=\\frac{1}{R}\\sum_{r=1}^R \\mathrm{AUC}^{(r)}.
$$

Một (N) đạt yêu cầu nếu thỏa tất cả tiêu chí đã chọn (ví dụ):

* (\\overline{b} \\ge 0.90)
* (\\widehat{\\Pr}(0.9 \\le b \\le 1.1) \\ge 0.80)
* (\\overline{\\mathrm{AUC}} \\ge \\mathrm{AUC}_{\\text{target}})

Chọn (N) nhỏ nhất đạt.

---

# Chú giải đầu vào (tìm ở đâu, nên chọn bao nhiêu)

### 1) Tỷ lệ biến cố (p)

**Lấy ở đâu:** số liệu bệnh viện/đoàn hệ gần nhất; nếu thiếu dùng y văn.
**Khoảng hay dùng khi lập kế hoạch:** 5%–15% (tùy bệnh).
**Khuyến nghị:** chạy độ nhạy theo khoảng plausible.

### 2) Số tham số (df) (P)

**Lấy ở đâu:** đặc tả mô hình dự kiến (bao gồm dummy, spline, tương tác).
**Thông lệ:** 10–30 df khá phổ biến; df càng lớn càng cần mẫu lớn.

### 3) AUC mục tiêu (Mode A)

**Lấy ở đâu:** mô hình tương tự đã công bố (ưu tiên ngoại kiểm), pilot data.
**Thông lệ:** 0,70–0,85 thường gặp; >0,90 thường hiếm và dễ lạc quan.

### 4) Danh sách (N) ứng viên

Chọn dải đủ rộng để thấy ngưỡng đạt/không đạt (ví dụ 1000–5000).

### 5) Số mô phỏng mỗi (N) (R)

* Demo: (R \\approx 200)
* Final: (R \\ge 1000)
  Sai số Monte Carlo cho xác suất đạt:
  $$
  \\mathrm{MCSE}=\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{R}}.
  $$

### 6) Tiêu chí Pass/Fail

* Mean calibration slope ≥ 0.9
* Pr(0.9 ≤ slope ≤ 1.1) ≥ 80%
* Mean AUC ≥ target

**Thông lệ:** slope 0,90–1,10 và ngưỡng xác suất 0,80 hay dùng cho planning; 0,90 nếu muốn chắc chắn hơn.

---

# Điểm mạnh và điểm yếu

**Điểm mạnh**

* Linh hoạt (tương quan, phi tuyến, tương tác).
* Nhắm trực tiếp hiệu năng trên dữ liệu mới, đặc biệt calibration.
* Dễ làm phân tích độ nhạy.

**Điểm yếu**

* Phụ thuộc mạnh vào giả định DGM.
* Tốn tài nguyên tính toán.
* Phải mô phỏng đúng pipeline dự định; nếu không dễ sai lệch.

---

## Tài liệu tham khảo

1. Pavlou M, Ambler G, Seaman SR, et al. *How to develop a more accurate risk prediction model when there are few events.* BMJ. 2015.
2. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
3. Pavlou M, et al. *Simulation-based sample size calculation for prediction model performance targets* (validation/development methodology). Statistics in Medicine. 2021.
4. Steyerberg EW. *Clinical Prediction Models: A Practical Approach to Development, Validation, and Updating.* 2nd ed. Springer. 2019.
""",
    "c7_content_md": """
## C7: Bayesian Assurance (MCMC) — Tiếng Việt

### Phương pháp này là gì?
**Bayesian assurance** là phương pháp lập kế hoạch cỡ mẫu bằng mô phỏng cho **xây dựng mô hình Bayes** (ở đây: hồi quy logistic Bayes cho kết cục nhị phân).  
Khác với “power” (frequentist), assurance nhắm tới **xác suất vô điều kiện** để nghiên cứu đạt **tiêu chí thành công** đã định trước (ví dụ: tiêu chí calibration, discrimination và/hoặc độ chính xác hậu nghiệm).

Nói đơn giản:
> “Nếu lặp lại toàn bộ nghiên cứu nhiều lần (sinh dữ liệu + fit Bayes bằng MCMC), xác suất mô hình đạt yêu cầu là bao nhiêu?”

---

### Khi nào nên dùng
Dùng C7 khi:
- Phân tích cuối cùng là **Bayes** và ước lượng bằng **MCMC**.
- Bạn muốn chọn cỡ mẫu sao cho đạt **xác suất thành công mục tiêu** (ví dụ ≥80% hoặc ≥90%).
- Bạn có thể đưa ra giả định hợp lý về:
  - tỷ lệ biến cố tại bệnh viện,
  - cấu trúc tương quan của biến dự báo,
  - hiệu ứng hợp lý (pilot/y văn),
  - prior cho các hệ số hồi quy.

### Khi nào không nên dùng (hoặc cần thận trọng)
Không nên chỉ dựa vào C7 khi:
- Không thể biện minh prior hoặc **cơ chế sinh dữ liệu (DGM)**.
- Hạn chế tài nguyên tính toán (MCMC tốn thời gian; nhạy với cài đặt).
- Pipeline thực tế có bước “data-adaptive” lớn (chọn biến/tuning) nhưng bạn **không mô phỏng đầy đủ** pipeline đó.
- Dữ liệu có cụm/đa trung tâm nhưng DGM bỏ qua clustering (dễ đánh giá thiếu cỡ mẫu).

---

## Mô hình và DGM

### Hồi quy logistic Bayes (mô hình phân tích)
\[
Y_i \sim \\text{Bernoulli}(\\pi_i), \\qquad
\\text{logit}(\\pi_i)=\\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_{ij})
\]
- \(P\) = số tham số/df (**không tính intercept**).
- \(f_j(\cdot)\): cách mã hóa biến (tuyến tính, dummy, spline, tương tác…).

**Ví dụ prior “weakly informative” hay dùng:**
\[
\\beta_j \sim \\mathcal{N}(0,\\sigma_\\beta^2),\\quad \\sigma_\\beta \\in [1, 2.5],
\\qquad \\beta_0 \sim \\mathcal{N}(0, 5^2)
\]
(Trong thực hành cần chạy độ nhạy theo prior hợp lý.)

### DGM cho biến dự báo (ví dụ equicorrelation)
Nếu app dùng một tham số tương quan \\(\\rho\\) (mọi cặp biến có cùng tương quan):
\[
\\mathrm{Corr}(X_j, X_k)=\\rho \\quad (j\\neq k),
\\qquad
\\Sigma_{jk}=
\\begin{cases}
1,& j=k\\\\
\\rho,& j\\neq k
\\end{cases}
\]
Sau đó sinh dữ liệu dự báo theo cơ chế tương quan (ví dụ Gaussian copula), rồi chuyển thành biến liên tục/nhị phân.

### Khớp tỷ lệ biến cố mục tiêu
Chọn intercept (hoặc hằng số hiệu chỉnh) để:
\[
\\mathbb{E}[\\pi_i]=p
\]
(thường giải bằng root-finding dựa trên mô phỏng \\(X\\).)

---

## “Assurance” là gì (công thức chính)
Gọi:
- \\(\\theta\\): tham số “thật” theo DGM,
- \\(y\\): dữ liệu quan sát cỡ mẫu \\(N\\),
- \\(S(y)\\): biến chỉ báo thành công (1 nếu đạt tiêu chí, 0 nếu không).

**Assurance tại cỡ mẫu \\(N\\):**
\[
\\mathcal{A}(N)=\\Pr(\\text{thành công tại }N)
=\\mathbb{E}_{\\theta}\\left[\\mathbb{E}_{y\\mid \\theta,N}\\left\\{S(y)\\right\\}\\right]
\]

**Ước lượng Monte Carlo trong app (với \\(R\\) mô phỏng cho mỗi \\(N\\)):**
\[
\\widehat{\\mathcal{A}}(N)=\\frac{1}{R}\\sum_{r=1}^{R} S\\!\\left(y^{(r)}\\right)
\]

Sai số Monte Carlo:
\[
\\mathrm{MCSE}\\left(\\widehat{\\mathcal{A}}(N)\\right)
=\\sqrt{\\frac{\\widehat{\\mathcal{A}}(N)\\left[1-\\widehat{\\mathcal{A}}(N)\\right]}{R}}
\]

**Quy tắc chọn cỡ mẫu:**
Chọn \\(N\\) nhỏ nhất sao cho:
\[
\\widehat{\\mathcal{A}}(N)\\ge \\mathcal{A}_\\text{target}
\]
(ví dụ 0,80 hoặc 0,90).

---

## Tiêu chí thành công (ví dụ thường dùng)
Tùy cấu hình app, có thể chọn một hoặc nhiều tiêu chí:
- **Calibration slope** trong khoảng chấp nhận:
  \[
  0.90 \le b \le 1.10
  \]
  với \\(b\\) ước lượng từ mô hình hiệu chỉnh trên dữ liệu test/validation:
  \[
  \\text{logit}(Y)=a + b\\cdot \\text{logit}(\\widehat{p})
  \]
- **Discrimination (AUC)**:
  \[
  \\mathrm{AUC} \\ge 0.75 \\;(\\text{hoặc ngưỡng do bạn chọn})
  \]
- **Độ chính xác hậu nghiệm**, ví dụ độ rộng CrI 95% của slope:
  \[
  \\mathrm{Width}\\left(\\text{CrI}_{95\\%}(b)\\right) \\le w
  \\quad (\\text{ví dụ } w=0.20)
  \]

---

## Chú giải đầu vào (tìm ở đâu; chọn bao nhiêu)

### 1) Tỷ lệ biến cố \\(p\\)
**Nguồn:** dữ liệu hồi cứu/đoàn hệ gần nhất tại bệnh viện; registry; y văn tương đồng.  
**Thông lệ khi lập kế hoạch:** 0,05–0,15 thường gặp (tùy bệnh).  
**Khuyến nghị:** chạy độ nhạy theo khoảng plausible.

### 2) Số tham số (df) \\(P\\)
**Nguồn:** đặc tả mô hình dự kiến (đếm theo tham số, không phải số biến).  
Bao gồm dummy, spline, tương tác; không tính intercept.  
**Thông lệ:** 10–30 df; df càng cao càng cần mẫu lớn và prior hợp lý.

### 3) Tương quan biến dự báo \\(\\rho\\)
**Nguồn:** ước lượng từ dữ liệu bệnh viện (ma trận tương quan của biến ứng viên).  
Nếu chưa biết, chạy độ nhạy (0; 0,1; 0,3).  
**Thông lệ:** 0–0,3 là mức nhẹ–vừa; tương quan cao làm tăng bất ổn và có thể tăng cỡ mẫu.

### 4) Danh sách \\(N\\) ứng viên
Chọn dải đủ rộng để thấy ngưỡng đạt/không đạt (500–2000 hoặc hơn tùy khả thi).

### 5) Số mô phỏng mỗi \\(N\\) (R)
- **Demo:** 50–200  
- **Final:** ≥500–1000  
Dùng MCSE để đánh giá độ ổn định.

### 6) Ngưỡng assurance \\(\\mathcal{A}_\\text{target}\\)
- **0,80:** hay dùng khi ưu tiên khả thi  
- **0,90:** khi muốn chắc chắn cao hơn

---

## Ưu điểm và nhược điểm
**Ưu điểm**
- Phù hợp “end-to-end” với workflow Bayes; nhắm trực tiếp tiêu chí hậu nghiệm.
- Linh hoạt với DGM, tương quan, tiêu chí hiệu năng và độ chính xác.
- Có thể xử lý biến cố hiếm tốt hơn khi dùng prior co rút (regularizing priors).

**Nhược điểm**
- Tốn tính toán; nhạy với cài đặt MCMC và hội tụ.
- Phụ thuộc giả định DGM và prior → cần phân tích độ nhạy.
- Phải mô phỏng đúng pipeline dự kiến để tránh ước tính sai.

---

## Tài liệu tham khảo
1) O'Hagan A. Assurance in clinical trial design. *Pharmaceutical Statistics.* 2005.  
2) Pan J, Banerjee S. bayesassurance: An R Package for Calculating Sample Size and Bayesian Assurance. *The R Journal.* 2023.  
3) Gelman A, Jakulin A, Pittau MG, Su Y-S. A weakly informative default prior distribution for logistic and other regression models. *The Annals of Applied Statistics.* 2008.  
4) Sahu SK, Smith TMF. Bayesian methods of sample size determination. *Statistical Methodology / related Bayesian SSD literature.* 2006.
""",
        # Email & Reporting
        "report_header": "Báo cáo & Tải xuống",
        "btn_download_report": "Tải Báo cáo (Văn bản)",
        "btn_download_html": "Tải Báo cáo (Định dạng HTML)",
        "btn_download_csv": "Tải Kết quả (CSV)",
        "report_title": "Báo cáo Tính toán Cỡ mẫu",
        "footer_text": "Tác giả & Quản trị: Minh Nguyễn (minhnt@ump.edu.vn) Bộ môn Dịch tễ học, Khoa Y tế Công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam",
        "btn_refresh": "Làm mới / Đặt lại",
        "email_header": "Gửi Kết quả qua Email",
        "email_to": "Email Người nhận",
        "email_send_btn": "Gửi Email",
        "email_success": "Đã gửi email thành công!",
        "email_error": "Lỗi khi gửi email:",
        "email_settings": "Cài đặt Email (SMTP)",
        "email_sender": "Email Của Bạn",
        "email_password": "Mật khẩu Ứng dụng",
        "email_subject_default": "Kết quả Tính toán Cỡ mẫu",
}

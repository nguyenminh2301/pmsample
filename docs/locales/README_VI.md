# Ước tính Cỡ mẫu cho Nghiên cứu Tiên lượng

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Một bộ công cụ để tính toán cỡ mẫu tối thiểu trong nghiên cứu tiên lượng lâm sàng. Được thiết kế dành cho các nhà khoa học dữ liệu, nhà thống kê và nghiên cứu viên lâm sàng, ứng dụng này triển khai các phương pháp thống kê đã được kiểm chứng cho **Phát triển Mô hình Dự báo**, **Thẩm định Ngoài (External Validation)**, **Nghiên cứu Yếu tố Tiên lượng**, và **Cập nhật Mô hình**.

🔗 **Truy cập Ứng dụng:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

> **Lưu ý**: Cập nhật bổ sung một phần các ngôn ngữ Trung Quốc, Nhật, Pháp, Đức bằng AI, mong rằng mọi thắc mắc vui lòng liên hệ admin của app.

---

## 1. Tổng quan và Mục đích

Ứng dụng này cung cấp một bộ công cụ để giải quyết các yêu cầu phức tạp của việc lập kế hoạch cỡ mẫu trong nghiên cứu y học. Khác với các công cụ tính toán power cơ bản, công cụ này tập trung vào các sắc thái cụ thể của *mô hình hóa tiên lượng*, nơi mục tiêu thường là ước tính chính xác nguy cơ (hiệu chuẩn và phân biệt) thay vì kiểm định giả thuyết đơn thuần.

### Các Tính năng Chính

* **Độ chính xác Phương pháp luận**: Triển khai các thuật toán tuân thủ nghiêm ngặt các tài liệu thống kê đã được bình duyệt (Riley et al., Hanley & McNeil, Hsieh, et al.).
* **Kiểm chứng (Validation)**: Các tính toán cốt lõi đã được đối chiếu với các gói R uy tín (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) để đảm bảo độ chính xác.
* **Hỗ trợ Đa ngôn ngữ**: Hỗ trợ đầy đủ tiếng Anh và tiếng Việt, tạo thuận lợi cho hợp tác quốc tế.
* **Phân tích Độ nhạy**: Tích hợp xử lý hàng loạt cho phép các nhà nghiên cứu đánh giá sự thay đổi yêu cầu cỡ mẫu qua một loạt các giả định (ví dụ: thay đổi tỷ lệ hiện mắc hoặc $R^2$ dự kiến).

---

## 2. Danh mục Phương pháp

Ứng dụng được cấu trúc thành bốn mô-đun chính, mỗi mô-đun nhắm mục tiêu đến một giai đoạn cụ thể của chu trình nghiên cứu.

### A. Đánh giá Tính khả thi Sơ bộ

| Phương pháp                                    | Mô tả                                                                                                                 | Tình huống Ứng dụng                                                                                                                                                                   |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1: Events Per Variable (EPV/EPP)**       | Quy tắc kinh nghiệm dựa trên tỷ lệ số biến cố trên số tham số dự báo.                                     | *Chỉ dùng để kiểm tra tính khả thi.* **Không khuyến nghị dùng làm căn cứ chính** cho đề cương nghiên cứu vì không tính đến overfitting hay calibration. |
| **A2: Độ chính xác của Nguy cơ Nền** | Ước tính cỡ mẫu cần thiết để ước tính tỷ lệ hiện mắc với độ rộng Khoảng tin cậy (CI) xác định. | Dịch tễ học mô tả; lập kế hoạch cho calibration-in-the-large.                                                                                                                     |

### B. Nghiên cứu Yếu tố Tiên lượng (Mối liên quan)

| Phương pháp                          | Mô tả                                                                                                                                      | Tài liệu tham khảo         |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| **B3: Logistic Regression Power** | Tính cỡ mẫu để phát hiện Tỷ số Chênh (OR) mục tiêu cho một biến dự báo, có hiệu chỉnh tương quan với các biến khác. | **Hsieh et al. (1998)** |
| **B4: Cox Regression Power**      | Tính số biến cố cần thiết để phát hiện Tỷ số Nguy cơ (HR) mục tiêu trong phân tích sống còn.                              | **Schoenfeld (1983)**   |

### C. Phát triển Mô hình Dự báo (Khuyến nghị)

Đây là mô-đun cốt lõi để xây dựng các mô hình dự báo lâm sàng mới.

| Phương pháp                                   | Mô tả                                                                                                           | Mục tiêu Chính                                                                                                                                             |
| :----------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **C5: Phương pháp Giải tích (Riley)** | **Tiêu chuẩn Vàng.** Công thức đóng cho phát triển mô hình đa biến.                            | 1. Hạn chế co rút toàn cục (shrinkage$S \ge 0.9$).<br />2. Hạn chế sự lạc quan về hiệu năng.<br />3. Ước tính chính xác hệ số intercept. |
| **C6: Thiết kế dựa trên Mô phỏng**   | Mô phỏng Cơ chế Sinh Dữ liệu (DGM) cụ thể để ước tính yêu cầu cho các mô hình phức tạp.       | Các thuật ngữ phi tuyến, tương tác phức tạp, cấu trúc tương quan đặc thù.                                                                     |
| **C7: Bayesian Assurance**                 | Mô phỏng dựa trên MCMC để xác định cỡ mẫu với xác suất thành công được đảm bảo (Assurance). | Phát triển mô hình theo trường phái Bayes.                                                                                                             |

### D. Thẩm định và Cập nhật Mô hình

Các công cụ để lập kế hoạch thẩm định ngoài (external validation) cho các mô hình hiện có.

| Phương pháp                                  | Mô tả                                                                                                                  | Tài liệu tham khảo                             |
| :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| **D8: Độ chính xác AUC**              | Tính N để đạt được độ rộng Khoảng tin cậy xác định cho AUC (C-statistic).                                | **Hanley & McNeil (1982)**                  |
| **D9: Cỡ mẫu Thẩm định Tùy chỉnh** | Tính N để đảm bảo ước tính chính xác tỷ lệ O/E, Calibration Slope, và AUC.                                 | **Riley et al. (2021)** / `pmvalsampsize` |
| **D10: Mô phỏng Thẩm định**          | Lập kế hoạch dựa trên mô phỏng sử dụng phân phối của yếu tố Tiên lượng Tuyến tính (LP).               | **Snell et al. (2021)**                     |
| **D11: Cập nhật Mô hình**             | Cỡ mẫu cần thiết để cập nhật (hiệu chuẩn lại) một mô hình hiện có (Intercept/Slope) cho bối cảnh mới. | **Van Calster et al.**                      |

---

## 3. Cài đặt và Chạy cục bộ

Để triển khai ứng dụng này trên hạ tầng của riêng bạn:

### Yêu cầu Tiên quyết

* Python 3.9 trở lên
* Git

### Các bước Triển khai

1. **Sao chép Kho lưu trữ (Clone)**

   ```bash
   git clone https://github.com/nguyenminh2301/pmsample.git
   cd pmsample
   ```
2. **Thiết lập Môi trường**
   Khuyến nghị sử dụng môi trường ảo (virtual environment).

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```
3. **Cài đặt Thư viện phụ thuộc**

   ```bash
   pip install -r requirements.txt
   ```
4. **Khởi chạy Ứng dụng**

   ```bash
   streamlit run pmsampsize_app/app.py
   ```

---

## 4. Tuyên bố Miễn trừ Trách nhiệm

**Chỉ dành cho mục đích Học thuật và Nghiên cứu.**

Phần mềm này là một sự triển khai của các phương pháp thống kê được công bố trong các tài liệu đã qua bình duyệt. Mặc dù mọi nỗ lực đã được thực hiện để đảm bảo tính chính xác của các thuật toán, các tác giả và người bảo trì không chịu trách nhiệm về thiết kế hoặc kết quả của bất kỳ nghiên cứu nào dựa trên công cụ này.

* **Trách nhiệm của Người dùng**: Người dùng chịu trách nhiệm xác minh các tham số đầu vào và giải thích kết quả trong bối cảnh lâm sàng cụ thể của họ.
* **Không đảm bảo Y tế**: Công cụ này không cung cấp lời khuyên y tế.

---

**Tác giả & Bảo trì:**
Minh Nguyen (minhnt@ump.edu.vn)
Bộ môn Dịch tễ học, Khoa Y tế công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam

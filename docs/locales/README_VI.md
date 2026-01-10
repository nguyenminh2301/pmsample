# Bộ công cụ ước tính cỡ mẫu mô hình tiên lượng (Prognosis-N)

> *Bộ công cụ dành cho Phát triển, Thẩm định và Cập nhật các Mô hình Dự báo Nghiên cứu Tiên lượng Lâm sàng.*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Một bộ công cụ để tính toán cỡ mẫu tối thiểu trong nghiên cứu tiên lượng lâm sàng. Được thiết kế dành cho các nhà khoa học dữ liệu, nhà thống kê và nghiên cứu lâm sàng, ứng dụng này triển khai các phương pháp thống kê đã được kiểm chứng cho **Phát triển Mô hình Dự báo**, **Thẩm định Ngoài (External Validation)**, **Nghiên cứu Yếu tố Tiên lượng**, và **Cập nhật Mô hình**.

🔗 **Truy cập Ứng dụng:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

> **Lưu ý**: Cập nhật bổ sung một phần các ngôn ngữ Trung Quốc, Nhật, Pháp, Đức bằng AI, mong rằng mọi thắc mắc vui lòng liên hệ admin của app.

---

## 1. Tổng quan và Mục đích

Ứng dụng này cung cấp một bộ công cụ để giải quyết các yêu cầu phức tạp của việc lập kế hoạch cỡ mẫu trong nghiên cứu y học. Khác với các công cụ tính toán power cơ bản, công cụ này tập trung vào các sắc thái cụ thể của *mô hình hóa tiên lượng*, nơi mục tiêu thường là ước tính chính xác nguy cơ (hiệu chuẩn và phân biệt) thay vì kiểm định giả thuyết đơn thuần.

### Các Tính năng Chính

* **Độ chính xác Phương pháp luận**: Triển khai các thuật toán tuân thủ nghiêm ngặt các tài liệu thống kê đã được bình duyệt (Riley et al., Hanley & McNeil, Hsieh, et al.).
* **Kiểm chứng (Validation)**: Các tính toán cốt lõi đã được đối chiếu với các gói R (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) để đảm bảo độ chính xác.
* **Hỗ trợ Đa ngôn ngữ**: Hỗ trợ đầy đủ tiếng Anh và tiếng Việt, tạo thuận lợi cho hợp tác quốc tế.
* **Phân tích Độ nhạy**: Tích hợp xử lý hàng loạt cho phép các nhà nghiên cứu đánh giá sự thay đổi yêu cầu cỡ mẫu qua một loạt các giả định (ví dụ: thay đổi tỷ lệ hiện mắc hoặc $R^2$ dự kiến).

---

## 2. Danh mục Phương pháp

Ứng dụng được cấu trúc thành bốn mô-đun chính, mỗi mô-đun nhắm mục tiêu đến một giai đoạn cụ thể của chu trình nghiên cứu.

### A. Kết cục Nhị phân

#### Nhóm phụ A1: Kiểm tra nhanh

| Phương pháp                                 | Mô tả                                                         |
| :--------------------------------------------- | :-------------------------------------------------------------- |
| **A1.1: Quy tắc kinh nghiệm (EPV)**    | Kiểm tra sơ bộ theo kinh nghiệm (biến cố trên tham số). |
| **A1.2: Độ chính xác Nguy cơ Nền** | Cỡ mẫu để ước tính tỷ lệ hiện mắc (độ rộng KTC).  |

#### Nhóm phụ A2: Yếu tố Tiên lượng

| Phương pháp                         | Mô tả                                                  |
| :------------------------------------- | :------------------------------------------------------- |
| **A2.1: Logistic Power (Hsieh)** | Power để phát hiện OR cho một biến dự báo đơn. |
| **A2.2: Cox Power (Schoenfeld)** | Power để phát hiện HR cho một biến dự báo đơn. |

#### Nhóm phụ A3: Phát triển Mô hình (Dự báo)

| Phương pháp                             | Mô tả                                                                                                       |
| :----------------------------------------- | :------------------------------------------------------------------------------------------------------------ |
| **A3.1: Riley et al. (Giải tích)** | **Tiêu chuẩn Vàng.** Cỡ mẫu phát triển để hạn chế overfitting & đảm bảo độ chính xác. |
| **A3.2: Mô phỏng Phát triển**    | Lập kế hoạch dựa trên mô phỏng cho các mô hình phức tạp (DGM).                                    |
| **A3.3: Bayesian Assurance**         | Đảm bảo (Assurance) dựa trên MCMC cho mô hình Bayes.                                                   |

#### Nhóm phụ A4: Thẩm định / Cập nhật

| Phương pháp                                   | Mô tả                                                                   |
| :----------------------------------------------- | :------------------------------------------------------------------------ |
| **A4.1: Độ chính xác AUC**             | Cỡ mẫu cho độ rộng KTC của AUC (Hanley-McNeil).                     |
| **A4.2: Thẩm định Ngoài (Tailored)**   | Mục tiêu độ chính xác calibration và discrimination (Riley/Snell). |
| **A4.3: Thẩm định Ngoài (Mô phỏng)** | Lập kế hoạch thẩm định dựa trên mô phỏng (phân phối LP).      |
| **A4.4: Cập nhật Mô hình**             | Cỡ mẫu để hiệu chuẩn lại intercept/slope.                          |

### B. Kết cục Liên tục

| Phương pháp                          | Mô tả                                                           |
| :-------------------------------------- | :---------------------------------------------------------------- |
| **B1: Quy tắc Green**            | Quy tắc kinh nghiệm cho hồi quy tuyến tính (50 + 8k).        |
| **B2: Riley et al. (Liên tục)** | Phương pháp giải tích cho hồi quy tuyến tính (residuals). |

### C. Kết cục Sống còn

| Phương pháp                          | Mô tả                                                       |
| :-------------------------------------- | :------------------------------------------------------------ |
| **C1: Riley et al. (Sống còn)** | Phương pháp giải tích cho mô hình Cox (time-to-event). |

---

## 3. Cài đặt và Chạy cục bộ

Để triển khai ứng dụng này trên hạ tầng của riêng bạn:

**Kho lưu trữ (Repositories):**

* **GitLab (Chính)**: [`gitlab.com/minhthiennguyen/pmsample`](https://gitlab.com/minhthiennguyen/pmsample.git)
* **GitHub (Dự phòng)**: [`github.com/nguyenminh2301/pmsample`](https://github.com/nguyenminh2301/pmsample.git)

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

## 5. Trích dẫn

Nếu bạn sử dụng công cụ này trong nghiên cứu, vui lòng trích dẫn như sau:

> Nguyen, M. (2025). Prognostic Research Sample Size Tool (Version 1.0) [Software]. Available at https://pmsample.streamlit.app/

Hoặc sử dụng BibTeX:

```bibtex
@software{nguyen2025pmsample,
  author = {Nguyen, Minh},
  title = {Prognostic Research Sample Size Tool},
  year = {2025},
  url = {https://pmsample.streamlit.app/},
  version = {1.0}
}
```

---

**Tác giả & Bảo trì:**
Minh Nguyen, MPH (Mr/ He/ him)
email: minhnt@ump.edu.vn
Bộ môn Dịch tễ học, Khoa Y tế công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam

# 🍷 Wine Quality Prediction System

Dự án Hệ thống Dự đoán Chất lượng Rượu sử dụng Machine Learning. Hệ thống bao gồm một Backend API xây dựng bằng **FastAPI** và một giao diện người dùng trực quan xây dựng bằng **Streamlit**.

---

## 🌟 Các Tính Năng Chính
- **Giao diện (Streamlit):** 
- **Backend (FastAPI):**
- **Machine Learning:**
---

## 🛠 Cài Đặt (Installation)

Yêu cầu bạn đã cài đặt Python (khuyên dùng Python 3.9+). 
Mở Terminal tại thư mục gốc của dự án (`wine_qualitiy_prediction_app`) và chạy lệnh sau để tải toàn bộ các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

*(Các thư viện chính bao gồm: fastapi, uvicorn, streamlit, requests, scikit-learn, joblib, pydantic...)*

---

## 🚀 Hướng Dẫn Sử Dụng (Chạy Ứng Dụng)

Hệ thống hoạt động dưới dạng Client - Server. Do đó, bạn cần mở **2 cửa sổ Terminal** riêng biệt: một để chạy Backend (API) và một để chạy Frontend (Giao diện web).

### Bước 1: Khởi động Backend (FastAPI)
Mở Terminal 1 tại thư mục gốc của dự án và chạy lệnh sau để khởi động server uvicorn:
```bash
uvicorn backend.app.main:app --reload
```
API sẽ khởi chạy tại: `http://127.0.0.1:8000`. 
*(Bạn có thể truy cập `http://127.0.0.1:8000/docs` để xem tài liệu API tự động sinh bởi Swagger UI).*

### Bước 2: Khởi động Frontend (Streamlit)
Giữ nguyên Terminal 1. Hãy mở một **Terminal 2** mới (cũng ở thư mục gốc của dự án) và chạy lệnh:
```bash
streamlit run app.py
```
Trình duyệt sẽ tự động mở trang web giao diện người dùng tại: `http://localhost:8501`.

### Bước 3: Trải Nghiệm Dự Đoán
Trên giao diện web, hãy nhập các thông số vật lý, hóa học của rượu (VD: fixed acidity, alcohol, type...) và nhấn nút **"Dự đoán chất lượng"**. Frontend sẽ tự động gửi một POST request tới Backend API và trả về điểm chất lượng mô hình phân tích được.

---

## 📁 Cấu Trúc Dự Án

```text
wine_qualitiy_prediction_app/
│
├── app.py                  # Mã nguồn giao diện Frontend (Streamlit).
├── requirements.txt        # Danh sách các thư viện cần thiết để chạy dự án.
│
├── backend/app/            # Thư mục mã nguồn Backend (FastAPI):
│   ├── main.py             # File khởi chạy ứng dụng API.
│   ├── core/inferences.py  # Chứa logic dự đoán, load model joblib.
│   ├── schemas/schemas.py  # Định nghĩa cấu trúc dữ liệu input (Pydantic Models).
│   └── core/config.py      # Cấu hình cài đặt API (ví dụ: CORS middleware).
│
├── wine_predict_ML/models/ # Thư mục chứa mô hình Machine Learning:
│   └── my_model.joblib     # File model ML đã được huấn luyện (Train).
│
├── data/                   # Thư mục lưu trữ dataset (CSV files...).
└── notebooks/              # Chứa các file Jupyter Notebook phân tích dữ liệu (EDA).
```

---


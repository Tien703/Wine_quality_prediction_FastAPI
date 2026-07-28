import streamlit as st
import requests
st.title("Ứng dụng dự đoán chất lượng rượu")
st.write("Nhập các thông số để dự đoán chất lượng rượu")
col1, col2 = st.columns(2)
with col1:
    fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=20.0, value=7.4, step=0.1)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=3.0, value=0.70, step=0.01)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=2.0, value=0.00, step=0.01)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=100.0, value=1.9, step=0.1)
    chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, value=0.076, step=0.001, format="%.3f")
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, max_value=500.0, value=11.0, step=1.0)

with col2:
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, max_value=600.0, value=34.0, step=1.0)
    density = st.number_input("Density", min_value=0.8, max_value=1.2, value=0.9978, step=0.0001, format="%.4f")
    pH = st.number_input("pH", min_value=2.0, max_value=5.0, value=3.51, step=0.01)
    sulphates = st.number_input("Sulphates", min_value=0.0, max_value=3.0, value=0.56, step=0.01)
    alcohol = st.number_input("Alcohol", min_value=0.0, max_value=25.0, value=9.4, step=0.1)
    type_wine = st.selectbox("Type", ["red", "white"])
if st.button("Dự đoán chất lượng"):
    payload = {
        "fixed_acidity" : fixed_acidity,
        "volatile_acidity":  volatile_acidity,
        "citric_acid": citric_acid,
        "residual_sugar": residual_sugar,
        "chlorides": chlorides,
        "free_sulfur_dioxide": free_sulfur_dioxide,
        "total_sulfur_dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol,
        "type": type_wine

    }
    API_URL = "http://backend:8000/predict/"
    try:
        # Bắn request POST sang Backend
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            # Bóc tách key "quality" từ JSON nhận được
            score = result.get("quality")
            
            # --- BƯỚC 3: Hiển thị kết quả ---
            st.metric(label="Điểm chất lượng rượu dự đoán", value=f"{score} / 10")
        else:
            st.error(f"Lỗi Backend trả về mã: {response.status_code}")
            
    except Exception as e:
        st.error(f"Không thể kết nối tới API. Hãy chắc chắn rằng bạn đã bật lệnh uvicorn trước! Lỗi: {e}")
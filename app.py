import streamlit as st
import requests
st.title("Ứng dụng dự đoán chất lượng rượu")
st.write("Nhập các thông số để dự đoán chất lượng rượu")
col1, col2 = st.columns(2)
with col1:
    fixed_acidity= st.number_input("fixed acidity",min_value=0, max_value=10)
    volatile_acidity = st.number_input("volatile_acidity" )
    citric_acid = st.number_input("citric_acid")
    residual_sugar = st.number_input("residual_sugar")
    chlorides = st.number_input("chlorides")
    free_sulfur_dioxide = st.number_input("free sulfur dioxide")
    total_sulfur_dioxide = st.number_input("total sulfur dioxide")
with col2:
    total_sulfur_dioxide  = st.number_input("total_sulfur_dioxide")
    density= st.number_input("density")
    pH= st.number_input("pH")
    sulphates= st.number_input("sulphates")
    alcohol= st.number_input("alcohol")
    type = st.selectbox("type", ["red", "white"])
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
        "type": type

    }
    API_URL = "http://127.0.0.1:8000/predict/"
    try:
        # Bắn request POST sang Backend
        response = requests.post(API_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            # Bóc tách key "quality" từ JSON nhận được
            score = result.get("quality")
            
            # --- BƯỚC 3: Hiển thị kết quả ---
            st.metric(label="Điểm chất lượng rượu dự đoán", value="5.16 / 10")
        else:
            st.error(f"Lỗi Backend trả về mã: {response.status_code}")
            
    except Exception as e:
        st.error(f"Không thể kết nối tới API. Hãy chắc chắn rằng bạn đã bật lệnh uvicorn trước! Lỗi: {e}")
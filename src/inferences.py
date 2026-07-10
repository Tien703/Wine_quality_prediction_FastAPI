import pandas as pd
import joblib
import numpy as np

model = joblib.load("../models/my_model.joblib")
def predict_wine_quality(data_inputs: dict) ->float:
    df = pd.DataFrame([data_inputs])
    #Convert to red/white
    df["type"] = df["type"].str.strip(" ").map({"red": 1, "white": 0})
    #Feature engineering
    df["free_to_total_SO2"]    = df["free_sulfur_dioxide"] / (df["total_sulfur_dioxide"] + 1e-6)
    df["acidity_ratio"]        = df["fixed_acidity"] / (df["volatile_acidity"] + 1e-6)
    df["acid_sugar_ratio"]     = df["fixed_acidity"] / (df["residual_sugar"] + 1e-6)

    # Tương tác features
    df["alcohol_density"]      = df["alcohol"] * df["density"]
    df["sulphates_alcohol"]    = df["sulphates"] * df["alcohol"]
    df["sulphates_SO2"]        = df["sulphates"] * df["free_sulfur_dioxide"]

    # Log transform (giảm skewness)
    for col in ["residual_sugar", "chlorides", "free_sulfur_dioxide",
            "total_sulfur_dioxide", "sulphates"]:
        df[f"log_{col.replace(' ', '_')}"] = np.log1p(df[col])

    # Polynomial features cho top predictors
    for col in ["alcohol", "volatile_acidity", "sulphates"]:
        df[f"{col.replace(' ', '_')}_sq"] = df[col] ** 2


    #Predict
    predict = model.predict(df)
    print(predict[0])
    return predict


if __name__ == "__main__":
    # 1. Tạo bộ dữ liệu giả lập (Mock Data) gồm 12 thông số thô ban đầu
    # Chú ý: Các key này phải khớp hoàn toàn với tên trường bạn dùng trong hàm xử lý (dict)
    test_data = {
        "fixed_acidity": 7.4,
        "volatile_acidity": 0.70,
        "citric_acid": 0.00,
        "residual_sugar": 1.9,
        "chlorides": 0.076,
        "free sulfur_dioxide": 11.0,
        "total_sulfur_dioxide": 34.0,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4,
        "type": "red"
    }
    
    print("--- BẮT ĐẦU TEST CỤC BỘ FILE INFERENCE ---")
    print(f"Dữ liệu thô đầu vào: {test_data}\n")
    
    # 2. Gọi hàm dự đoán và truyền mock data vào làm tham số
    try:
        ket_qua = predict_wine_quality(test_data)
        
        # 3. In kết quả ra màn hình để kiểm tra
        print("--- TEST THÀNH CÔNG ---")
        print(f"Điểm chất lượng rượu dự đoán trả về: {ket_qua}")
        print(f"Kiểu dữ liệu của kết quả: {type(ket_qua)}")
        
    except Exception as e:
        print("--- TEST THẤT BẠI (CÓ LỖI) ---")
        print(f"Lỗi xuất hiện: {str(e)}")
        print("Hãy kiểm tra lại xem tên các cột trong hàm feature_engineering đã khớp với key của test_data chưa nhé!")
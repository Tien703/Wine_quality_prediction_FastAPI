from fastapi import FastAPI
from schemas import Wine
from inferences import predict_wine_quality
from config import setup_cors

app = FastAPI()
setup_cors(app)

@app.post("/predict/")
def predective_wine_quality(features:Wine):
    features = features.model_dump()
    pre_quality =predict_wine_quality(features)
    return {"quality": pre_quality[0]}

    


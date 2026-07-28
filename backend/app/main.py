from fastapi import FastAPI
from backend.app.schemas.schemas import Wine, WineQualityRespond
from backend.app.core.inferences import predict_wine_quality
from backend.app.core.config import setup_cors

app = FastAPI()
setup_cors(app)

@app.post("/predict/", response_model=WineQualityRespond )
def predective_wine_quality(features:Wine):
    features = features.model_dump()
    pre_quality =predict_wine_quality(features)
    return {"quality": pre_quality}

    


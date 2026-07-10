from pydantic import BaseModel, Field
class Wine(BaseModel):
    fixed_acidity: float = Field(..., ge=0)
    volatile_acidity: float = Field(...)
    citric_acid: float=Field(...)
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    type: str

    
    
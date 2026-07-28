# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field  
from typing import Literal
class Wine(BaseModel):
    fixed_acidity: float = Field(
        ..., ge=0, le=20.0, description="Fixed acidity in g/dm3"
    )
    volatile_acidity: float = Field(
        ..., ge=0, le=3.0, description="Volatile acidity in g/dm3"
    )
    citric_acid: float = Field(
        ..., ge=0, le=2.0, description="Citric acid in g/dm3"
    )
    residual_sugar: float = Field(
        ..., ge=0, le=100.0, description="Residual sugar in g/dm3"
    )
    chlorides: float = Field(
        ..., ge=0, le=1.0, description="Chlorides in g/dm3"
    )
    free_sulfur_dioxide: float = Field(
        ..., ge=0, le=500.0, description="Free sulfur dioxide in mg/dm3"
    )
    total_sulfur_dioxide: float = Field(
        ..., ge=0, le=600.0, description="Total sulfur dioxide in mg/dm3"
    )
    density: float = Field(
        ..., ge=0.8, le=1.2, description="Density in g/cm3"
    )
    pH: float = Field(..., ge=2.0, le=5.0, description="pH level")
    sulphates: float = Field(
        ..., ge=0, le=3.0, description="Sulphates in g/dm3"
    )
    alcohol: float = Field(
        ..., ge=0, le=25.0, description="Alcohol content in % vol"
    )
    type: Literal["red", "white"] = Field(
        ..., description="Type of wine: red or white"
    )
class WineQualityRespond(BaseModel):   
    quality: float
    
    
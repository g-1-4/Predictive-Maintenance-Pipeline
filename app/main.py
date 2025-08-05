from fastapi import FastAPI
from app.schemas import predictionRequest
from app.inference import predict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Predictive Maintenance API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def get_prediction(data: predictionRequest):
    features = {
    "Type": data.Type,
    "Air temperature [K]": data.Air_temperature,
    "Process temperature [K]": data.Process_temperature,
    "Rotational speed [rpm]": data.Rotational_speed,
    "Torque [Nm]": data.Torque,
    "Tool wear [min]": data.Tool_wear
    }
    result = predict(features)
    return {"Prediction": result}
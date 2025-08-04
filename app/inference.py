import joblib
import pandas as pd


model = joblib.load('models/predictive_maintenance_model.pkl')

def predict(features: dict):
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return int(prediction)
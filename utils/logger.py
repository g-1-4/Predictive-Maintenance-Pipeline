from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def log_prediction(data: dict, prediction: int):
    insert_data = {
        "Type": data["Type"],
        "Air temperature [K]": data["Air temperature [K]"],
        "Process temperature [K]": data["Process temperature [K]"],
        "Rotational speed [rpm]": data["Rotational speed [rpm]"],
        "Torque [Nm]": data["Torque [Nm]"],
        "Tool wear [min]": data["Tool wear [min]"],
        "prediction": prediction
    }

    supabase.table("prediction_logs").insert(insert_data).execute()
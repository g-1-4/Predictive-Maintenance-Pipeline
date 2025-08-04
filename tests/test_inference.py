from app.inference import predict
import os

def test_model_file_exists_and_not_empty():
    assert os.path.exists("models/predictive_maintenance_model.pkl"), "Model file is missing"

def test_prediction_function():
    sample_input = {
        "type": "L",
        "air_temperature": 298.1,
        "process_temperature": 308.6,
        "rotational_speed": 1551,
        "torque": 42.8,
        "tool_wear": 0
    }
    result = predict(sample_input)
    assert result in [0, 1], "Prediction should be either 0 or 1"
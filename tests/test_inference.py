from app.inference import predict
import os

def test_model_file_exists_and_not_empty():
    assert os.path.exists("models/predictive_maintenance_model.pkl"), "Model file is missing"


def test_prediction_output_format():
    from app.inference import predict
    sample_input = {
        "Type": "L",
        "Air temperature [K]": 298.1,
        "Process temperature [K]": 308.6,
        "Rotational speed [rpm]": 1551,
        "Torque [Nm]": 42.8,
        "Tool wear [min]": 0
    }
    result = predict(sample_input)
    assert isinstance(result, int), "Prediction must be an integer"
    assert result in [0, 1], "Prediction must be 0 or 1"
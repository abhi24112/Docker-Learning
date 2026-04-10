import joblib as jb
import pandas as pd
import numpy as np
from src.data_preprocessing import scale_features, encoding, load_scaler
from src.utils import load_config

# Load config to get run name
mlflow_config, _, _, _ = load_config()
run_name = mlflow_config['run_name']

# Load models dynamically
xgb_model = jb.load(f"./models/{run_name}_xgboost.jbl")
gb_model = jb.load(f"./models/{run_name}_gradient_boosting.jbl")

# Load the scaler used during training (optional)
scaler = None
try:
    scaler = load_scaler()
    print("✅ Models and scaler loaded successfully!")
except FileNotFoundError:
    print("⚠️  Models loaded, but scaler not found. Please run training first to create scaler.joblib")


def predict(input_data):
    """Make predictions on input data."""
    if scaler is None:
        raise ValueError("Scaler not loaded. Please run training first to create scaler.joblib")
    
    # input_data can be a DataFrame or dictionary
    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])
    
    # Prepare data
    data = input_data.copy()
    data = encoding(data)
    data, _ = scale_features(data, scaler=scaler)  # Use the pre-fitted scaler
    
    # Get predictions
    xgb_pred = xgb_model.predict(data)
    gb_pred = gb_model.predict(data)
    ensemble_pred = (xgb_pred + gb_pred) / 2
    
    return {
        'xgboost': xgb_pred,
        'gradient_boosting': gb_pred,
        'ensemble': ensemble_pred
    }


# Example usage
if __name__ == "__main__":
    # Example 1: From dictionary (correct features from dataset)
    sample = {
        'Age': 65,
        'Gender': 'Female',
        'Sleep duration': 6.0,
        'REM sleep percentage': 18,
        'Deep sleep percentage': 70,
        'Light sleep percentage': 12,    
        'Awakenings': 0.0,
        'Caffeine consumption': 0.0,
        'Alcohol consumption': 0.0,
        'Smoking status': 'Yes',
        'Exercise frequency': 3
    }
    
    results = predict(sample)
    print("\nPredictions:")
    print(f"XGBoost: {results['xgboost'][0]:.4f}")
    print(f"Gradient Boosting: {results['gradient_boosting'][0]:.4f}")
    print(f"Ensemble: {results['ensemble'][0]:.4f}")

 
import streamlit as st
import joblib
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import sys

# Add parent directory to path to import src modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.data_preprocessing import scale_features, encoding, load_scaler

# Page Setup
st.set_page_config(
    page_title="Sleep Efficiency Predictor",
    page_icon="🥱",
    layout="centered"
)

# Get the absolute path to the models directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# MODEL_DIR = os.path.join(BASE_DIR, "models")

# Cache the model and scaler loading to avoid reloading on every slider change
@st.cache_resource
def load_model_and_scaler():
    if os.path.exists("/app/models/SEP_Baseline_xgboost.jbl"):  # Inside Docker
        model_path = "/app/models/SEP_Baseline_xgboost.jbl"
        scaler_path = "/app/models/scaler.joblib"
    elif os.path.exists("models/SEP_Baseline_xgboost.jbl"):  # Local Run
        model_path = "models/SEP_Baseline_xgboost.jbl"
        scaler_path = "models/scaler.joblib"
    else:
        model_path = None
        scaler_path = None

    # model_path = os.path.join(MODEL_DIR, "SEP_Baseline_xgboost.jbl")
    # scaler_path = os.path.join(MODEL_DIR, "scaler.joblib")
    
    model = None
    scaler = None
    
    if os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None, None
    else:
        st.error("⚠️ Model file not found.")
    
    if os.path.exists(scaler_path):
        try:
            scaler = joblib.load(scaler_path)
        except Exception as e:
            st.error(f"Error loading scaler: {e}")
            return model, None
    else:
        st.error("⚠️ Scaler file not found.")
    
    return model, scaler

# Load model and scaler
model, scaler = load_model_and_scaler()

# Show toast messages only once using session state
if "model_loaded_toast" not in st.session_state:
    if model is not None and scaler is not None:
        st.toast("✅ Model and scaler loaded successfully")
    elif model is not None:
        st.toast("⚠️ Model loaded but scaler not found")
    else:
        st.toast("❌ Model not found")
    st.session_state.model_loaded_toast = True


# User Interface
st.title("🥱 Sleep :blue[Efficiency] Predictor")
st.write("""
Welcome to the Sleep Efficiency Predictor! This web app uses machine learning models (XGBoost and Gradient Boosting) 
to predict your sleep efficiency based on various health and lifestyle factors.
         
> My Portfolio : [Abhishek Portfolio](https://www.abhiprajapati.me/)
""")
st.markdown("```✨ How it works:```")
st.write("""
    * Fill all the fields in sidebar.
    * Click the **Predict** button.
    * Result will display on the home screen.
""")

st.sidebar.header("User Input")

age = st.sidebar.slider("Age", min_value=0, max_value=100, value=25)
gender = st.sidebar.radio("Gender", ["Male", "Female"], index=0)
sleep_duration = st.sidebar.slider("Sleep Duration (hrs)", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
rem_sleep = st.sidebar.slider("REM Sleep (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.5)
deep_sleep = st.sidebar.slider("Deep Sleep (%)", min_value=0.0, max_value=100.0, value=15.0, step=0.5)
light_sleep = st.sidebar.slider("Light Sleep (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.5)
awakenings = st.sidebar.slider("Number of Awakenings", min_value=0, max_value=10, value=2)
caffeine = st.sidebar.slider("Caffeine Consumption (mg/day)", min_value=0.0, max_value=1000.0, value=50.0, step=10.0)
alcohol = st.sidebar.slider("Alcohol Consumption (drinks/day)", min_value=0.0, max_value=10.0, value=0.0, step=0.5)
smoking = st.sidebar.radio("Smoking Status", ["Non-Smoker", "Smoker"], index=0)
exercise = st.sidebar.slider("Exercise Frequency (days/week)", min_value=0, max_value=7, value=3)

gender_encoded = 0 if gender == "Male" else 1
smoking_encoded = 0 if smoking == "Non-Smoker" else 1

def prediction():
    """Make prediction with proper scaling."""
    # Create a DataFrame with the input features
    feature_names = ['Age', 'Gender', 'Sleep duration', 'REM sleep percentage', 
                     'Deep sleep percentage', 'Light sleep percentage', 'Awakenings', 
                     'Caffeine consumption', 'Alcohol consumption', 'Smoking status', 
                     'Exercise frequency']
    
    input_array = np.array([[age, gender_encoded, sleep_duration, rem_sleep, deep_sleep,
                            light_sleep, awakenings, caffeine, alcohol, smoking_encoded, exercise]])
    
    input_df = pd.DataFrame(input_array, columns=feature_names)
    
    try:
        # Apply scaling using the pre-fitted scaler
        scaled_df, _ = scale_features(input_df, scaler=scaler)
        
        # Get prediction
        pred = model.predict(scaled_df)
        return pred[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

if st.sidebar.button("predict"):
    if model is None:
        st.error("❌ Model not found")
    elif scaler is None:
        st.error("❌ Scaler not found. Please ensure scaler.joblib is in the models directory.")
    else:
        result = prediction()
        if result is not None:
            st.success(f"🌙 Your predicted sleep efficiency is **{(result * 100):.2f}%**")
        else:
            st.error("❌ Error in making predictions / check all values are correctly inserted.")

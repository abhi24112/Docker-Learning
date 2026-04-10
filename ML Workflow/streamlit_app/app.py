import streamlit as st
import joblib
import os
import numpy as np

# Page Setup
st.set_page_config(
    page_title="Sleep Efficiency Predictor",
    page_icon="🥱",
    layout="centered"
)

# Get the absolute path to the models directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Cache the model loading to avoid reloading on every slider change
@st.cache_resource
def load_model():
    model_path = os.path.join(MODEL_DIR, "SEP_Baseline_xgboost.jbl")
    
    if not os.path.exists(model_path):
        return None
    
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        return None

# Load model once
model = load_model()

# Show toast messages only once using session state
if "model_loaded_toast" not in st.session_state:
    if model is not None:
        st.toast("✅ Model loaded successfully")
    else:
        st.toast("❌ Model not found")
    st.session_state.model_loaded_toast = True


# User Interface
st.title("🥱 Sleep :blue[Efficiency] Predictor")
st.write("""
Welcome to the Food Image Predictor! This web app uses a deep learning model (EfficientNetB0) to identify different food items from images. 
With **81% accuracy**, it can classify 101 types of delicious dishes like pizza, sushi, tacos, and more.
         
> Check the **Code of the model** on my [GitHub](https://github.com/abhi24112/Streamlit_app_food101)
         
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
    f = np.array([[age, gender_encoded, sleep_duration, rem_sleep, deep_sleep,
                        light_sleep, awakenings, caffeine, alcohol, smoking_encoded, exercise]]            
                )
    try:
        pred = model.predict(f)
        return pred[0]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

if st.sidebar.button("predict"):
    if model is None:
        st.error("❌Model not found")
    else:
        result = prediction()
        if result is None:
            st.error("❌Error in making predictions / check all values are correctly inserted.")
        st.success(f"🌙 Your predicted sleep efficiency is **{(result* 100):.2f}%**")

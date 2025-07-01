import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from model.granite_loader import load_granite_model

def inject_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background: linear-gradient(135deg, #1e1e2f 0%, #1c1c2b 100%);
            padding: 1rem;
        }
        .stButton>button {
            background-color: #00b894;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #0984e3;
            transform: scale(1.05);
            transition: all 0.3s ease-in-out;
        }
        .stTextInput>div>input, .stTextArea>div>textarea {
            background-color: #2c2c3c;
            color: #ffffff;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

@st.cache_resource(show_spinner=False)
def init_model_with_custom_message():
    with st.spinner("🤖 Booting up HealthAI brain... Please wait"):
        time.sleep(1)
        return load_granite_model()

model = init_model_with_custom_message()

def answer_patient_query(query):
    prompt = f"""
    As a healthcare AI assistant, provide a concise, empathetic response (max 6 sentences) to the patient's question below.
    Avoid medical jargon. Suggest seeing a doctor if appropriate.

    PATIENT QUESTION: {query}

    RESPONSE:
    """
    response = model(prompt, max_length=256, do_sample=False)
    return response[0]['generated_text'].split("RESPONSE:")[-1].strip()

def predict_disease(symptoms, age, gender, medical_history, avg_heart_rate, avg_bp_systolic, avg_bp_diastolic, avg_glucose, recent_symptoms):
    prompt = f"""
    As a medical AI assistant, predict potential health conditions based on the following patient data:
    Current Symptoms: {symptoms}
    Age: {age}
    Gender: {gender}
    Medical History: {medical_history}
    Recent Health Metrics:
    - Avg Heart Rate: {avg_heart_rate} bpm
    - Avg BP: {avg_bp_systolic}/{avg_bp_diastolic} mmHg
    - Avg Glucose: {avg_glucose} mg/dL
    Recently Reported Symptoms: {recent_symptoms}

    Respond with the top 3 most likely conditions, each with:
    1. Condition name
    2. Likelihood (High/Medium/Low)
    3. Brief explanation
    4. Recommended next steps

    RESPONSE:
    """
    response = model(prompt, max_length=256, do_sample=False)
    return response[0]['generated_text'].split("RESPONSE:")[-1].strip()

def generate_treatment(condition, age, gender, history):
    return f"""
    🧪 Treatment Plan Generator

    Condition: {condition or "Not specified"}
    Age: {age}, Gender: {gender}
    Medical History: {history or "None"}

    💊 Recommended Plan:
    - Treatment based on current clinical guidelines
    - Personalized for this patient's specific needs.
    - For pain: Ibuprofen (400–800mg), twice daily
    - For inflammation: Consider Meloxicam or Celecoxib
    - Consult a physician for more accurate treatment.

    ⚠️ This is not a substitute for real medical advice.
    """

def display_patient_chat():
    st.header("🩺 Patient Chat")
    user_input = st.text_input("Ask your health-related question:")
    if user_input:
        with st.spinner("🤖 Thinking... generating response"):
            response = answer_patient_query(user_input)
        st.markdown(f"#### {response}")

def display_treatment_plan():
    st.subheader("🧪 Treatment Plan Generator")

    condition = st.text_input("Enter your diagnosed condition:")
    age = st.number_input("Age:", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
    history = st.text_area("Medical History:")

    if st.button("Generate Treatment Recommendation"):
        with st.spinner("Generating treatment plan..."):
            time.sleep(1)
            result = generate_treatment(condition, age, gender, history)
        st.success("Here is the recommended treatment plan:")
        st.markdown(result)

def display_disease_prediction():
    st.header("🧬 Disease Prediction")
    symptoms = st.text_area("Symptoms:")
    age = st.number_input("Age:", 0, 120, step=1)
    gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
    medical_history = st.text_area("Medical History:")
    avg_heart_rate = st.number_input("Avg Heart Rate (bpm):", 30, 200)
    avg_bp_systolic = st.number_input("Avg BP Systolic (mmHg):", 80, 200)
    avg_bp_diastolic = st.number_input("Avg BP Diastolic (mmHg):", 50, 130)
    avg_glucose = st.number_input("Avg Glucose (mg/dL):", 50, 400)
    recent_symptoms = st.text_area("Recent Symptoms:")

    if st.button("Predict Most Likely Disease"):
        with st.spinner("Analyzing your data..."):
            result = predict_disease(symptoms, age, gender, medical_history, avg_heart_rate, avg_bp_systolic, avg_bp_diastolic, avg_glucose, recent_symptoms)
        st.markdown(f"""
            <div style='padding: 20px; background-color: #2e2e3e; border-radius: 12px; color: white;'>
            <strong>🧠 Prediction:</strong><br>{result}
            </div>
        """, unsafe_allow_html=True)

def display_health_analytics():
    st.header("📈 Health Analytics Dashboard")

    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    heart_rate = np.random.normal(70, 5, size=30)
    bp_systolic = np.random.normal(120, 10, size=30)
    bp_diastolic = np.random.normal(80, 5, size=30)
    glucose = np.random.normal(100, 15, size=30)

    df = pd.DataFrame({
        "Date": dates,
        "Heart Rate": heart_rate,
        "Blood Pressure Systolic": bp_systolic,
        "Blood Pressure Diastolic": bp_diastolic,
        "Blood Glucose": glucose
    })

    st.plotly_chart(px.line(df, x="Date", y="Heart Rate", title="Heart Rate Over Time"))
    st.plotly_chart(px.line(df, x="Date", y=["Blood Pressure Systolic", "Blood Pressure Diastolic"], title="Blood Pressure Over Time"))
    st.plotly_chart(px.line(df, x="Date", y="Blood Glucose", title="Blood Glucose Over Time"))

def main():
    inject_custom_css()
    st.title("🤖 HealthAI Assistant")
    menu = ["Patient Chat", "Disease Prediction", "Treatment Plans", "Health Analytics"]
    choice = st.sidebar.selectbox("Select Functionality", menu)

    if choice == "Patient Chat":
        display_patient_chat()
    elif choice == "Disease Prediction":
        display_disease_prediction()
    elif choice == "Treatment Plans":
        display_treatment_plan()
    elif choice == "Health Analytics":
        display_health_analytics()

if __name__ == "__main__":
    main()
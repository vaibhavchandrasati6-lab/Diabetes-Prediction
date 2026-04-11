import streamlit as st
import numpy as np
import pickle

# Load model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details:")

# Create columns (2 per row)
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0)

with col2:
    glucose = st.number_input("Glucose Level", min_value=0)

col3, col4 = st.columns(2)

with col3:
    blood_pressure = st.number_input("Blood Pressure", min_value=0)

with col4:
    skin_thickness = st.number_input("Skin Thickness", min_value=0)

col5, col6 = st.columns(2)

with col5:
    insulin = st.number_input("Insulin Level", min_value=0)

with col6:
    bmi = st.number_input("BMI", min_value=0.0)

col7, col8 = st.columns(2)

with col7:
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)

with col8:
    age = st.number_input("Age", min_value=0)

# Prediction
if st.button("Predict"):

    input_data = np.array([
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, dpf, age
    ]).reshape(1, -1)

    prediction = loaded_model.predict(input_data)

    if prediction[0] == 0:
        st.success("✅ Person is NOT Diabetic")
    else:
        st.error("⚠️ Person is Diabetic")
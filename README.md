# 🩺 Diabetes Prediction System (Machine Learning App)

A machine learning web application that predicts whether a person is diabetic or not based on medical input parameters. The model is deployed using Streamlit for an interactive and user-friendly interface.

---

## 📌 Project Overview
This project uses a trained Support Vector Machine (SVM) model to predict diabetes based on user inputs such as glucose level, BMI, age, insulin, and other medical attributes.

The goal is to demonstrate how machine learning models can be deployed as real-world web applications.

---
## 🚀 Live Demo
https://diabetes-prediction-fcmfve4zxyuj7jqjceriqn.streamlit.app/

---

## 🧠 Machine Learning Model
- Algorithm: Support Vector Machine (SVM)
- Library: Scikit-learn
- Problem Type: Binary Classification (Diabetic / Non-Diabetic)

---

## 📊 Input Features
The model takes the following inputs:

- Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

---

## 🖥️ Tech Stack
- Python  
- Streamlit  
- Scikit-learn  
- NumPy  
- Pickle  




## 🧪 Example Input (Diabetic Case)
Pregnancies: 8  
Glucose: 180  
Blood Pressure: 90  
Skin Thickness: 40  
Insulin: 200  
BMI: 35  
Diabetes Pedigree Function: 0.8  
Age: 55  

---

## 🎯 Output
0 → Non-Diabetic  
1 → Diabetic  

---

## 🚀 Deployment
This app is deployed using Streamlit Community Cloud.

Steps:
1. Push code to GitHub  
2. Connect repository to Streamlit Cloud  
3. Deploy app.py  

---

## ⚠️ Important Notes
- Input values must be non-negative  
- Model accuracy depends on training dataset  
- If scaler was used during training, apply same scaler in app  

---

## 👨‍💻 Author

Vaibhav Chandra Sati


---

## ⭐ Future Improvements
- Add user history tracking  
- Improve accuracy with advanced models  
- Add probability/confidence score  
- Better UI with charts and analytics  

---

## 📜 License
This project is for educational purposes only.

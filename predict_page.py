import streamlit as st
import pickle
import numpy as np

def load_model():
     with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
        return data  

data = load_model()

model_loaded = data["model"]
lab_country = data["lab_country"]
lab_Ed = data["lab_Ed"]

def show_predict_page():
    st.title("Software Developer Salary Prediction (Anually)")
    st. write("We require few details to predict your Salary")

    countries = (
        "United States of America",
        "Germany",
        "Ukraine",
        "United Kingdom of Great Britain and Northern Ireland",
        "India",
        "France",
        "Canada",
        "Brazil",
    )

    educations = (
        "Post Grad",
        "Master’s degree",
        "Bachelor’s degree",
        "Less than a Bachelors"
    )

    country = st.selectbox("Country",countries)
    education = st.selectbox("Highest Education Level",educations)
    experience = st.slider("Years of Experience",0,50,3)
    age = st.number_input("Enter your Age",25,65)

    result = st.button("Predict Salary")
    if result:
        X_train = np.array([[country, education, experience]])
        X_train[:, 0] = lab_country.transform(X_train[:,0])
        X_train[:, 1] = lab_Ed.transform(X_train[:,1])
        X_train= X_train.astype(float)
        
        salary = model_loaded.predict(X_train)
        st.success(f"The estimated salary is ${salary[0]:.2f}")

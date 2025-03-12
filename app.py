import streamlit as st
import joblib
import numpy as np
model=joblib.load("C:\\Users\\depan\\Downloads\\my_model.pkl")
import streamlit as st

st.markdown("<h1 style='text-align: center; color: white;'>PCOS DIAGNOSIS SYSTEM</h1>", unsafe_allow_html=True)
import streamlit as st

image_path = "C:\\Users\\depan\\Downloads\\Screenshot_2025-03-03_124305-removebg-preview.png"

col1, col2, col3 = st.columns([1.5, 1, 1.5])

with col1:
    st.write("")  # Empty column for spacing

with col2:
    st.image(image_path, width=200)

with col3:
    st.write("")  # Empty column for spacing

age=st.number_input("Age",value=0)
BMI=st.number_input("BMI index",value=0.0)
Menstrual_Irregularity=st.number_input(" Menstrual irregularity(0/1)",value=0)
Testosterone_Level=st.number_input("Testosterone level",value=0.0)
Antral_Follicle_Count=st.number_input("Antral follicle count",value=0)

if st.button("Predict"):
    input=np.array([[age,BMI,Menstrual_Irregularity,Testosterone_Level,Antral_Follicle_Count]])
    prediction=model.predict(input)
    if prediction[0]==1:
        st.write("You are at a high risk of having PCOS please consult the doctor")
    else:
        st.write("You have low chances of having PCOS")
import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app predicts the price of a house based on various features such as the number of bedrooms, bathrooms, living area, condition of the house, and number of views.")

st.divider()

# Input features
bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=0)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=0)
living_area = st.number_input("Living Area (sq ft)", min_value=0, value=2000)
condition = st.number_input("Condition of the House", min_value=0, value=3)
Number_of_schools_nearby = st.number_input("Number of Schools Nearby", min_value=0, value=0)

st.divider()

X = [[bedrooms, bathrooms, living_area, condition, Number_of_schools_nearby]]

predictbutton = st.button("Predict Price!")

if predictbutton:

    st.balloons()

    x_array = np.array(X)

    prediction = model.predict(x_array)[0]

    st.write(f"Predicted House Price is  €{prediction:,.2f}")

else:
    st.write("Please click the 'Predict Price' button to see the predicted house price.")

# To run this app, use the command: streamlit run app.py
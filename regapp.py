import streamlit as st
import pickle
import numpy as np

# Load model
with open("decision_tree_regressor.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("California House Price Prediction")

# Inputs
MedInc = st.number_input("Median Income", value=5.0)
HouseAge = st.number_input("House Age", value=20.0)
AveRooms = st.number_input("Average Rooms", value=5.0)
AveBedrms = st.number_input("Average Bedrooms", value=1.0)
Population = st.number_input("Population", value=1000.0)
AveOccup = st.number_input("Average Occupancy", value=3.0)
Latitude = st.number_input("Latitude", value=37.0)
Longitude = st.number_input("Longitude", value=-122.0)

# Prediction button
if st.button("Predict House Price"):

    input_data = np.array([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude
    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: {prediction[0]:.2f}$")
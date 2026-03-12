import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("classification_model.pkl")
reg = joblib.load("radius_model.pkl")

st.title("Stellar Analytics – Exoplanet Detection")

st.write("Predict whether a signal corresponds to a confirmed exoplanet.")

koi_period = st.number_input("Orbital Period", value=10.0)
koi_depth = st.number_input("Transit Depth", value=500.0)
koi_model_snr = st.number_input("Signal to Noise Ratio", value=20.0)
koi_impact = st.number_input("Impact Parameter", value=0.5)
koi_num_transits = st.number_input("Number of Transits", value=5)

input_data = pd.DataFrame({
    "koi_period":[koi_period],
    "koi_depth":[koi_depth],
    "koi_model_snr":[koi_model_snr],
    "koi_impact":[koi_impact],
    "koi_num_transits":[koi_num_transits]
})

if st.button("Predict"):

    planet_prediction = clf.predict(input_data)[0]
    radius_prediction = reg.predict(input_data)[0]

    if planet_prediction == 1:
        st.success("Confirmed Exoplanet")
    else:
        st.error("False Positive")

    st.write("Predicted Planet Radius:", round(radius_prediction,2))

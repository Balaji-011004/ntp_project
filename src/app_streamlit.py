import streamlit as st
import tensorflow as tf
import numpy as np

st.title("Network Traffic Prediction")

# Load trained model
model = tf.keras.models.load_model("models/lstm_model.h5")

traffic_input = st.number_input("Enter Traffic Value")

if st.button("Predict"):
    data = np.array([[traffic_input]])
    prediction = model.predict(data)

    st.write("Predicted Traffic:", prediction)
# app.py

import streamlit as st
import requests

st.set_page_config(page_title="Spam Detector", page_icon="📩")

st.title("📩 Spam Message Classifier")
st.markdown("This app helps you detect whether a message is **Spam** or **Not Spam**.")

# Text input
message = st.text_area("Enter your message:")

# Prediction button
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        # Send POST request to the FastAPI backend
        response = requests.post(
            "https://spam-detector-q252.onrender.com/predict",
            json={"message": message}
        )

        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            st.success(f"The message is: **{prediction.upper()}**")
        else:
            st.error("Something went wrong. Please try again later.")

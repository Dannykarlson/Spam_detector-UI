#app.py
import streamlit as st
import requests

st.set_page_config(page_title="Spam Detector", page_icon="📩")

# Initialize logged_in state if it doesn't exist
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.title("Login to Spam Detector")
    
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    
    login_button = st.button("Login")
    
    if login_button:
        if username == "admin" and password == "1234":
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Invalid username or password")

def main_app():
    st.title("📩 Spam Message Classifier")
    st.markdown("This app helps you detect whether a message is **Spam** or **Not Spam**.")

    message = st.text_area("Enter your message:")

    if st.button("Predict"):
        if message.strip() == "":
            st.warning("Please enter a message to classify.")
        else:
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

# Show login or app based on logged_in state
if st.session_state['logged_in']:
    main_app()
else:
    login()

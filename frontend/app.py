import streamlit as st
import requests

st.title("Message Fetcher")

if st.button("Get Message"):
    response = requests.get("http://127.0.0.1:8000/api/message")
    data = response.json()
    
    st.write(f"Status: {data['statut']}")
    st.write(f"Message: {data['message']}")


import streamlit as st
import requests

st.title("Message Fetcher")

if st.button("Get Message"):
    response = requests.get("http://127.0.0.1:8000/api/message")
    data = response.json()
    
    st.write(f"Status: {data['statut']}")
    st.write(f"Message: {data['message']}")

user_input = st.text_input("Message:")

if st.button("Envoyer"):
    requests.post("http://127.0.0.1:8000/api/message", params={"message": user_input})
    st.rerun()

response = requests.get("http://127.0.0.1:8000/api/messages")
messages = response.json()["messages"]

st.subheader("Messages reçus du backend :")
for msg in messages:
    st.write(msg)
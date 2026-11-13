
import streamlit as st
from groq import Groq

st.set_page_config(page_title="EMMA AI")
st.title("EMMA AI")
st.write("Bonjour Boss, pose-moi ta question !")

api_key = st.text_input("Mets ta cle Groq ici", type="password")
question = st.text_input("Ta question :")

if st.button("Demander") and api_key and question:
    client = Groq(api_key=api_key)
    reponse = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": question}]
    )
    st.write(reponse.choices[0].message.content)

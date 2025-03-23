import streamlit as st
from transformers import pipeline

# Cargar un modelo ligero de Hugging Face
modelo = pipeline("text-generation", model="distilgpt2")

# Interfaz en Streamlit
st.title("📚 Chatbot con Modelo Ligero")
st.write("Escribe una pregunta y te responderé usando IA.")

# Entrada del usuario
pregunta = st.text_input("Pregunta:")

# Botón para generar respuesta
if st.button("Responder"):
    respuesta = modelo(pregunta, max_length=50, do_sample=True)
    st.write("🤖 **Asistente:**", respuesta[0]["generated_text"])

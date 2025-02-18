import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Mi Aplicación Streamlit Básica")

st.write("Nombre: Hadith")
st.write("Matrícula: 123456789")
st.write("Correo: hadith024@gmail.com")

image = Image.open("thw.png")
st.image(image, caption="Credencial", use_column_width=True)

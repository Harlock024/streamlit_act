import streamlit as st
import pandas as pd


st.title("DASHBOARD")
st.header("Streamlit App")


def bienvenido(name):
    return f"Bienvenido, {name}!"


@st.cache_data
def load_data(nrows=1000):
    file_path = "dataset.csv"
    return pd.read_csv(file_path, nrows=nrows)


name = st.text_input("Nombre:")
if name:
    st.write(bienvenido(name))


data = load_data()


st.subheader("Datos Originales")
st.dataframe(data)

selected_sex = st.selectbox("Selecciona el sexo:", data["sex"].unique())


filtered_data = data[data["sex"] == selected_sex]


st.subheader(f"Datos filtrados por sexo: {selected_sex}")
st.dataframe(filtered_data)


st.subheader("Resumen de datos filtrados")
st.write(filtered_data.describe())

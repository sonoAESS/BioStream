import streamlit as st
import requests

API_URL = "http://localhost:8000/api/secuencias/"

st.title("Gestión de Secuencias Biológicas")

# Formulario para ingresar nueva secuencia
with st.form("form_sec"):
    nombre = st.text_input("Nombre de la secuencia")
    tipo = st.selectbox("Tipo de secuencia", ["ADN", "ARN", "Proteina"])
    secuencia = st.text_area("Secuencia")
    descripcion = st.text_area("Descripción (opcional)")
    submitted = st.form_submit_button("Guardar secuencia")

if submitted:
    data = {
        "nombre": nombre,
        "tipo": tipo,
        "secuencia": secuencia,
        "descripcion": descripcion
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        st.success("Secuencia guardada correctamente")
    else:
        st.error(f"Error al guardar: {response.text}")

# Mostrar lista de secuencias existentes
if st.button("Cargar secuencias"):
    response = requests.get(API_URL)
    if response.status_code == 200:
        secuencias = response.json()
        for s in secuencias:
            st.write(f"**{s['nombre']}** ({s['tipo']}): {s['secuencia']}")
    else:
        st.error("Error al cargar secuencias")

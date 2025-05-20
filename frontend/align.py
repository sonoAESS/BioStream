import streamlit as st
import requests

def align():
    API_URL = "http://localhost:8000/api/secuencias/alinear/"

    st.title("Alineamiento de dos secuencias")

    seq1 = st.text_area("Secuencia 1")
    seq2 = st.text_area("Secuencia 2")

    if st.button("Alinear"):
        if seq1 and seq2:
            try:
                response = requests.post(API_URL, json={"seq1": seq1, "seq2": seq2})
                if response.status_code == 200:
                    data = response.json()
                    st.text_area("Resultado del alineamiento", data['alineamiento'], height=200)
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Error de conexión: {e}")
        else:
            st.warning("Por favor ingresa ambas secuencias")

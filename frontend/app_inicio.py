import streamlit as st
import requests

def app_inicio():
    API_URL = "http://localhost:8000/api/secuencias/"

    st.title("Gestión de Secuencias Biológicas")

    # Estado para guardar la secuencia creada y su id
    if "seq_guardada" not in st.session_state:
        st.session_state.seq_guardada = None  # guardará dict con la secuencia

    # Pestañas para separar carga y operaciones
    tab_carga, tab_operaciones = st.tabs(["Cargar Secuencia", "Operaciones"])

    with tab_carga:
        st.header("Cargar nueva secuencia")
        with st.form("form_sec"):
            nombre = st.text_input("Nombre de la secuencia")
            tipo = st.selectbox("Tipo de secuencia", ["ADN", "ARN", "Proteina"])
            secuencia = st.text_area("Secuencia")
            descripcion = st.text_area("Descripción (opcional)")
            submitted = st.form_submit_button("Guardar secuencia")

        if submitted:
            if not nombre or not secuencia:
                st.error("Por favor completa el nombre y la secuencia")
            else:
                data = {
                    "nombre": nombre,
                    "tipo": tipo,
                    "secuencia": secuencia,
                    "descripcion": descripcion
                }
                response = requests.post(API_URL, json=data)
                if response.status_code == 201:
                    st.success("Secuencia guardada correctamente")
                    st.session_state.seq_guardada = response.json()
                    # Cambiar a pestaña operaciones automáticamente
                    st.rerun()
                else:
                    st.error(f"Error al guardar: {response.text}")

    with tab_operaciones:
        if st.session_state.seq_guardada is None:
            st.info("Primero debes cargar una secuencia en la pestaña 'Cargar Secuencia'")
        else:
            sec = st.session_state.seq_guardada
            st.header(f"Operaciones para secuencia: {sec['nombre']} ({sec['tipo']})")
            st.write(f"Secuencia: {sec['secuencia']}")

            # Solo ADN y ARN pueden tener reverso complementario y traducción
            if sec['tipo'] in ["ADN", "ARN"]:
                if st.button("Obtener reverso complementario"):
                    url = f"{API_URL}{sec['id']}/reverso_complementario/"
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            data = response.json()
                            st.success(f"Reverso complementario: {data['reverso_complementario']}")
                        else:
                            st.error(f"Error: {response.status_code} - {response.text}")
                    except Exception as e:
                        st.error(f"Error de conexión: {e}")

                if st.button("Traducir secuencia"):
                    url = f"{API_URL}{sec['id']}/traducir_seq/"
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            data = response.json()
                            st.success(f"Traducción: {data['traduction']}")
                        else:
                            st.error(f"Error: {response.status_code} - {response.text}")
                    except Exception as e:
                        st.error(f"Error de conexión: {e}")
            else:
                st.info("Para secuencias de proteínas no hay operaciones disponibles por ahora.")

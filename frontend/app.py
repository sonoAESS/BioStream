# app.py
import streamlit as st
from app_inicio import app_inicio
from align import align  # Importa la página align

# Diccionario de páginas
paginas = {
    "Inicio": app_inicio,
    "Alineamiento": align
}

# Selector de página en sidebar
pagina_seleccionada = st.sidebar.selectbox(
    "Navegar a",
    list(paginas.keys()),
    index=0  # selecciona la primera opción por defecto
)

# Ejecutar la función correspondiente a la página seleccionada
paginas[pagina_seleccionada]()

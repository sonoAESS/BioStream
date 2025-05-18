# BioStream

BioStream es una aplicación para el análisis y gestión de secuencias biológicas, desarrollada con Django (API REST) para el backend y Streamlit para el frontend. Permite almacenar, editar y analizar secuencias de ADN, ARN y proteínas, integrando funcionalidades básicas como reverso complementario y traducción.

---

## Características principales

- Gestión de secuencias biológicas (crear, listar, editar, eliminar).
- Funciones bioinformáticas básicas con Biopython (reverso complementario, traducción).
- API REST construida con Django REST Framework.
- Interfaz web interactiva con Streamlit que consume la API.
- Arquitectura modular y contenerizada para facilitar desarrollo y despliegue.

---

## Requisitos

- Python 3.9 o superior
- Django
- Django REST Framework
- Biopython
- Streamlit
- Requests (para consumo de API desde Streamlit)

---

## Instalación y configuración

1. Clonar el repositorio:
```
git clone https://github.com/tu_usuario/BioStream.git
cd BioStream
```
1. Crear y activar entorno virtual:
```
python -m venv env
source env/bin/activate # Linux/Mac
```
o
```
env\Scripts\activate # Windows
```

1. Instalar dependencias backend:
```
pip install -r backend/requirements.txt
```

1. Ejecutar migraciones:
```
cd backend
python manage.py makemigrations
python manage.py migrate
```
1. (Opcional) Crear superusuario para panel admin:
```
python manage.py createsuperuser
```

1. Ejecutar servidor Django:
```
python manage.py runserver
```
1. En otra terminal, instalar dependencias frontend y ejecutar Streamlit:

```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```
---

## Uso

- Accede a la API en `http://localhost:8000/api/secuencias/` para gestionar secuencias vía REST.
- Usa la interfaz Streamlit en `http://localhost:8501` para interactuar de forma visual e intuitiva.
- Desde Streamlit puedes crear nuevas secuencias, ver las existentes y ejecutar análisis básicos.

---

## Estructura del proyecto
```
BioStream/
│
├── backend/ # Proyecto Django (API)
│ ├── manage.py
│ ├── api/ # App principal con modelos, vistas y serializers
│ ├── backend/ # Configuración Django
│ └── requirements.txt
│
├── frontend/ # Proyecto Streamlit (frontend)
│ ├── app.py
│ ├── requirements.txt
│ └── ...
│
├── README.md
└── ...
```
---

## Próximas mejoras

- Implementar importación y exportación de archivos FASTA.
- Añadir alineamiento múltiple con integración de Clustal Omega o MUSCLE.
- Incorporar búsquedas BLAST y visualización avanzada.
- Contenerización con Docker y despliegue en la nube.
- Tests unitarios y funcionales para backend y frontend.

---

## Contacto

Para dudas, sugerencias o contribuciones, puedes contactarme en:

- Email: eliasyosoto@gmail.com  
- GitHub: https://github.com/sonoAESS

---

¡Gracias por usar BioStream!
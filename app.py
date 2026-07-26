# ==========================================================
# PROYECTO 1 - STREAMLIT
# Autor: Jhon Doe
# Módulo: Python + Streamlit
# ==========================================================

# ----------------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# ----------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np

# Librerías proporcionadas para el proyecto
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc


# ----------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ----------------------------------------------------------

st.set_page_config(
    page_title="DMC Proyecto Mod 1",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ----------------------------------------------------------
# MENÚ LATERAL
# ----------------------------------------------------------

st.sidebar.title("Aplicación en Streamlit")

st.sidebar.markdown("---")

opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    (
        "Home",
        "Ejercicio 1",
        "Ejercicio 2",
        "Ejercicio 3",
        "Ejercicio 4"
    )
)

st.sidebar.markdown("---")

st.sidebar.success("Python • NumPy • Pandas • Streamlit")


# ----------------------------------------------------------
# VARIABLES DE SESIÓN
# ----------------------------------------------------------

# ---------- Ejercicio 1 ----------

if "movimientos" not in st.session_state:
    st.session_state.movimientos = []


# ---------- Ejercicio 2 ----------

if "productos" not in st.session_state:
    st.session_state.productos = np.array([], dtype=object)

if "categorias" not in st.session_state:
    st.session_state.categorias = np.array([], dtype=object)

if "precios" not in st.session_state:
    st.session_state.precios = np.array([], dtype=float)

if "cantidades" not in st.session_state:
    st.session_state.cantidades = np.array([], dtype=int)

if "totales" not in st.session_state:
    st.session_state.totales = np.array([], dtype=float)


# ---------- Ejercicio 3 ----------

if "historial_funciones" not in st.session_state:
    st.session_state.historial_funciones = []


# ---------- Ejercicio 4 ----------

if "registros_crud" not in st.session_state:
    st.session_state.registros_crud = []


# ==========================================================
# HOME
# ==========================================================

if opcion == "Home":

    st.title("DMC PROYECTO 1")
    st.subheader("Aplicación desarrollada con Streamlit")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:

        # Reemplazar por una imagen propia
        st.image("Python_logo.png", width=440)
        st.image("DMC.png", width=330)

    with col2:

        st.markdown("## Información del estudiante")

        st.write("**Nombre:** Nick Dante Flores Pérez")

        st.write("**Módulo:** Python con Streamlit")

        st.write("**Carrera:** Ingeniería Electrónica")
        
        st.write("**Institución:** DMC")

        st.write("**Año:** 2026")

    st.markdown("---")

    st.header("Descripción")

    st.markdown(
        """
Esta aplicación integra los conocimientos adquiridos durante el módulo de Python.

En el proyecto se desarrollan cuatro ejercicios donde se utilizan:

- Listas
- NumPy
- Pandas
- Funciones
- Clases
- Programación Orientada a Objetos
- CRUD
- Streamlit
"""
    )

    st.markdown("---")

    st.header("Tecnologías utilizadas")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Lenguaje", "Python")

    with c2:
        st.metric("Framework", "Streamlit")

    with c3:
        st.metric("Datos", "Pandas")

    with c4:
        st.metric("Arreglos", "NumPy")

    st.markdown("---")

    st.success(
        "Seleccione uno de los ejercicios desde el menú lateral para comenzar."
    )

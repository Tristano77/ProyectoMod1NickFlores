
import streamlit as st
import pandas as pd
import numpy as np
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
# EJERCICIO 1
# FLUJO DE CAJA CON LISTAS
# ==========================================================

def ejercicio1():

    st.title("💰 Ejercicio 1 - Flujo de Caja")

    st.markdown("""
    ### Descripción

    En este ejercicio se registran movimientos financieros utilizando una **lista**.
    Cada movimiento corresponde a un ingreso o un gasto y posteriormente se calcula
    el saldo del flujo de caja.
    """)

    st.divider()

    # ------------------------------------------------------
    # FORMULARIO
    # ------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        concepto = st.text_input(
            "Concepto",
            placeholder="Ejemplo: Compra de repuestos"
        )

        tipo = st.selectbox(
            "Tipo de movimiento",
            (
                "Ingreso",
                "Gasto"
            )
        )

    with col2:

        valor = st.number_input(
            "Valor",
            min_value=0.0,
            step=10.0,
            format="%.2f"
        )

    st.write("")

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # BOTÓN AGREGAR
    # ------------------------------------------------------

    with col1:

        if st.button(
            "➕ Agregar movimiento",
            use_container_width=True
        ):

            if concepto.strip() == "":

                st.warning("Ingrese un concepto.")

            elif valor <= 0:

                st.warning("El valor debe ser mayor que cero.")

            else:

                movimiento = {

                    "Concepto": concepto,

                    "Tipo": tipo,

                    "Valor": valor

                }

                st.session_state.movimientos.append(
                    movimiento
                )

                st.success("Movimiento agregado correctamente.")

    # ------------------------------------------------------
    # BOTÓN LIMPIAR
    # ------------------------------------------------------

    with col2:

        if st.button(
            "🗑 Limpiar registros",
            use_container_width=True
        ):

            st.session_state.movimientos = []

            st.success("Registros eliminados.")

    st.divider()

    # ------------------------------------------------------
    # TABLA
    # ------------------------------------------------------

    if len(st.session_state.movimientos) == 0:

        st.info("No existen movimientos registrados.")

    else:

        df = pd.DataFrame(
            st.session_state.movimientos
        )

        st.subheader("Movimientos registrados")

        st.dataframe(
            df,
            use_container_width=True
        )

        # --------------------------------------------------
        # CÁLCULOS
        # --------------------------------------------------

        ingresos = df[
            df["Tipo"] == "Ingreso"
        ]["Valor"].sum()

        gastos = df[
            df["Tipo"] == "Gasto"
        ]["Valor"].sum()

        saldo = ingresos - gastos

        total_movimientos = len(df)

        st.divider()

        st.subheader("Resumen")

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Ingresos",
                f"S/. {ingresos:,.2f}"
            )

        with c2:

            st.metric(
                "Gastos",
                f"S/. {gastos:,.2f}"
            )

        with c3:

            st.metric(
                "Saldo",
                f"S/. {saldo:,.2f}"
            )

        with c4:

            st.metric(
                "Movimientos",
                total_movimientos
            )

        st.divider()

        # --------------------------------------------------
        # ESTADO
        # --------------------------------------------------

        if saldo > 0:

            st.success(
                "✅ El flujo de caja se encuentra A FAVOR."
            )

        elif saldo == 0:

            st.warning(
                "⚠ El flujo de caja se encuentra equilibrado."
            )

        else:

            st.error(
                "❌ El flujo de caja se encuentra EN CONTRA."
            )

        # --------------------------------------------------
        # INFORMACIÓN ADICIONAL
        # --------------------------------------------------

        with st.expander("Ver estadísticas"):

            st.write(
                f"Cantidad de ingresos: {(df['Tipo']=='Ingreso').sum()}"
            )

            st.write(
                f"Cantidad de gastos: {(df['Tipo']=='Gasto').sum()}"
            )

            st.write(
                f"Valor promedio por movimiento: S/. {df['Valor'].mean():,.2f}"
            )

            st.write(
                f"Movimiento máximo: S/. {df['Valor'].max():,.2f}"
            )

            st.write(
                f"Movimiento mínimo: S/. {df['Valor'].min():,.2f}"
            )



# ==========================================================
# HOME
# ==========================================================

if opcion == "Home":

    st.title("DMC PROYECTO MODULO 1")
    st.subheader("Aplicación desarrollada con Streamlit")

    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image("Python_logo.png", width=440)
        st.image("DMC.png", width=330)

    with col2:

        st.markdown("## Datos personales")

        st.write("**Nombre:** Nick Dante Flores Pérez")

        st.write("**About me:** Ingeniero Electrónico con especialidad en instrumentación y control de procesos.")

        st.write("**Módulo:** Python con Streamlit")
        
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
elif opcion == "Ejercicio 1":

    ejercicio1()
    

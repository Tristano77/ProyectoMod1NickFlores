
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

if "equipos_crud" not in st.session_state:
    st.session_state.equipos_crud = []


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
# EJERCICIO 2
# REGISTRO DE PRODUCTOS CON NUMPY
# ==========================================================

def ejercicio2():

    st.title("📦 Ejercicio 2 - Registro con NumPy")

    st.markdown("""
    ### Descripción

    Este ejercicio registra productos utilizando **arreglos de NumPy**.
    Cada nuevo producto se almacena en los arrays y posteriormente se
    construye un **DataFrame de Pandas** para visualizar la información.
    """)

    st.divider()

    # ------------------------------------------------------
    # FORMULARIO
    # ------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        producto = st.text_input(
            "Nombre del producto",
            placeholder="Ejemplo: Disco de freno"
        )

        categoria = st.selectbox(
            "Categoría",
            (
                "Repuestos",
                "Herramientas",
                "Lubricantes",
                "Seguridad",
                "Consumibles",
                "Otros"
            )
        )

    with col2:

        precio = st.number_input(
            "Precio Unitario",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )

        cantidad = st.number_input(
            "Cantidad",
            min_value=1,
            step=1
        )

    total = precio * cantidad

    st.info(f"Total del registro : S/. {total:,.2f}")

    st.write("")

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # BOTÓN AGREGAR
    # ------------------------------------------------------

    with col1:

        if st.button(
            "➕ Agregar producto",
            use_container_width=True
        ):

            if producto.strip() == "":

                st.warning("Debe ingresar un producto.")

            else:

                st.session_state.productos = np.append(
                    st.session_state.productos,
                    producto
                )

                st.session_state.categorias = np.append(
                    st.session_state.categorias,
                    categoria
                )

                st.session_state.precios = np.append(
                    st.session_state.precios,
                    precio
                )

                st.session_state.cantidades = np.append(
                    st.session_state.cantidades,
                    cantidad
                )

                st.session_state.totales = np.append(
                    st.session_state.totales,
                    total
                )

                st.success("Producto agregado correctamente.")

    # ------------------------------------------------------
    # LIMPIAR
    # ------------------------------------------------------

    with col2:

        if st.button(
            "🗑 Limpiar productos",
            use_container_width=True
        ):

            st.session_state.productos = np.array([], dtype=object)

            st.session_state.categorias = np.array([], dtype=object)

            st.session_state.precios = np.array([], dtype=float)

            st.session_state.cantidades = np.array([], dtype=int)

            st.session_state.totales = np.array([], dtype=float)

            st.success("Registros eliminados.")

    st.divider()

    # ------------------------------------------------------
    # DATAFRAME
    # ------------------------------------------------------

    if len(st.session_state.productos) == 0:

        st.info("No existen productos registrados.")

        return

    df = pd.DataFrame({

        "Producto": st.session_state.productos,

        "Categoría": st.session_state.categorias,

        "Precio": st.session_state.precios,

        "Cantidad": st.session_state.cantidades,

        "Total": st.session_state.totales

    })

    st.subheader("Inventario registrado")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------------
    # MÉTRICAS
    # ------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Productos",
            len(df)
        )

    with c2:

        st.metric(
            "Cantidad Total",
            int(df["Cantidad"].sum())
        )

    with c3:

        st.metric(
            "Precio Promedio",
            f"S/. {df['Precio'].mean():,.2f}"
        )

    with c4:

        st.metric(
            "Valor Inventario",
            f"S/. {df['Total'].sum():,.2f}"
        )

    st.divider()

    # ------------------------------------------------------
    # ESTADÍSTICAS
    # ------------------------------------------------------

    with st.expander("📈 Estadísticas"):

        st.write(
            f"Producto más costoso : **{df.loc[df['Precio'].idxmax(),'Producto']}**"
        )

        st.write(
            f"Producto más económico : **{df.loc[df['Precio'].idxmin(),'Producto']}**"
        )

        st.write(
            f"Cantidad promedio : **{df['Cantidad'].mean():.2f}**"
        )

        st.write(
            f"Venta promedio : **S/. {df['Total'].mean():,.2f}**"
        )

        categoria_mayor = (
            df.groupby("Categoría")["Total"]
            .sum()
            .sort_values(ascending=False)
        )

        st.subheader("Ventas por categoría")

        st.dataframe(categoria_mayor)

        st.subheader("Resumen estadístico")

        st.dataframe(
            df.describe(include="all")
        )

# ==========================================================
# EJERCICIO 3
# FUNCIONES DE LA LIBRERÍA EXTERNA
# ==========================================================

def ejercicio3():

    st.title("⚙ Ejercicio 3 - Indicadores de Mantenimiento")

    st.markdown("""
    ### Descripción

    Este ejercicio utiliza funciones de la librería
    **libreria_funciones_proyecto1.py**.

    Primero se calculan:

    - MTBF (Mean Time Between Failure) Tiempo medio entre fallas
    - MTTR (Mean Time to Repair) Tiemp medio entre reparaciones
    - Disponibilidad

    Posteriormente, utilizando la disponibilidad calculada,
    se determina el **OEE** (Overall Equipment Effectiveness) del equipo.
    """)

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        horas_operacion = st.number_input(
            "Horas de operación",
            min_value=1.0,
            value=500.0
        )

        numero_fallas = st.number_input(
            "Número de fallas",
            min_value=1,
            value=5
        )

    with col2:

        horas_reparacion = st.number_input(
            "Horas de reparación",
            min_value=0.0,
            value=18.0
        )

        rendimiento = st.slider(
            "Rendimiento (%)",
            0.0,
            100.0,
            95.0
        )

    calidad = st.slider(
        "Calidad (%)",
        0.0,
        100.0,
        98.0
    )

    st.divider()

    if st.button(
        "Calcular Indicadores",
        use_container_width=True
    ):

        try:

            indicadores = lf.calcular_indicadores_mantenimiento(

                horas_operacion,

                numero_fallas,

                horas_reparacion

            )

            oee = lf.calcular_oee(

                indicadores["disponibilidad_pct"],

                rendimiento,

                calidad

            )

            mtbf = indicadores["mtbf_h"]

            mttr = indicadores["mttr_h"]

            disponibilidad = indicadores["disponibilidad_pct"]

            oee_final = oee["oee_pct"]

            st.subheader("Resultados")

            c1,c2,c3,c4 = st.columns(4)

            with c1:

                st.metric(
                    "MTBF",
                    f"{mtbf:.2f} h"
                )

            with c2:

                st.metric(
                    "MTTR",
                    f"{mttr:.2f} h"
                )

            with c3:

                st.metric(
                    "Disponibilidad",
                    f"{disponibilidad:.2f}%"
                )

            with c4:

                st.metric(
                    "OEE",
                    f"{oee_final:.2f}%"
                )

           #--------------------------
            
            #--------
            st.divider()

            st.subheader("Diagnóstico")

            if disponibilidad >=95:

                st.success(
                    "Excelente disponibilidad."
                )

            elif disponibilidad>=85:

                st.warning(
                    "Disponibilidad aceptable."
                )

            else:

                st.error(
                    "Disponibilidad baja."
                )

            if oee_final>=85:

                st.success(
                    "OEE de clase mundial."
                )

            elif oee_final>=60:

                st.warning(
                    "OEE aceptable."
                )

            else:

                st.error(
                    "OEE bajo."
                )
            registro = {
        
            "Ejecución": len(st.session_state.historial_funciones)+1,
        
            "Horas Operación": horas_operacion,
        
            "Fallas": numero_fallas,
        
            "Horas Reparación": horas_reparacion,
        
            "MTBF": mtbf,
        
            "MTTR": mttr,
        
            "Disponibilidad": disponibilidad,
        
            "Rendimiento": rendimiento,
        
            "Calidad": calidad,
        
            "OEE": oee_final

            }

            st.session_state.historial_funciones.append(
                registro
            )

        except Exception as e:

            st.error(e)
    if len(st.session_state.historial_funciones)>0:

        st.divider()

        st.subheader("Histórico")

        historial = pd.DataFrame(
            st.session_state.historial_funciones
        )

        st.dataframe(
            historial,
            use_container_width=True
        )
        st.subheader("Histórico de Disponibilidad y OEE")
        
        fig, ax = plt.subplots(figsize=(10,5))
        
        ax.plot(
            historial["Ejecución"],
            historial["Disponibilidad"],
            marker="o",
            linewidth=2,
            label="Disponibilidad"
        )
        
        ax.plot(
            historial["Ejecución"],
            historial["OEE"],
            marker="s",
            linewidth=2,
            label="OEE"
        )
        
        ax.set_xlabel("Ejecución")
        
        ax.set_ylabel("Porcentaje (%)")
        
        ax.set_title("Evolución de Indicadores")
        
        ax.set_ylim(0,100)
        
        ax.grid(True)
        
        ax.legend()
        
        st.pyplot(fig)
        col1,col2 = st.columns(2)

        with col1:

            csv = historial.to_csv(index=False)

            st.download_button(

                "📥 Descargar CSV",

                csv,

                "historial_mantenimiento.csv",

                "text/csv"

            )

        with col2:

            if st.button(
                "🗑 Limpiar historial"
            ):

                st.session_state.historial_funciones=[]

                st.rerun()

# ==========================================================
# EJERCICIO 4
# CRUD CON CLASES
# ==========================================================

def ejercicio4():

    st.title("🛠 Ejercicio 4 - CRUD de Equipos de Mantenimiento")

    st.markdown("""
    ### Descripción

    Este ejercicio utiliza la clase **EquipoMantenimiento**
    de la librería externa.

    Se implementan las operaciones CRUD:

    - Crear
    - Leer
    - Actualizar
    - Eliminar

    utilizando Programación Orientada a Objetos.
    """)

    tabs = st.tabs([
        "➕ Crear",
        "📋 Consultar",
        "✏ Actualizar",
        "🗑 Eliminar"
    ])
    # =====================================================
    # CREAR
    # =====================================================

    with tabs[0]:

        st.subheader("Registrar nuevo equipo")

        nombre = st.text_input(
            "Nombre del equipo"
        )

        col1,col2,col3 = st.columns(3)

        with col1:

            horas = st.number_input(
                "Horas de operación",
                min_value=1.0,
                value=500.0,
                key="crear_horas"
            )

        with col2:

            fallas = st.number_input(
                "Número de fallas",
                min_value=1,
                value=5,
                key="crear_fallas"
            )

        with col3:

            reparacion = st.number_input(
                "Horas de reparación",
                min_value=0.0,
                value=20.0,
                key="crear_rep"
            )

        if st.button(
            "Guardar Equipo",
            use_container_width=True
        ):

            try:

                equipo = lc.EquipoMantenimiento(
            
                    nombre,
                
                    horas,
                
                    fallas,
                
                    reparacion
            
                )
                
                registro = equipo.resumen()
                
                # Guardamos también los datos originales
                
                registro["horas_operacion"] = horas
                
                registro["numero_fallas"] = fallas
                
                registro["horas_reparacion"] = reparacion
                
                st.session_state.equipos_crud.append(registro)
    
                st.success("Equipo registrado correctamente.")

            except Exception as e:

                st.error(e)
    # =====================================================
    # CONSULTAR
    # =====================================================

    with tabs[1]:

        st.subheader("Equipos registrados")

        if len(st.session_state.equipos_crud)==0:

            st.info(
                "No existen registros."
            )

        else:

            df = pd.DataFrame(st.session_state.equipos_crud)
            
            # Ordenar columnas
            df = df[
                [
                    "equipo",
                    "horas_operacion",
                    "numero_fallas",
                    "horas_reparacion",
                    "mtbf_h",
                    "mttr_h",
                    "disponibilidad_pct"
                ]
            ]
            
            # Cambiar nombres de columnas
            df = df.rename(columns={
                "equipo": "Equipo",
                "horas_operacion": "Horas Operación (h)",
                "numero_fallas": "N° Fallas",
                "horas_reparacion": "Horas Reparación (h)",
                "mtbf_h": "MTBF (h)",
                "mttr_h": "MTTR (h)",
                "disponibilidad_pct": "Disponibilidad (%)"
            })
            
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )
    # =====================================================
    # ACTUALIZAR
    # =====================================================
    
    with tabs[2]:
    
        st.subheader("Actualizar Equipo")
    
        if len(st.session_state.equipos_crud) == 0:
    
            st.info("No existen registros para actualizar.")
    
        else:
    
            df = pd.DataFrame(st.session_state.equipos_crud)
    
            indice = st.selectbox(
                "Seleccione el equipo",
                df.index,
                format_func=lambda x: df.loc[x, "equipo"]
            )
    
            nombre = st.text_input(
                "Nombre",
                value=df.loc[indice, "equipo"],
                key="upd_nombre"
            )
    
            col1, col2, col3 = st.columns(3)
    
            with col1:
    
                horas = st.number_input(
                    "Horas de Operación",
                    min_value=1.0,
                    value=float(df.loc[indice, "horas_operacion"]),
                    key="upd_horas"
                )
    
            with col2:
    
                fallas = st.number_input(
                    "Número de Fallas",
                    min_value=1,
                    value=int(df.loc[indice, "numero_fallas"]),
                    key="upd_fallas"
                )
    
            with col3:
    
                reparacion = st.number_input(
                    "Horas de Reparación",
                    min_value=0.0,
                    value=float(df.loc[indice, "horas_reparacion"]),
                    key="upd_rep"
                )
    
            if st.button(
                "Actualizar",
                use_container_width=True
            ):
            
                try:
            
                    equipo = lc.EquipoMantenimiento(
            
                        nombre,
            
                        horas,
            
                        fallas,
            
                        reparacion
            
                    )
            
                    # Obtener el resumen calculado por la clase
                    registro = equipo.resumen()
            
                    # Agregar los datos originales del equipo
                    registro["horas_operacion"] = horas
                    registro["numero_fallas"] = fallas
                    registro["horas_reparacion"] = reparacion
            
                    # Actualizar el registro seleccionado
                    st.session_state.equipos_crud[indice] = registro
            
                    st.success("Equipo actualizado correctamente.")
            
                    st.rerun()
            
                except Exception as e:
            
                    st.error(f"Error al actualizar el equipo: {e}")
    # =====================================================
    # ELIMINAR
    # =====================================================

    with tabs[3]:

        st.subheader("Eliminar Equipo")

        if len(st.session_state.equipos_crud)==0:

            st.info("No existen registros.")

        else:

            df = pd.DataFrame(st.session_state.equipos_crud)

            indice = st.selectbox(

                "Equipo",

                df.index,

                format_func=lambda x: df.loc[x,"equipo"],

                key="delete"

            )

            st.write(df.loc[indice])

            if st.button(

                "Eliminar Equipo",

                type="primary",

                use_container_width=True

            ):

                st.session_state.equipos_crud.pop(indice)

                st.success("Registro eliminado.")

                st.rerun()
    # =====================================================
    # DASHBOARD
    # =====================================================

    if len(st.session_state.equipos_crud) > 0:

        df = pd.DataFrame(st.session_state.equipos_crud)

        st.divider()

        st.header("Dashboard de Mantenimiento")
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
        
            st.metric(
                "Equipos Registrados",
                len(df)
            )
        
        with c2:
        
            st.metric(
                "Horas Operación Totales",
                f"{df['horas_operacion'].sum():,.1f}"
            )
        
        with c3:
        
            st.metric(
                "Total de Fallas",
                int(df["numero_fallas"].sum())
            )
        
        c1, c2, c3 = st.columns(3)
        
        with c1:
        
            st.metric(
                "MTBF Promedio",
                f"{df['mtbf_h'].mean():.2f} h"
            )
        
        with c2:
        
            st.metric(
                "MTTR Promedio",
                f"{df['mttr_h'].mean():.2f} h"
            )
        
        with c3:
        
            st.metric(
                "Disponibilidad Promedio",
                f"{df['disponibilidad_pct'].mean():.2f}%"
            )
        st.divider()
  
        st.subheader("Indicadores de Mantenimiento por Equipo")
        
        fig, ax1 = plt.subplots(figsize=(10,5))
        
        # Disponibilidad (eje izquierdo)
        ax1.plot(
            df["equipo"],
            df["disponibilidad_pct"],
            marker="o",
            linewidth=2.5,
            label="Disponibilidad (%)"
        )
        
        ax1.set_ylabel("Disponibilidad (%)")
        ax1.set_ylim(0,100)
        ax1.set_xlabel("Equipo")
        ax1.grid(True, linestyle="--", alpha=0.5)
        
        # MTBF (eje derecho)
        ax2 = ax1.twinx()
        
        ax2.plot(
            df["equipo"],
            df["mtbf_h"],
            marker="s",
            linewidth=2.5,
            linestyle="--",
            label="MTBF (h)"
        )
        
        ax2.set_ylabel("MTBF (h)")
        ax2.set_ylim(
            0,
            df["mtbf_h"].max() * 1.15
        )
        # Leyenda
        lineas1, etiquetas1 = ax1.get_legend_handles_labels()
        lineas2, etiquetas2 = ax2.get_legend_handles_labels()
        
        ax1.legend(
            lineas1 + lineas2,
            etiquetas1 + etiquetas2,
            loc="upper left"
        )
        
        ax1.set_title("Comparación de Indicadores por Equipo")
        
        plt.xticks(rotation=20)
        
        fig.tight_layout()
        
        st.pyplot(fig)
        
        st.divider()

        csv = df.to_csv(index=False)

        st.download_button(

            "📥 Descargar Equipos CSV",

            csv,

            "equipos.csv",

            "text/csv",

            use_container_width=True

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

        st.markdown("## 👤 Información del Estudiante"")

        st.write("**Nombre:** Nick Dante Flores Pérez")

        st.write("**About me:** Ingeniero Electrónico con especialidad en instrumentación y control de procesos.")

        st.write("**Módulo:** Python con Streamlit")
        
        st.write("**Institución:** DMC")

        st.write("**Año:** 2026")

    st.markdown("---")

    st.header("📖 Descripción del Proyecto")

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
elif opcion == "Ejercicio 2":
    ejercicio2()
elif opcion == "Ejercicio 3":
    ejercicio3()
elif opcion == "Ejercicio 4":
    ejercicio4()

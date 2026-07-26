# app.py
import streamlit as st
import pandas as pd
import numpy as np
from libreria_funciones_proyecto1 import calcular_indicadores_mantenimiento
from librería_clases_proyecto1 import EquipoMantenimiento

st.set_page_config(page_title="Proyecto 1",layout="wide")
menu=st.sidebar.selectbox("Menú",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

for k,v in {
"movimientos":[],
"productos":np.array([],dtype=str),
"categorias":np.array([],dtype=str),
"precios":np.array([],dtype=float),
"cantidades":np.array([],dtype=int),
"totales":np.array([],dtype=float),
"historial":[],
"equipos":[]}.items():
    if k not in st.session_state: st.session_state[k]=v

if menu=="Home":
    st.title("Proyecto 1 - Streamlit")
    st.subheader("Jhon Doe")
    st.write("Ingeniería Electrónica")
    st.markdown("Aplicación que integra listas, NumPy, Pandas, funciones y clases.")
elif menu=="Ejercicio 1":
    st.title("Flujo de Caja")
    c=st.text_input("Concepto")
    t=st.selectbox("Tipo",["Ingreso","Gasto"])
    v=st.number_input("Valor",0.0)
    if st.button("Agregar"):
        st.session_state.movimientos.append({"Concepto":c,"Tipo":t,"Valor":v})
    df=pd.DataFrame(st.session_state.movimientos)
    st.dataframe(df)
    if not df.empty:
        ing=df[df.Tipo=="Ingreso"].Valor.sum();gas=df[df.Tipo=="Gasto"].Valor.sum();sal=ing-gas
        a,b,c=st.columns(3);a.metric("Ingresos",ing);b.metric("Gastos",gas);c.metric("Saldo",sal)
        st.success("A favor") if sal>=0 else st.error("En contra")
elif menu=="Ejercicio 2":
    st.title("Registro con NumPy")
    p=st.text_input("Producto");cat=st.selectbox("Categoría",["A","B","C"]);pre=st.number_input("Precio",0.0);cant=st.number_input("Cantidad",1,step=1)
    if st.button("Agregar registro"):
        ss=st.session_state
        ss.productos=np.append(ss.productos,p);ss.categorias=np.append(ss.categorias,cat)
        ss.precios=np.append(ss.precios,pre);ss.cantidades=np.append(ss.cantidades,cant);ss.totales=np.append(ss.totales,pre*cant)
    df=pd.DataFrame({"Producto":st.session_state.productos,"Categoría":st.session_state.categorias,"Precio":st.session_state.precios,"Cantidad":st.session_state.cantidades,"Total":st.session_state.totales})
    st.dataframe(df)
elif menu=="Ejercicio 3":
    st.title("Indicadores de Mantenimiento")
    h=st.number_input("Horas operación",1.0);f=st.number_input("Número fallas",1,step=1);r=st.number_input("Horas reparación",0.0)
    if st.button("Calcular"):
        try:
            res=calcular_indicadores_mantenimiento(h,int(f),r)
            st.write(res);st.session_state.historial.append(res)
        except Exception as e: st.error(e)
    st.dataframe(pd.DataFrame(st.session_state.historial))
else:
    st.title("CRUD Equipo Mantenimiento")
    tabs=st.tabs(["Crear","Leer","Actualizar","Eliminar"])
    with tabs[0]:
        n=st.text_input("Nombre");h=st.number_input("Horas",1.0,key="h");f=st.number_input("Fallas",1,key="f");r=st.number_input("Rep",0.0,key="r")
        if st.button("Crear"):
            try:
                st.session_state.equipos.append(EquipoMantenimiento(n,h,int(f),r).resumen())
            except Exception as e: st.error(e)
    with tabs[1]:
        st.dataframe(pd.DataFrame(st.session_state.equipos))
    with tabs[2]:
        if st.session_state.equipos:
            i=st.selectbox("Registro",range(len(st.session_state.equipos)))
            d=st.session_state.equipos[i]
            nn=st.text_input("Nombre",d["equipo"]);mh=st.number_input("MTBF base horas",1.0,key="uh");nf=st.number_input("Fallas",1,key="uf");hr=st.number_input("Rep",0.0,key="ur")
            if st.button("Actualizar"):
                st.session_state.equipos[i]=EquipoMantenimiento(nn,mh,int(nf),hr).resumen()
    with tabs[3]:
        if st.session_state.equipos:
            i=st.selectbox("Eliminar",range(len(st.session_state.equipos)),key="del")
            if st.button("Eliminar"):
                st.session_state.equipos.pop(i)

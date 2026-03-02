import streamlit as st
import pandas as pd

# Inicializar session state para almacenar los datos
if 'nombres' not in st.session_state:
    st.session_state.nombres = []
if 'apellidos' not in st.session_state:
    st.session_state.apellidos = []

# Inputs
nombre = st.text_input("Ingrese un nombre: ")
apellido = st.text_input("Ingrese el apellido: ")

# Botón para agregar
if st.button("Agregar"):
    if nombre and apellido:  # Solo agregar si ambos campos tienen contenido
        st.session_state.nombres.append(nombre)
        st.session_state.apellidos.append(apellido)
        st.success(f"Se agregó: {nombre} {apellido}")
    else:
        st.warning("Por favor ingrese ambos campos")

# Botón para limpiar todos los datos
if st.button("Limpiar todo"):
    st.session_state.nombres = []
    st.session_state.apellidos = []
    st.info("Todos los datos han sido eliminados")

# Mostrar el DataFrame con todos los datos acumulados
if st.session_state.nombres:
    dataframe = pd.DataFrame({
        'Nombres': st.session_state.nombres,
        'Apellidos': st.session_state.apellidos,
    })
    st.write(dataframe)
else:
    st.info("No hay datos para mostrar. Ingrese un nombre y apellido y haga clic en 'Agregar'.")
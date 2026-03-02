import streamlit as st
import pandas as pd

if 'lista_comidas' not in st.session_state:
    st.session_state.lista_comidas = []

comida = st.text_input("Ingrese su comida favorita", key = "comida")
nombre = st.text_input("Ingrese su nombre", key = "nombre")

if st.button("Agregar Comida"):
    if comida and comida not in st.session_state.lista_comidas:
        st.session_state.lista_comidas.append(comida)

dataframe = st.selectbox (
    
    "Las comidas que has ingresado son: ",
    (st.session_state.lista_comidas),
    index = None,
    accept_new_options = True,
    placeholder = "Aqui aparecerán tus comidas favoritas:",
)

df = pd.DataFrame ({
    
    'Nombre': [nombre],
    'Comida Favorita': [st.sessawion_state.comida],
})

st.write(df)

# Usar "==" es un operador de comparación, ":" define las claves del diccionario en Pandas.
# Cuando se crea una tabla se deben utilizar "[]" para crear la lista y que funcione.
# Append es un metodo que se utiliza para las listas en Python que AGREGA UN ELEMENTO AL FINAL DE LA LISTA.
# Not In es un operador de Python que verifica si un elemento NO esta dentro de una lista, tupla, conjunto o cadena. Devuelve TRUE si No esta, FALSE si está.
# st.session_state
import streamlit as st
import pandas as pd
import numpy as np

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["Tiempo", "Velocidad"])
    
st.header("Elije un color para los puntos")
color = st.color_picker("color", "#FF0000")

st.divider()

st.scatter_chart(st.session_state.df, x="Tiempo", y="Velocidad", color=color)

# Este archivo crea un DataFrame de forma aleatoria una sola vez y lo guarda en st.session_state.
# La condición con "if 'df' not in st.session_state:" verifica si el DataFrame ya existe en el st.session_state para evitar que se genere nuevamente en cada recarga.
# la parte de "st.session_state.df = pd.DataFrame(np.random.randn(20, 5), columns=["x", "y"])" crea un DataFrame con numero aleatorios con 20 filas, se etiquetan como "x" y "y" para el grafico.
# La sección de de "st.header('Elije un DataPoint Color)" muestra un titulo en la interfaz.
# En "color = st.color_picker('color', '"FF0000")" muestra un selector de color y guarda el color elegido.
# El "st.divider()" dibuja una linea divisora en la interfaz.
# La parte de "st.scatter_chart(se.session_state.df, x="Tiempo", y="Velocidad", color=color)" dibuja un gráficode dispersión usando las columnas X y Y de DataFrame y les aplica el color que seleccionamos.
import streamlit as st
import numpy as np

dataframe = np.random.randn(8, 8)
st.dataframe(dataframe)

# Numpy para generar una muestra aleatoria, pero se puede utilizar "Pandas DataFrame", "Matrices Numpy" o "Matrices  Python Simples".
# Genera numeros randoms donde el primer numero son las filas y el segundo numero son las columnas.
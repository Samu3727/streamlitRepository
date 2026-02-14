import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame (
    
    np.random.randn(10, 20),
    columns = ('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

# La línea de "np.random.randn(10, 20)" genera una matriz de 10 filas y 20 columnas.
# La línea "range(20))" genera numeros del 0 al 19, "'col %d' % i" es un formato de string que inserta el numero, "%d" es el placeholder para los numero enteros.
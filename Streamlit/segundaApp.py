import streamlit as st
import pandas as pd

st.write("Primer intento utilizando para crear una tabla en Streamlit en una tabla")
st.write(pd.DataFrame ({
    
    'Nombres': ["Juan", "Mateo", "Samuel", "Julian"],
    'Número Celular': [3159874562, 32547898547, 3054302025, 3224598745]
}))

# st.write funciona para hacer tablas interactivas.
# st.table funciona para hacer tablas estáticas.
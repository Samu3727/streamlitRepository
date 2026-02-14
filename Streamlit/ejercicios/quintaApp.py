import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame (
    
    np.random.randn(10, 3),
    columns = ['a', 'b', 'c']
)

st.line_chart(chart_data)

# La línea "st.line_chart(chart_data)" crea un grafico de lineas interactivo.
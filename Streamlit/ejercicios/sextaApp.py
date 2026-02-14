import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame (
    
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(map_data)

# La línea "(1000, 2) / [50, 50]" Divide cada columna por 50 reduciendo la disperción, "+ [37.76, -122.4]" Suma las coordenadas el centro del mapa 37.76: Latitud, -122.4 Longitud distribuyendo alrededor de San Francisco.
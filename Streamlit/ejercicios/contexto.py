import streamlit as st
import pandas as pd
import numpy as np

st.markdown (
    
    """
    
    <style>
    
    .stApp {
        
       background: #fff;
       color: #000;
    }
    </style>
    """,
    
    unsafe_allow_html=True
)

st.selectbox("Seleccione de que tablero desea que sea el contexto", ["Hola", "Como estas?", "Bien y tu?"], index=None, placeholdstreer="Tablero.")

st.write("Hola como estas")


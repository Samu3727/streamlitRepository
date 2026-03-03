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


st.title("Formulario Contexto")
st.write("Ingrese el contexto del proyecto")

st.text_area("")
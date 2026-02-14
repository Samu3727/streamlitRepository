import streamlit as st

if "visibility" not in st.session_state:
    
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    
col1, col2 = st.columns(2)

with col1:
    
    st.checkbox("Desabilitar la caja de selección", key = "disabled")
    st.radio (
        
        "Determinar la visibilidad de la caja de selección",
        key = "visibility",
        options = ["visible", "hidden", "collapsed"],
    )
    
with col2:
    
    opcion = st.selectbox (
        
        "Lenguaje de Programación Favorito: ",
        ("Java", "JavaScript", "C++", "C#"),
        label_visibility = st.session_state.visibility,
        disabled = st.session_state.disabled,
    )
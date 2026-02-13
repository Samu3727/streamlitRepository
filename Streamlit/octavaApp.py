import streamlit as st

opcion = st.selectbox (
    
    "Como te gustaria que te contactaramos?",
    ("Correo", "Telefono", "Telefono fijo", "Ouija"),     
) # Ese es un widget de lista desplegable (Lo que necesitamos para uso de las Epicas y HU e el CodeBrain).

st.write("tu eleccion fue: ", opcion)
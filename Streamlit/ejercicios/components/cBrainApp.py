import streamlit as st

opcion = st.selectbox (
    
    "Que comida te gusta?",
    ("Pollo", "Pizza", "Hamburguesa", "Sushi"),
    index = None,
    placeholder = "Selecciona tu comid favorita",
)

st.write("Tu comida favorita es: ", opcion)

# Exactamente lo que necesitamos en el CodeBrain.
import streamlit as st

opcion = st.selectbox (
    
    "Bebida Preferida:",
    ["Coca Cola", "Pepsi", "Jugo de Naranja"],
    index = None,
    placeholder = "Selecciona alguna bebida o ingresa una nueva: ",
    accept_new_options = True,
)

st.write("Tu bebida favorita es: ", opcion)
import streamlit as st

if "counter" not in st.session_state:
    
    st.session_state.counter = 0
    
st.session_state.counter += 1

st.header(f"Esta página ha funcionado {st.session_state.counter} times")
st.button("Ejecutalo de nuevo")

# Esta app cuenta el numero de veces que el programa fue ejecutado basandose en el contador y en el st.session_state.
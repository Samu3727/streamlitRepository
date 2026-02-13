import streamlit as st

x = st.slider('x') # Ese es un widget de barra que se mueve y adquiere un valor según la posició

st.write(x, 'Al cuadrado es: ', x * x)
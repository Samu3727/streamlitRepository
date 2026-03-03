import streamlit as st
from Frontend.src.components.organisms.tabs import Tabs

def MainTemplate():
    st.set_page_config(page_title="AgileCodeBrAI+n", page_icon=":robot_face:", layout="wide")
    st.header("🤖 Tablero de Trabajo")
    st.selectbox("Selecciona un tablero", ["Tablero 1", "Tablero 2", "Tablero 3"])
    st.title("AgileCodeBrAI+n")
    Tabs()
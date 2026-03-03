import streamlit as st
from ..organisms.tabs import Tabs

def MainTemplate():
    st.set_page_config(page_title="AgileCodeBrAI+n", page_icon=":robot_face:", layout="wide")
    st.header("🤖 Tablero de Trabajo")
    st.selectbox("Selecciona un tablero", ["Tablero 1", "Tablero 2", "Tablero 3"], key="main_board")
    st.title("AgileCodeBrAI+n")
    Tabs()
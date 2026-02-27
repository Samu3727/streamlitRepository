from streamlit_option_menu import option_menu
import streamlit as st

with st.sidebar:
    selected = option_menu(
        "AgileCodeBrAI+n",
        ["Requerimientos", "Casos de Prueba", "Desarrollo"],
        icons=["list-task", "check2-circle", "code-slash"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Requerimientos":
    st.subheader("Opciones de Requerimientos")
    opcion = st.selectbox("Selecciona:", ["Historia de Usuario", "Épicas", "Casos"])
elif selected == "Casos de Prueba":
    st.subheader("Opciones de Casos de Prueba")
    opcion = st.selectbox("Selecciona:", ["Unit Testing", "Integración", "End-to-End"])
elif selected == "Desarrollo":
    st.subheader("Opciones de Desarrollo")
    opcion = st.selectbox("Selecciona:", ["Backend", "Frontend", "DevOps"])
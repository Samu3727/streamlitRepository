import streamlit as st
from Frontend.src.components.atoms.selectbox import SelectBox

def CodeGenerationForm():
    st.header("👨‍💻 Formulario Generación de Código")
    st.info("💡 Ingresa los datos para la generación de código.")

    user_story = SelectBox("Historia de Usuario:", ["Historia 1", "Historia 2", "Historia 3"])
    github_url = st.text_input("Url Proyecto Github:", placeholder="https://github.com/davivienda-example/DevMau")
    technology = SelectBox("Tecnología:", ["Python", "Node.js", "Java", "Ruby"])

    if st.button("Enviar"):
        st.success(f"Codigo generado con {technology} para la historia de usuario seleccionada, en el repositorio de Github proporcionado.")
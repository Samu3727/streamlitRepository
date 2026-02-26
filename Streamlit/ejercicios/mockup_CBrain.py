import streamlit as st

def main():

    st.set_page_config(page_title="AgileCodeBrAI+n", page_icon=":robot_face:", layout="wide")

    st.header("🤖 Tablero de Trabajo")
    table = st.selectbox("Selecciona un tablero", ["Tablero 1", "Tablero 2", "Tablero 3"])

    st.title("AgileCodeBrAI+n")

    tab1, tab2 = st.tabs(["Requerimientos", "Desarrollo"])

    with tab1:
        st.header("📝 Formulario Historia de Usuario")
        st.info("💡 Ingresa los requerimientos de la historia de usuario. ⚠️ Recuerda seleccionar primero el tablero para poder seleccionar la épica a la que pertenece.")
        epic = st.selectbox("Épicas", ["Épica 1", "Épica 2", "Épica 3"])
        update_story = st.checkbox("¿Necesita Actualizar una Historia de Usuario sin contenido?")

        

        if update_story:
            user_story = st.selectbox("Historia de Usuario:", ["Historia 1", "Historia 2", "Historia 3"])
        else:
            additional_info = None

        additional_info = st.text_area("Información adicional:")
        if epic:
            if st.button("Enviar"):
                if update_story and additional_info:
                    st.success("Historia de Usuario y la información adicional se han enviado correctamente.")
                elif not update_story:
                    st.success("Historia de Usuario enviada correctamente.")

    with tab2:
        st.header("👨‍💻 Formulario Generación de Código")
        st.info("💡 Ingresa los datos para la generación de código.")

        user_story = st.selectbox("Historia de Usuario:", ["Historia 1", "Historia 2", "Historia 3"])
        github_url = st.text_input("Url Proyecto Github:", placeholder="https://github.com/davivienda-example/DevMau")
        technology = st.selectbox("Tecnología:", ["Python", "Node.js", "Java", "Ruby"])
    if st.button("Enviar"):
        st.success(f"Codigo generado con {technology} para la historia de usuario seleccionada, en el repositorio de Github proporcionado.")

if __name__ == "__main__":
    main()
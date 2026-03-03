import streamlit as st
from ..atoms.selectbox import SelectBox

def UserStoryForm():
    st.header("📝 Formulario Historia de Usuario")
    st.info("💡 Ingresa los requerimientos de la historia de usuario. ⚠️ Recuerda seleccionar primero el tablero para poder seleccionar la épica a la que pertenece.")
    epic = SelectBox("Épicas", ["Épica 1", "Épica 2", "Épica 3"], key="us_epic")
    update_story = st.checkbox("¿Necesita Actualizar una Historia de Usuario sin contenido?")

    if update_story:
        user_story = SelectBox("Historia de Usuario:", ["Historia 1", "Historia 2", "Historia 3"], key="us_user_story")
    else:
        user_story = None

    additional_info = st.text_area("Información adicional:")

    if epic:
        if st.button("Enviar", key="submit_user_story"):
            if update_story and additional_info:
                st.success("Historia de Usuario y la información adicional se han enviado correctamente.")
            elif not update_story:
                st.success("Historia de Usuario enviada correctamente.")
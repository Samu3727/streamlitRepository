import streamlit as st
from ..molecules.form_user_story import UserStoryForm
from ..molecules.form_code_generation import CodeGenerationForm

def Tabs():
    tab1, tab2 = st.tabs(["Requerimientos", "Desarrollo"])

    with tab1:
        UserStoryForm()

    with tab2:
        CodeGenerationForm()
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;
        padding-top: 70px; /* espacio para que el header fijo no tape el contenido */
    }
    

    h1, p {
        color: black !important;
    }

    /* Inputs de texto y áreas de texto */
    input::placeholder,
    selectbox::placeholder,
    textarea::placeholder {
        color: grey !important;   /* color del placeholder */
        opacity: 1 !important;     /* asegura que no se vea grisáceo */
    }

    /* Selectbox cuadro */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 5px !important;
    }
    
    /* Placeholder de selectbox */
    div[data-baseweb="select"] span {
        color: black !important;   /* fuerza el color del texto */
        opacity: 1 !important;     /* evita que se vea grisáceo */
        font-style: italic;        /* opcional: estilo para diferenciar placeholder */
    }


    /* Selectbox cuadro */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 5px !important;
    }
    
    /* Menú desplegable */
    div[role="listbox"] {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
    }

    /* Opciones dentro del menú */
    div[role="option"] {
        background-color: white !important;
        color: black !important;
    }

    div[role="option"]:hover {
        background-color: #f0f0f0 !important;
        color: black !important;
    }

    /* Botones */
    div.stButton > button:first-child {
        background-color: black;
        color: white;
        border-radius: 5px;
        font-weight: bold;
        padding: 8px 16px;
    }

    /* Inputs de texto y áreas de texto */
    input, textarea {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 5px;
        padding: 6px;
    }

    /* Checkbox */
    div[data-testid="stCheckbox"] label {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("AgileCodeBrAI+n")

def main():
    st.set_page_config(page_title="AgileCodeBrAI+n - jira", page_icon=":robot_face:", layout="wide")
    
    tableros = st.selectbox("Tablero", ["Peticiones", "Quejas", "Reclamos"], index=None, placeholder="Seleccione o ingrese un Tablero.")
    
    tab1, tab2, tab3 = st.tabs(["Requerimientos","Casos de Prueba", "Desarrollo"])
    
    st.divider()
    
    with tab1:
        st.header("Formulario de Historia de Usuario(HU) 📋")
        st.info("Ingrese los requerimientos de la historia de usuario. ⚠️ Recuerda seleecionar primero el tablero para poder seleccionar la épica a la que pertenece.")
        epica = st.selectbox("Épicas", ["Backend", "Frontend", "CodeBrAI+n"], index=None, placeholder="Seleccione o ingrese la Epica.")
        actualizar_historia = st.checkbox("¿Necesita actulaizar alguna Historia de usuario?")
        
        if actualizar_historia:
            historia_usuario = st.selectbox("Historia de Usuario: ", ["Inicio de sesión", "Registro", "Proveedores"], index=None, placeholder="Seleccione o ingrese la Epica.")
        else:
            informacion_adicional = None
            
        informacion_adicional = st.text_area("Información Adicional: ")
        
        if epica:
            if st.button("Enviar", key="tab1"):
                if actualizar_historia and informacion_adicional:
                    st.success("Historia de usuario con nueva información se ha enviado correctamente.")
                elif not actualizar_historia:
                    st.success("Historia de Usuario enviada correctamente.")
    
    with tab3:
        st.header("💻 Formulario Generación de Código.")
        st.info("Ingresa los datos para la generación del código💡.")
        
        historia_usuario = st.selectbox("Historia de Usuario:", ["Registro", "Inicio de Sesión", "Codificación"], index=None, placeholder="Historia de Usuario")
        github_url = st.text_input("Url Proyecto GitHub:", placeholder="https://github.com/davivienda-example/DevSam")
        tecnologia = st.selectbox("Tecnología:", ["Python", "JavaScript", "C", "C++", "PHP"], index=None, placeholder="Tecnología")
        
    if st.button("Enviar", key="Tab2"):
        st.success(f"Codigo generado con {lenguaje} para la Historia de Usuario seleccionada en el repositorio de GitHub proporcioando.")

if __name__ == "__main__":
    main()
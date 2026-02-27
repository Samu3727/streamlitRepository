import streamlit as st

st.set_page_config(page_title="AgileCodeBrAI+n - jira", page_icon=":robot_face:", layout="wide")

st.markdown(
    """
    <style>
    stApp {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("AgileCodeBrAI+n")

tableros = st.selectbox("Tablero", ["Peticiones", "Quejas", "Reclamos"], index=None, placeholder="Seleccione o ingrese un Tablero.")

TAB_OPTIONS = ["Requerimientos", "Casos de Prueba", "Desarrollo"]

tab_activa = st.query_params.get("tab", TAB_OPTIONS[0])

if tab_activa not in TAB_OPTIONS:
    tab_activa = TAB_OPTIONS[0]

clase_req = "active" if tab_activa == "Requerimientos" else ""
clase_casos = "active" if tab_activa == "Casos de Prueba" else ""
clase_dev = "active" if tab_activa == "Desarrollo" else ""

html_content = f"""
    <style>
    .tab-menu-container {{
        display: flex;
        gap: 8px;
        margin: 1rem 0;
        border-bottom: 1px solid #ffff;
    }}
    .tab-dropdown {{
        position: relative;
        display: inline-block;
    }}
    .tab-button {{
        padding: 8px 16px;
        font-size: 14px;
        font-weight: 500;
        border-bottom: 3px solid transparent;
        cursor: pointer;
        transition: all 0.3s;
        color: #fff;
        background: none;
        border: none;
    }}
    .tab-button.active {{
        color: #ffff;
        border-bottom-color: #f09090;
    }}
    .tab-button:hover {{
        color: #f24b4b;
    }}
    .dropdown-content {{
        display: none;
        position: absolute;
        top: 42px;
        left: 0;
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        min-width: 200px;
        z-index: 1000;
        overflow: hidden;
    }}
    .tab-dropdown:hover .dropdown-content {{
        display: block;
    }}
    .dropdown-content a {{
        color: #333;
        padding: 10px 16px;
        text-decoration: none;
        display: block;
        font-size: 14px;
    }}
    .dropdown-content a:hover {{
        background: #f5d7d7;
    }}
    </style>

    <div class="tab-menu-container">
        <div class="tab-dropdown">
            <div class="tab-button {clase_req}">Requerimientos &#9662;</div>
            <div class="dropdown-content">
                <a href="?tab=Requerimientos">Formulario HU</a>
                <a href="?tab=Requerimientos">Ver Historico</a>
                <a href="?tab=Requerimientos">Plantillas</a>
            </div>
        </div>
        <div class="tab-dropdown">
            <div class="tab-button {clase_casos}">Casos de Prueba &#9662;</div>
            <div class="dropdown-content">
                <a href="?tab=Casos+de+Prueba">Crear Caso</a>
                <a href="?tab=Casos+de+Prueba">Ver Historico</a>
                <a href="?tab=Casos+de+Prueba">Plantillas</a>
            </div>
        </div>
        <div class="tab-dropdown">
            <div class="tab-button {clase_dev}">Desarrollo &#9662;</div>
            <div class="dropdown-content">
                <a href="?tab=Desarrollo">Generar Codigo</a>
                <a href="?tab=Desarrollo">Ver Proyectos</a>
                <a href="?tab=Desarrollo">Configurar IA</a>
            </div>
        </div>
    </div>
    """

st.markdown(html_content, unsafe_allow_html=True)

if tab_activa == "Requerimientos":
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

elif tab_activa == "Casos de Prueba":
    st.header("🧪 Formulario Casos de Prueba")
    st.write("💡 Ingrese o seleccione el caso de prueba")
    
    casos_de_uso = st.selectbox("Historia de Usuario:", ["Epica para Prueba", "Simulación para código"], index=None, placeholder="Historia de Usuario:")
    
    if st.button("Enviar", key="Tab2"):
        st.success("Se ha enviado los Casos de Uso correctamente.")

elif tab_activa == "Desarrollo":
    st.header("💻 Formulario Generación de Código.")
    st.info("Ingresa los datos para la generación del código💡.")
    
    historia_usuario = st.selectbox("Historia de Usuario:", ["Registro", "Inicio de Sesión", "Codificación"], index=None, placeholder="Historia de Usuario")
    github_url = st.text_input("Url Proyecto GitHub:", placeholder="https://github.com/davivienda-example/DevSam")
    tecnologia = st.selectbox("Tecnología:", ["Python", "JavaScript", "C", "C++", "PHP"], index=None, placeholder="Tecnología")
    
    if st.button("Enviar", key="Tab3"):
        st.success(f"Codigo generado con {tecnologia} para la Historia de Usuario seleccionada en el repositorio de GitHub proporcionado.")
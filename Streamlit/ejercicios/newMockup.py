import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AgileCodeBrAI+n - jira", page_icon=":robot_face:", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: white !important;
        color: black !important;
    }

    /* Labels de selectbox y text inputs */
    label, .stSelectbox label, .stTextInput label, .stTextArea label, .stCheckbox label {
        color: black !important;
    }

    /* Contenedor del selectbox */
    .stSelectbox > div > div,
    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: white !important;
        border-radius: 6px !important;
        color: black !important;
    }

    /* TextArea específico */
    .stTextArea textarea {
        background-color: white !important;
        color: black !important;
    }

    .stTextArea textarea::placeholder {
        color: #666 !important;
        opacity: 1 !important;
    }

    .stTextArea textarea:focus {
        box-shadow: none !important;
    }

    /* Placeholder */
    .stSelectbox [data-baseweb="select"] [data-testid="stMarkdownContainer"],
    input::placeholder,
    textarea::placeholder {
        color: #666 !important;
    }

    /* Texto seleccionado dentro del selectbox */
    .stSelectbox span {
        color: black !important;
    }

    /* Flecha del selectbox */
    .stSelectbox svg {
        fill: black !important;
    }

    /* Menú desplegable del selectbox */
    [data-baseweb="popover"] ul,
    [data-baseweb="menu"] {
        background-color: white !important;
        border: 1px solid black !important;
    }

    [data-baseweb="menu"] li {
        color: black !important;
    }

    [data-baseweb="menu"] li:hover {
        background-color: #f0f0f0 !important;
    }

    /* Headers y texto general */
    h1, h2, h3, p, span, div {
        color: black !important;
    }

    /* Botones */
    .stButton > button {
        background-color: white !important;
        color: black !important;
        border: 1.5px solid black !important;
    }

    .stButton > button:hover {
        background-color: #f0f0f0 !important;
    }

    /* Checkbox base */
    [data-baseweb="checkbox"] span {
        background-color: red !important;
        border-color: black !important;
    }

    [data-baseweb="checkbox"] svg {
        fill: white !important;
    }

    .checkbox-checked span {
        background-color: red !important;
        border-color: red !important;
    }

    }
    </style>
    """,
    unsafe_allow_html=True
)

components.html(
    """
    <script>
    function updateCheckboxes() {
        var doc = window.parent.document;
        doc.querySelectorAll('[data-baseweb="checkbox"]').forEach(function(cb) {
            var input = cb.querySelector('input[type="checkbox"]');
            var span = cb.querySelector('span');
            if (!input || !span) return;
            function applyStyle() {
                if (input.checked) {
                    span.style.setProperty('background-color', 'red', 'important');
                    span.style.setProperty('border-color', 'red', 'important');
                } else {
                    span.style.setProperty('background-color', 'white', 'important');
                    span.style.setProperty('border-color', 'black', 'important');
                }
            }
            applyStyle();
            if (!input._listenerAdded) {
                input.addEventListener('change', applyStyle);
                input._listenerAdded = true;
            }
        });
    }
    var observer = new MutationObserver(updateCheckboxes);
    observer.observe(window.parent.document.body, { childList: true, subtree: true });
    setTimeout(updateCheckboxes, 500);
    </script>
    """,
    height=0
)

st.header("AgileCodeBrAI+n")

tableros = st.selectbox("Tablero", ["Peticiones", "Quejas", "Reclamos"], index=None, placeholder="Tablero")

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
        border-bottom: 1px solid #d6d2d2;
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
        color: #000;
        background: none;
        border: none;
    }}
    
    .tab-button.active {{
        color: #000;
        border-bottom-color: #c00;
    }}
    
    .tab-button:hover {{
        color: #c00;
    }}
    
    .dropdown-content {{
        display: none;
        position: absolute;
        top: 42px;
        left: 0;
        background: #1a1a1a;
        border: 1px solid #444;
        border-radius: 6px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        min-width: 200px;
        z-index: 1000;
        overflow: hidden;
    }}
    
    .tab-dropdown:hover .dropdown-content {{
        display: block;
    }}
    
    .dropdown-content a {{
        color: #fff;
        padding: 10px 16px;
        text-decoration: none;
        display: block;
        font-size: 14px;
    }}
    
    .dropdown-content a:hover {{
        background: #333;
    }}
    
    </style>

    <div class="tab-menu-container">
        <div class="tab-dropdown">
            <div class="tab-button {clase_req}">Requerimientos &#9662;</div>
            <div class="dropdown-content">
                <a href="?tab=Requerimientos">Contexto</a>
                <a href="?tab=Requerimientos">Historia de usuario</a>
            </div>
        </div>
        <div class="tab-dropdown">
            <div class="tab-button {clase_casos}">Casos de Prueba &#9662;</div>
            <div class="dropdown-content">
                <a href="?tab=Casos+de+Prueba">Pruebas</a>
                <a href="?tab=Casos+de+Prueba">Automatización E2E</a>
                <a href="?tab=Casos+de+Prueba">API OAS</a>
            </div>
        </div>
        <div class="tab-dropdown">
            <div class="tab-button {clase_dev}">Desarrollo &#9662;</div>
            <div class="dropdown-content">
                <a href="?tab=Desarrollo">Código</a>
            </div>
        </div>
    </div>
    """

st.markdown(html_content, unsafe_allow_html=True)

if tab_activa == "Requerimientos":
    st.header("📋 Formulario Historia de Usuario")
    st.write("💡 Ingrese los requerimientos de la historia de usuario. ⚠️ Recuerda seleecionar primero el tablero para poder seleccionar la épica a la que pertenece.")
    epica = st.selectbox("Épicas", ["Backend", "Frontend", "CodeBrAI+n"], index=None, placeholder="Épicas")
    actualizar_historia = st.checkbox("¿Necesita actulaizar alguna Historia de usuario?")
    
    historia_usuario = None
    if actualizar_historia:
        historia_usuario = st.selectbox("Historia de Usuario: ", ["Inicio de sesión", "Registro", "Proveedores"], index=None, placeholder="Seleccione o ingrese la Epica.")
        
    informacion_adicional = st.text_area("Información Adicional:", max_chars=50000)
    
    char_count = len(informacion_adicional) if informacion_adicional else 0
    st.markdown(
        f'<p style="text-align:right; color: {"red" if char_count >= 50000 else "#666"}; font-size:12px;">{char_count:,} / 50,000</p>',
        unsafe_allow_html=True
    )

    # Determinar si todos los campos están llenos
    campos_ok = bool(epica) and bool(informacion_adicional)
    if actualizar_historia:
        campos_ok = campos_ok and bool(historia_usuario)

    if campos_ok:
        btn_style = """
        <style>
        div[data-testid="stButton"] > button {
            display: block;
            margin: 20px auto 0 auto;
            background-color: red !important;
            border: none !important;
            padding: 10px 40px;
            width: 250px;
            font-size: 16px;
            border-radius: 50px;
            cursor: pointer;
        }
        div[data-testid="stButton"] > button p,
        div[data-testid="stButton"] > button span,
        div[data-testid="stButton"] > button * {
            color: white !important;
        }
        </style>
        """
    else:
        btn_style = """
        <style>
        div[data-testid="stButton"] > button {
            display: block;
            margin: 20px auto 0 auto;
            background-color: #ccc !important;
            border: none !important;
            padding: 10px 40px;
            width: 250px;
            font-size: 16px;
            border-radius: 50px;
            cursor: not-allowed;
        }
        div[data-testid="stButton"] > button p,
        div[data-testid="stButton"] > button span,
        div[data-testid="stButton"] > button * {
            color: #888 !important;
        }
        </style>
        """
    st.markdown(btn_style, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([4, 2, 4])
    with col2:
        if st.button("Enviar", key="tab1", disabled=not campos_ok):
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
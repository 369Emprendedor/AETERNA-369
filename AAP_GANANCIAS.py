import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA ---
st.set_page_config(page_title="AETERNA 369 | CORE", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CONVERSIÓN DE IMAGEN A FONDO (Lógica de Inyección) ---
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Intentar cargar la Cúpula como fondo real
bg_img = ""
if os.path.exists("CUPULA_369.png"):
    bin_str = get_base64("CUPULA_369.png")
    bg_img = f"url(data:image/png;base64,{bin_str})"

# --- 3. CSS DE ALTA FIDELIDAD (ELIMINA LO NEGRO) ---
st.markdown(f"""
<style>
    /* Forzar que el fondo sea la imagen y no haya nada negro */
    .stApp {{
        background-image: {bg_img};
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Eliminar contenedores de Streamlit que comprimen el diseño */
    .block-container {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    header, footer {{visibility: hidden !important;}}

    /* PANELES HOLOGRÁFICOS FLOTANTES */
    .panel-soberano {{
        position: fixed;
        background: rgba(0, 0, 0, 0.7);
        border: 2px solid #d4af37;
        padding: 15px;
        color: #d4af37;
        font-family: 'Courier New', monospace;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
        z-index: 100;
        backdrop-filter: blur(5px);
    }}

    .top-left {{ top: 20px; left: 20px; width: 250px; }}
    .top-right {{ top: 20px; right: 20px; width: 300px; }}
    .bottom-center {{ bottom: 30px; left: 50%; transform: translateX(-50%); width: 500px; }}
    
    /* Input de comandos */
    input {{
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid #d4af37 !important;
        color: #d4af37 !important;
        text-align: center;
        width: 100%;
        font-size: 18px;
    }}
</style>
""", unsafe_allow_html=True)

# --- 4. RENDERIZADO DE LOS NÓDOS ---

# Nodo Izquierdo: Capital
st.markdown('<div class="panel-soberano top-left"><b>ESTATUS DE CAPITAL</b><br><small>LIQUIDEZ SOBERANA</small></div>', unsafe_allow_html=True)

# Nodo Derecho: Infraestructura
st.markdown('<div class="panel-soberano top-right"><b>RED NVDA | ASML</b><br><small>SYNC: 99.8% | NANO-LITOGRAFÍA</small></div>', unsafe_allow_html=True)

# Nodo Inferior: Terminal
st.markdown('<div class="panel-soberano bottom-center">', unsafe_allow_html=True)
cmd = st.text_input("", placeholder="AETERNA: ESPERANDO COMANDO...", key="cmd_soberano")
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. AUDIO (Si existe) ---
if os.path.exists("latido_369.mp3"):
    a_str = get_base64("latido_369.mp3")
    st.markdown(f'<audio autoplay loop><source src="data:audio/mp3;base64,{a_str}" type="audio/mp3"></audio>', unsafe_allow_html=True)

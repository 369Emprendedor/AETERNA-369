import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN DE PANTALLA COMPLETA ---
st.set_page_config(page_title="AETERNA 369 | NODO CORE", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INYECTOR DE GEOMETRÍA HUD (CSS) ---
st.markdown("""
<style>
    /* Reset total para eliminar márgenes de Streamlit */
    .main .block-container {
        max-width: 100vw !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    .stApp { background-color: #000; overflow: hidden; }

    /* CONTENEDOR MAESTRO QUE LLENA EL MONITOR HP */
    .viewport {
        position: relative;
        width: 100vw;
        height: 100vh;
        background-color: #000;
    }

    /* LA CÚPULA: OCUPAR TODO EL FONDO */
    .background-media {
        position: absolute;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: cover; /* Esto estira la imagen/video a toda la pantalla */
        z-index: 0;
        opacity: 0.6;
    }

    /* PANELES HOLOGRÁFICOS POSICIONADOS POR COORDENADAS */
    .overlay-panel {
        position: absolute;
        z-index: 10;
        background: rgba(0, 0, 0, 0.7);
        border: 1px solid #d4af37;
        padding: 15px;
        font-family: 'Courier New', monospace;
        color: #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }

    .panel-derecho { top: 50px; right: 30px; width: 300px; }
    .panel-izquierdo { top: 50px; left: 30px; width: 280px; }
    .panel-inferior { bottom: 80px; left: 25vw; width: 50vw; }
    
    /* BARRAS DE FLUJO LUMEN */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #d4af37, #fff, #d4af37) !important;
        background-size: 200% 100% !important;
        animation: flow 2s linear infinite !important;
    }
    @keyframes flow { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

    /* INPUT DE COMANDOS */
    .stTextInput input {
        background-color: transparent !important;
        color: #d4af37 !important;
        border: none !important;
        border-bottom: 1px solid #d4af37 !important;
        text-align: center;
        font-size: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. RENDERIZADO DE CAPAS ---
st.markdown("<div class='viewport'>", unsafe_allow_html=True)

# CAPA DE FONDO: CÚPULA 369
if os.path.exists("CUPULA_369.png"):
    with open("CUPULA_369.png", "rb") as f:
        data = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/png;base64,{data}" class="background-media">', unsafe_allow_html=True)
else:
    st.markdown('<div class="background-media" style="display:flex; align-items:center; justify-content:center; color:#333;">[ CARGANDO MATRIZ VISUAL... ]</div>', unsafe_allow_html=True)

# PANEL DERECHO: INTELIGENCIA (NVDA/ASML)
st.markdown(f"""
<div class='overlay-panel panel-derecho'>
    <div style='font-size:10px; color:#888;'>INTELIGENCIA DE INFRAESTRUCTURA</div>
    <div style='font-size:18px; font-weight:bold;'>NVDA | ASML</div>
    <hr style='border: 0.5px solid #d4af37; opacity: 0.3;'>
    <div style='font-size:12px;'>SYNC: 99.8%</div>
</div>
""", unsafe_allow_html=True)

# PANEL IZQUIERDO: CAPITAL (STARLINK/LUMEN)
st.markdown(f"""
<div class='overlay-panel panel-izquierdo'>
    <div style='font-size:10px; color:#888;'>ESTATUS DE CAPITAL</div>
    <div style='font-size:18px; font-weight:bold;'>PODER SOBERANO</div>
    <div style='font-size:12px; color:#00ff00;'>STATUS: ONLINE</div>
</div>
""", unsafe_allow_html=True)

# PANEL INFERIOR: TERMINAL
st.markdown("<div class='overlay-panel panel-inferior'>", unsafe_allow_html=True)
comando = st.text_input("", placeholder="INTRODUCE COMANDO DE INTERCEPCIÓN...", key="cmd")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True) # CIERRE DE VIEWPORT

# --- 4. AUDIO (CONTROL FLOTANTE) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        a_data = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <audio id="h_audio" loop><source src="data:audio/mp3;base64,{a_data}" type="audio/mp3"></audio>
        <div style='position:absolute; bottom:20px; left:20px; z-index:100; cursor:pointer; color:#d4af37; border:1px solid #d4af37; padding:5px; font-size:10px;' 
             onclick="document.getElementById('h_audio').play();">
             ACTIVAR PULSO
        </div>
    """, unsafe_allow_html=True)

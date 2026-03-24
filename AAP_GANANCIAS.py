import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (HUD PANORÁMICO HP) ---
st.set_page_config(
    page_title="AETERNA 369 NODO 001", 
    layout="wide", # <-- Ancho total obligatorio
    initial_sidebar_state="collapsed"
)

# --- 2. CSS DE INYECCIÓN HOLOGRÁFICA (PULSO 3D) ---
st.markdown("""
<style>
    /* Reset total para eliminar márgenes de Streamlit */
    .stApp { 
        background-color: #000000; 
        color: #d4af37; 
        overflow: hidden !important; 
    }
    .block-container { padding: 0rem !important; max-width: 100% !important; margin: 0 !important; }

    /* CONTENEDOR MAESTRO DEL HUD (CANVAS 3D) */
    .hud-canvas {
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
    }

    /* LA CÚPULA: OCUPAR TODO EL FONDO SIN CORTES */
    .cupula-media {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover; /* Estira la imagen para llenar el monitor */
        z-index: 1;
        opacity: 0.8; /* Transparencia suave */
    }

    /* ESTILO GENERAL DE ELEMENTOS FLOTANTES */
    .holo-ui {
        position: absolute;
        z-index: 10; /* Por encima de la Cúpula */
        background: rgba(0, 0, 0, 0.6); /* Fondo semi-transparente */
        border: 2px solid #d4af37;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.3); /* Glow suave */
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #d4af37;
        backdrop-filter: blur(5px); /* Desenfoque de fondo */
    }

    /* UBICACIONES GEOMÉTRICAS EXACTAS */
    .panel-intel { top: 10vh; right: 2vw; width: 20vw; }
    .panel-capital { top: 10vh; left: 2vw; width: 20vw; }
    .chat-terminal { bottom: 5vh; left: 30vw; width: 40vw; text-align: center; }

    /* ESTILO DE BARRAS DE PROGRESO LÍQUIDAS */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #d4af37, #ffffff, #d4af37) !important;
        background-size: 200% 100% !important;
        animation: flow_lumen 2s linear infinite !important;
    }
    @keyframes flow_lumen { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

    /* INPUT TERMINAL SOBERANA */
    .stTextInput input {
        background-color: transparent !important;
        color: #d4af37 !important;
        border: none !important;
        border-bottom: 2px solid #d4af37 !important;
        font-size: 1.2rem !important;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. INICIO DEL CANVAS MAESTRO DEL HUD ---
st.markdown("<div class='hud-canvas'>", unsafe_allow_html=True)

# A. LA CÚPULA (FONDO COMPLETO ADAPTADO)
if os.path.exists("CUPULA_369.png"):
    with open("CUPULA_369.png", "rb") as f:
        data = f.read()
        b64_img = base64.b64encode(data).decode()
    st.markdown(f"<img src='data:image/png;base64,{b64_img}' class='cupula-media'>", unsafe_allow_html=True)

# B. ELEMENTOS HOLOGRÁFICOS FLOTANTES (3D POSICIONADOS)

# 1. TÍTULO CENTRAL SUPERIOR
st.markdown("<div class='holo-ui' style='top: 2vh; left: 40vw; width: 20vw; text-align: center;'>AETERNA 369 - NODO ACTIVADO</div>", unsafe_allow_html=True)

# 2. PANEL DE INTELIGENCIA (DERECHA, FLOTANDO SOBRE LA CÚPULA)
st.markdown("<div class='holo-ui panel-intel'>", unsafe_allow_html=True)
st.markdown("<div style='font-size: 12px; font-weight: bold;'>RED NVDA H100 | ASML EUV</div>", unsafe_allow_html=True)
st.progress(98)
st.markdown("<div style='font-size: 10px;'>SYNC: 99.8%</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 3. PANEL DE CAPITAL (IZQUIERDA, FLOTANDO SOBRE LA CÚPULA)
st.markdown("<div class='holo-ui panel-capital'>", unsafe_allow_html=True)
st.markdown("<div style='font-size: 12px; font-weight: bold;'>ESTATUS DE CAPITAL</div>", unsafe_allow_html=True)
st.progress(95)
st.markdown("<div style='font-size: 10px; color: #00ff00;'>PODER: SOBERANO</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

#  core del chat
# 4. CHAT TERMINAL (CENTRO INFERIOR, FLOTANDO SOBRE LA CÚPULA)
st.markdown("<div class='holo-ui chat-terminal'>", unsafe_allow_html=True)
# Formulario vacío para posicionar el input de Streamlit aquí
with st.container():
    comando = st.text_input("SISTEMA:", placeholder="Introduce comando...", key="core_integrated")
st.markdown("</div>", unsafe_allow_html=True)

# 5. AUDIO SELLO DE ACTIVACIÓN (FLOTANTE ABAJO IZQUIERDA)
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data_audio = f.read()
        b64_audio = base64.b64encode(data_audio).decode()
        
    audio_html = f"""
        <div class='holo-ui' style='bottom: 5vh; left: 2vw; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; cursor: pointer;'
             onclick="var a=document.getElementById('audio_core'); a.play(); this.style.backgroundColor='#00ff00';">
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3"></audio>
            <div style='font-size: 10px; font-weight: bold; color: #000;'>ACTIVAR</div>
        </div>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- FIN DEL CANVAS MAESTRO DEL HUD ---
st.markdown("</div>", unsafe_allow_html=True)

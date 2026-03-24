import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (ELIMINA TODO EL ESPACIO NEGRO) ---
st.set_page_config(page_title="AETERNA 369 | CORE", layout="wide", initial_sidebar_state="collapsed")

# --- 2. MOTOR DE RENDERIZADO (CSS) ---
st.markdown("""
<style>
    /* Forzar que no haya scroll ni espacios negros arriba */
    [data-testid="stAppViewContainer"] {
        background-color: #000 !important;
        overflow: hidden !important;
    }
    .main .block-container {
        padding: 0 !important;
        max-width: 100vw !important;
        height: 100vh !important;
    }
    header, footer {visibility: hidden !important;}

    /* LA CÚPULA DE FONDO */
    .cupula-fondo {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        object-fit: cover;
        z-index: -1;
        opacity: 0.7;
    }

    /* PANELES HOLOGRÁFICOS (ACHICADOS Y POSICIONADOS) */
    .hud-panel {
        position: fixed;
        background: rgba(0, 0, 0, 0.7);
        border: 1px solid #d4af37;
        padding: 10px;
        color: #d4af37;
        font-family: 'Courier New', monospace;
        z-index: 100;
        backdrop-filter: blur(5px);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }

    .p-capital { top: 30px; left: 30px; width: 220px; }
    .p-infra { top: 30px; right: 30px; width: 220px; }
    
    /* TERMINAL CENTRAL (POSICIÓN FIJA PARA QUE NO SE CORRA) */
    .p-terminal {
        bottom: 50px;
        left: 50%;
        transform: translateX(-50%);
        width: 400px;
        text-align: center;
    }

    /* BOTÓN DE AUDIO (EL CORAZÓN) */
    .p-audio {
        top: 30px;
        left: 50%;
        transform: translateX(-50%);
        cursor: pointer;
        background: rgba(212, 175, 55, 0.1);
        border-radius: 5px;
        font-size: 12px;
        padding: 5px 15px;
    }

    /* ESTILO DE LA TERMINAL */
    .stTextInput input {
        background-color: transparent !important;
        color: #d4af37 !important;
        border: none !important;
        border-bottom: 2px solid #d4af37 !important;
        text-align: center;
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. PROCESAMIENTO DE ARCHIVOS ---
def to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Fondo (Imagen o Video)
if os.path.exists("CUPULA_369.png"):
    img_b64 = to_b64("CUPULA_369.png")
    st.markdown(f'<img src="data:image/png;base64,{img_b64}" class="cupula-fondo">', unsafe_allow_html=True)

# --- 4. INTERFAZ FLOTANTE ---

# Panel Capital
st.markdown('<div class="hud-panel p-capital"><b>CAPITAL</b><br><small>PODER SOBERANO</small></div>', unsafe_allow_html=True)

# Panel Infraestructura
st.markdown('<div class="hud-panel p-infra"><b>NVDA | ASML</b><br><small>SYNC: 99.8%</small></div>', unsafe_allow_html=True)

# Botón de Audio (Corazón de Aeterna)
if os.path.exists("latido_369.mp3"):
    audio_b64 = to_b64("latido_369.mp3")
    st.markdown(f"""
        <div class="hud-panel p-audio" onclick="document.getElementById('heartbeat').play()">
            ❤️ ACTIVAR CORAZÓN AETERNA
        </div>
        <audio id="heartbeat" loop><source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3"></audio>
    """, unsafe_allow_html=True)

# Terminal de Comandos (Visible y Funcional)
st.markdown('<div class="hud-panel p-terminal">', unsafe_allow_html=True)
cmd = st.text_input("SISTEMA", placeholder="Escribe comando...", key="main_cmd")
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (PANTALLA COMPLETA) ---
st.set_page_config(page_title="AETERNA 369 HUD", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE INTEGRACIÓN HOLOGRÁFICA (EL CEREBRO DEL DISEÑO) ---
st.markdown("""
<style>
    /* Fondo negro absoluto y eliminar scroll */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 0rem !important; max-width: 100% !important; }

    /* CONTENEDOR MAESTRO DEL HUD (Contiene la imagen y los controles) */
    .hud-container {
        position: relative;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    /* LA CÚPULA (Imagen de fondo inmersiva) */
    .cupula-bg {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover; /* Llena la pantalla */
        z-index: 1;
        opacity: 0.8; /* Ligeramente oscurecida para que resalten los controles */
    }

    /* ESTILO COMÚN PARA ELEMENTOS HOLOGRÁFICOS */
    .holo-element {
        position: absolute;
        z-index: 10; /* Por encima de la imagen */
        font-family: 'Courier New', monospace;
        color: #d4af37;
        text-shadow: 0 0 10px #d4af37, 0 0 20px #d4af37; /* Brillo neón */
    }

    /* 1. TÍTULO SUPERIOR */
    .hud-header {
        top: 20px;
        font-size: 1.5rem;
        font-weight: bold;
        animation: flicker 3s infinite;
    }

    /* 2. PANEL DE BARRAS (Holograma Flotante a la Derecha) */
    .data-panel {
        top: 30%; right: 50px;
        width: 300px;
        background: rgba(0, 0, 0, 0.5); /* Fondo semi-transparente */
        border: 1px solid #d4af37;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
    }
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 8px !important; }
    .label-gold { font-size: 0.8rem; margin-bottom: 2px; }

    /* 3. CHAT DE COMANDOS (Holograma Inferior Central) */
    .chat-panel {
        bottom: 50px;
        width: 500px;
        padding: 10px;
    }
    .stTextInput>div>div>input {
        background-color: rgba(0, 0, 0, 0.7) !important; /* Transparente */
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        text-shadow: 0 0 5px #d4af37;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.3) inset;
    }

    /* 4. BOTÓN DE AUDIO (Holograma Flotante a la Izquierda) */
    .audio-panel {
        bottom: 50px; left: 50px;
        width: fit-content;
    }
    .audio-trigger {
        background: rgba(0, 0, 0, 0.5);
        color: #d4af37;
        border: 1px solid #d4af37;
        padding: 8px 15px;
        cursor: pointer;
        font-size: 12px;
        font-weight: bold;
        text-shadow: 0 0 5px #d4af37;
    }
    .audio-trigger:hover { background: #d4af37; color: #000; box-shadow: 0 0 15px #d4af37; }

    /* ANIMACIONES */
    @keyframes flicker {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
        90% { opacity: 0.9; }
    }

</style>
""", unsafe_allow_html=True)

# --- 3. INICIO DEL CONTENEDOR MAESTRO ---
st.markdown("<div class='hud-container'>", unsafe_allow_html=True)

# A. LA CÚPULA (FONDO)
if os.path.exists("CUPULA_369.png"):
    # Convertimos la imagen a base64 para inyectarla en el CSS de fondo
    with open("CUPULA_369.png", "rb") as f:
        data = f.read()
        b64_img = base64.b64encode(data).decode()
    st.markdown(f"<img src='data:image/png;base64,{b64_img}' class='cupula-bg'>", unsafe_allow_html=True)
else:
    st.error("⚠️ Matriz visual 'CUPULA_369.png' no encontrada.")

# --- B. INYECCIÓN DE ELEMENTOS HOLOGRÁFICOS ---

# 1. TÍTULO
st.markdown("<div class='holo-element hud-header'>AETERNA 369 - HUD SOBERANO</div>", unsafe_allow_html=True)

# 2. PANEL DE DATOS (NVDA, ASML, CAPITAL)
st.markdown("<div class='holo-element data-panel'>", unsafe_allow_html=True)
st.markdown("<p class='label-gold'>🌌 NVDA</p>", unsafe_allow_html=True)
st.progress(95)
st.markdown("<p class='label-gold'>🔬 ASML</p>", unsafe_allow_html=True)
st.progress(100)
st.markdown("<p class='label-gold'>💰 CAPITAL</p>", unsafe_allow_html=True)
st.progress(90)
st.markdown("</div>", unsafe_allow_html=True) # Cierra data-panel

# 3. CHAT DE COMANDOS (CENTRAL INFERIOR)
st.markdown("<div class='holo-element chat-panel'>", unsafe_allow_html=True)
# Usamos un formulario vacío para forzar que el chat se renderice aquí en el HTML
with st.container():
    comando = st.text_input("SISTEMA:", placeholder="Introduce comandos...", key="hud_cmd")
st.markdown("</div>", unsafe_allow_html=True) # Cierra chat-panel

# 4. MOTOR DE AUDIO (INFERIOR IZQUIERDO)
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data_audio = f.read()
        b64_audio = base64.b64encode(data_audio).decode()
        
    audio_html = f"""
        <div class='holo-element audio-panel'>
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3"></audio>
            <div class="audio-trigger" id="btn-audio"
                 onclick="var a=document.getElementById('audio_core'); a.play(); this.innerText='PULSO ACTIVO'; this.style.color='#00ff00';">
                ACTIVAR PULSO SONORO
            </div>
        </div>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# --- FIN DEL CONTENEDOR MAESTRO ---
st.markdown("</div>", unsafe_allow_html=True)

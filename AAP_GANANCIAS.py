import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN DE IDENTIDAD (PANTALLA ANCHA) ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE EXPANSIÓN Y CENTRADO VISUAL (NUEVA ESTRUCTURA) ---
st.markdown("""
<style>
    /* Forzar fondo negro y eliminar scroll del navegador */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    
    /* Eliminar márgenes por defecto de Streamlit */
    .block-container { padding: 0rem !important; max-width: 100%; }

    /* CONTENEDOR MAESTRO: Centra todo y le da el ancho justo */
    .main-canvas {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        height: 100vh;
        width: 100vw;
        padding-top: 1vh;
    }

    /* Título minimalistico */
    .header-369 {
        text-align: center;
        color: #d4af37;
        font-size: 1.5rem;
        text-shadow: 0 0 10px #d4af37;
        margin-bottom: 5px;
    }

    /* BOTÓN DE AUDIO CENTRAL */
    .audio-btn {
        background: #000;
        color: #d4af37;
        border: 2px solid #d4af37;
        padding: 8px 15px;
        text-align: center;
        margin-bottom: 10px;
        cursor: pointer;
        font-family: monospace;
        font-size: 12px;
        font-weight: bold;
    }
    .audio-btn:hover { background: #d4af37; color: #000; }

    /* IMAGEN EXPANSIBLE Y CENTRALIZED */
    .img-box {
        text-align: center;
        width: 80% !important; /* Le damos el 80% del ancho del monitor */
        margin-bottom: 10px;
    }
    .stImage > img {
        max-height: 30vh !important; /* Ajuste manual de altura: 30% del monitor */
        width: auto !important;
        border: 2px solid #d4af37;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.4);
    }
    /* BARRAS DE PROGRESO Y ETIQUETAS (En la zona visible) */
    .progress-box {
        width: 55%; /* Ligeramente más estrecho que la imagen para estética */
    }
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 10px !important; }
    .label-gold { color: #d4af37; font-size: 0.85rem; text-align: center; font-family: monospace; margin: 0; }
    /* Input de Chat visible */
    .stTextInput > div > div > input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE AUDIO (CENTRALIZADO) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div style="display: flex; justify-content: center;">
                <div class="audio-btn" onclick="document.getElementById('audio_core').play(); this.innerText='[ PULSO ACTIVO ]'">
                    ACTIVAR PULSO SOBERANO
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- 4. CONSTRUCCIÓN DE LA INTERFAZ EXPANDIDA ---
st.markdown("<div class='header-369'>SISTEMA AETERNA 369</div>", unsafe_allow_html=True)

# Contenedor para Imagen (con ancho controlado)
with st.container():
    col_left_img, col_mid_img, col_right_img = st.columns([1, 8, 1]) # Columnas [10%, 80%, 10%]
    with col_mid_img:
        if os.path.exists("CUPULA_369.png"):
            st.image("CUPULA_369.png", use_container_width=True) # La imagen llena el 80% central

# Contenedor para Barras y Chat (Justo debajo de la imagen)
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
with st.container():
    col_left_data, col_mid_data, col_right_data = st.columns([1.5, 7, 1.5]) # Columnas [15%, 70%, 15%]
    with col_mid_data:
        # Tríada de Poder
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<p class='label-gold'>🌌 NVDA</p>", unsafe_allow_html=True)
            st.progress(95)
        with c2:
            st.markdown("<p class='label-prog'>🔬 ASML</p>", unsafe_allow_html=True)
            st.progress(100)
        with c3:
            st.markdown("<p class='label-prog'>💰 CAPITAL</p>", unsafe_allow_html=True)
            st.progress(90)

        # Input de Comandos (Subido para visibilidad)
        st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        comando = st.text_input("SISTEMA SOBERANO:", placeholder="Comandos del Arquitecto...", key="cmd_v4")

        st.markdown("<p style='text-align:center; color:#333; font-size:9px;'>PALMETTO BAY</p>", unsafe_allow_html=True)

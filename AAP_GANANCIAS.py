import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS RADICAL PARA MONITORES (SIN SCROLL) ---
st.markdown("""
<style>
    /* Forzar fondo y ocultar barras de scroll */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 1rem !important; }

    /* Título compacto */
    .header-369 {
        text-align: center;
        color: #d4af37;
        font-size: 1.2rem;
        text-shadow: 0 0 10px #d4af37;
        margin-bottom: 5px;
    }

    /* IMAGEN: Forzamos tamaño pequeño para que suba todo */
    .stImage > img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 35vh !important; /* Ajuste a 35% de la pantalla */
        width: auto !important;
        border: 1px solid #d4af37;
    }

    /* Barras de progreso y etiquetas */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; }
    .label-prog { color: #d4af37; font-size: 0.8rem; text-align: center; margin-bottom: 0px; }

    /* Input de chat: Forzar visibilidad */
    .stTextInput > div > div > input {
        background-color: #111 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- BOTÓN DE AUDIO (FLOTANTE E INFALIBLE) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div id="trigger" onclick="document.getElementById('audio_core').play(); this.style.color='#00ff00'; this.innerText='[ PULSO ACTIVO ]'" 
                 style="position:fixed; top:10px; right:10px; color:#d4af37; cursor:pointer; border:2px solid #d4af37; padding:10px; z-index:9999; background:black; font-family:monospace; font-size:12px;">
                [ ACTIVAR AUDIO ]
            </div>
        """, unsafe_allow_html=True)

# --- CONTENIDO DE LA INTERFAZ ---
st.markdown("<div class='header-369'>SISTEMA AETERNA 369 - NODO 001</div>", unsafe_allow_html=True)

# Imagen
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# Espaciador mínimo
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)

# Tríada de Poder
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<p class='label-prog'>🌌 NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with c2:
    st.markdown("<p class='label-prog'>🔬 ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with c3:
    st.markdown("<p class='label-prog'>💰 CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# Input de Chat (Ahora debe verse sí o sí)
st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)
comando = st.text_input("COMANDO SOBERANO:", placeholder="Escribe al pulso de AETERNA...", key="input_soberano")

st.markdown("<p style='text-align:center; color:#444; font-size:10px; margin-top:10px;'>CONEXIÓN PALMETTO BAY ESTABLE</p>", unsafe_allow_html=True)

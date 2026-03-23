import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS RADICAL (Ajuste manual de altura para tu monitor) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; }
    
    /* Título */
    .header-369 { text-align: center; color: #d4af37; font-size: 1.5rem; text-shadow: 0 0 10px #d4af37; margin: 0; }

    /* IMAGEN: Forzamos a que sea pequeña para que el chat suba */
    .stImage > img {
        display: block;
        margin: 0 auto;
        max-height: 20vh !important; /* Ajuste manual: 20% de la pantalla */
        width: auto !important;
        border: 1px solid #d4af37;
    }

    /* Barras de Progreso */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 12px !important; }
    .label-prog { color: #d4af37; font-size: 0.9rem; text-align: center; margin: 0; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE AUDIO (Botón visible arriba a la derecha) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div id="trigger" onclick="document.getElementById('audio_core').play(); this.style.color='#00ff00'; this.innerText='[ PULSO ACTIVO ]'" 
                 style="position:fixed; top:20px; right:20px; color:#d4af37; cursor:pointer; border:2px solid #d4af37; padding:10px; z-index:9999; background:black; font-family:monospace; font-size:14px; border-radius:5px;">
                [ ACTIVAR AUDIO ]
            </div>
        """, unsafe_allow_html=True)

# --- 4. CONSTRUCCIÓN VISUAL ---
st.markdown("<div class='header-369'>SISTEMA AETERNA 369</div>", unsafe_allow_html=True)

# Imagen de la Cúpula
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# Tríada de Poder
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
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

# Chat de Comandos (Subido para que sea visible)
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
comando = st.text_input("COMANDO SOBERANO:", placeholder="Escribe al pulso de AETERNA...", key="input_final")

st.markdown("<p style='text-align:center; color:#333; font-size:10px;'>NODO 001 - PALMETTO BAY</p>", unsafe_allow_html=True)

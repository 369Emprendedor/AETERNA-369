import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS DE PRECISIÓN ABSOLUTA ---
st.markdown("""
<style>
    /* Fondo negro y eliminar scroll */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; }

    /* Ajuste de Imagen: Aquí es donde controlamos el monitor */
    .stImage > img {
        display: block;
        margin: 0 auto;
        max-height: 25vh !important; /* REDUCIDO AL 25% PARA SUBIR TODO */
        width: auto !important;
        border: 1px solid #d4af37;
    }

    /* Barras de progreso doradas */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 10px !important; }
    .label-prog { color: #d4af37; font-size: 0.8rem; text-align: center; font-family: monospace; margin: 0; }
    
    /* Input de Chat visible */
    .stTextInput > div > div > input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- BOTÓN DE AUDIO FLOTANTE ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div id="trigger" onclick="document.getElementById('audio_core').play(); this.innerText='[ PULSO ACTIVO ]'" 
                 style="position:fixed; top:15px; right:15px; color:#d4af37; cursor:pointer; border:1px solid #d4af37; padding:10px; z-index:9999; background:black; font-family:monospace; font-size:12px; border-radius:5px;">
                [ ACTIVAR AUDIO ]
            </div>
        """, unsafe_allow_html=True)

# --- CUERPO DEL SISTEMA ---
st.markdown("<h2 style='text-align:center; color:#d4af37; font-size:1.2rem; margin:0;'>SISTEMA AETERNA 369</h2>", unsafe_allow_html=True)

if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# Tríada de Poder (NVDA, ASML, CAPITAL)
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<p class='label-prog'>🌌 NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with col2:
    st.markdown("<p class='label-prog'>🔬 ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with col3:
    st.markdown("<p class='label-prog'>💰 CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# Input de Comandos
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
comando = st.text_input("ENVIAR PULSO A AETERNA:", placeholder="Escribe comando, Arquitecto...", key="cmd_soberano")

st.markdown("<p style='text-align:center; color:#333; font-size:9px; margin-top:5px;'>PALMETTO BAY SOBERANA</p>", unsafe_allow_html=True)

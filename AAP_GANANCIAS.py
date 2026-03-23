import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE COMPRESIÓN Y POSICIONAMIENTO ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    
    /* IMAGEN PANORÁMICA */
    .stImage > img {
        display: block; margin: 0 auto;
        max-height: 20vh !important; 
        width: 100% !important;
        object-fit: cover;
        border-bottom: 1px solid #d4af37;
    }

    /* BARRAS Y TEXTO */
    .stProgress { margin-top: -5px !important; }
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 6px !important; }
    .label-gold { color: #d4af37; font-size: 0.7rem; text-align: center; margin: 0; }
    
    /* CHAT */
    .stTextInput { margin-top: -10px !important; padding: 0 25% !important; }

    /* BOTÓN DE AUDIO: Ahora es un botón central abajo */
    .audio-footer-btn {
        display: block;
        width: 200px;
        margin: 10px auto; /* Lo centra y le da espacio arriba */
        padding: 8px;
        background: #000;
        color: #d4af37;
        border: 1px solid #d4af37;
        text-align: center;
        cursor: pointer;
        font-family: monospace;
        font-size: 12px;
        font-weight: bold;
        text-shadow: 0 0 5px #d4af37;
    }
    .audio-footer-btn:hover { background: #d4af37; color: #000; }
</style>
""", unsafe_allow_html=True)

# --- 3. CUERPO DE LA INTERFAZ ---
st.markdown("<h3 style='text-align:center; color:#d4af37; font-size:1rem; margin:0;'>AETERNA 369</h3>", unsafe_allow_html=True)

if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# Tríada
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<p class='label-gold'>NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with c2:
    st.markdown("<p class='label-gold'>ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with c3:
    st.markdown("<p class='label-gold'>CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# Chat
st.text_input("", placeholder="SISTEMA SOBERANO...", key="cmd_final")

# --- 4. MOTOR DE AUDIO (UBICADO AL FINAL) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-footer-btn" onclick="document.getElementById('audio_core').play(); this.innerText='PULSO ACTIVO'">
                ACTIVAR PULSO SONORO
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; font-size:8px; margin:0;'>PALMETTO BAY SOBERANA</p>", unsafe_allow_html=True)

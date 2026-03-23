import streamlit as st
import os
import base64

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS DE CONTROL (IMPLACABLE) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding-top: 0rem !important; }

    /* Imagen: Forzada al 25% de la altura del monitor */
    .stImage > img {
        display: block;
        margin: 0 auto;
        max-height: 25vh !important; 
        width: auto !important;
        border: 1px solid #d4af37;
    }

    /* Botón de Audio Centralizado */
    .audio-btn {
        display: block;
        width: 200px;
        margin: 10px auto;
        padding: 10px;
        border: 2px solid #d4af37;
        background: #000;
        color: #d4af37;
        text-align: center;
        cursor: pointer;
        font-family: monospace;
        font-weight: bold;
    }
    .audio-btn:hover { background: #d4af37; color: #000; }

    /* Barras de progreso */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 8px !important; }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<h2 style='text-align:center; color:#d4af37; margin-bottom:0;'>SISTEMA AETERNA 369</h2>", unsafe_allow_html=True)

# --- BOTÓN DE AUDIO (AHORA ESTÁ AQUÍ, EN EL CENTRO) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-btn" onclick="document.getElementById('audio_core').play(); this.innerText='[ LATIDO ACTIVO ]'">
                ACTIVAR PULSO 369
            </div>
        """, unsafe_allow_html=True)

# --- IMAGEN ---
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# --- TRÍADA DE PODER ---
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<p style='text-align:center; font-size:12px;'>🌌 NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with c2:
    st.markdown("<p style='text-align:center; font-size:12px;'>🔬 ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with c3:
    st.markdown("<p style='text-align:center; font-size:12px;'>💰 CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# --- CHAT ---
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
st.text_input("ENVIAR COMANDO:", placeholder="Escribe al pulso de AETERNA...", key="final_cmd")

st.markdown("<p style='text-align:center; color:#222; font-size:9px;'>PALMETTO BAY</p>", unsafe_allow_html=True)

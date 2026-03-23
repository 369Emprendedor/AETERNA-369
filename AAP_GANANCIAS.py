import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AETERNA 369", layout="centered", initial_sidebar_state="collapsed")

# --- CSS RADICAL (SIN COLUMNAS, TODO AL CENTRO) ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding-top: 1rem !important; max-width: 800px !important; }

    /* IMAGEN: Forzada a ser pequeña para que no empuje el resto */
    .stImage > img {
        display: block;
        margin: 0 auto;
        max-height: 35vh !important; 
        width: auto !important;
        border: 1px solid #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }

    /* Botón de Audio Estilo Dashboard */
    .audio-btn {
        background: #000;
        color: #d4af37;
        border: 2px solid #d4af37;
        padding: 10px 20px;
        text-align: center;
        margin: 10px auto;
        display: block;
        width: fit-content;
        cursor: pointer;
        font-family: monospace;
        font-weight: bold;
        text-shadow: 0 0 5px #d4af37;
    }

    /* Barras de progreso compactas */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 8px !important; }
    p { margin-bottom: 2px !important; font-size: 14px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<h3 style='text-align:center; color:#d4af37;'>SISTEMA AETERNA 369</h3>", unsafe_allow_html=True)

# --- BOTÓN DE AUDIO (JUSTO ARRIBA PARA QUE NO SE PIERDA) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-btn" onclick="document.getElementById('audio_core').play(); this.innerText='[ PULSO ACTIVO ]'">
                ACTIVA EL PULSO AQUÍ
            </div>
        """, unsafe_allow_html=True)

# --- IMAGEN CENTRAL ---
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# --- TRÍADA DE PODER (EN UNA SOLA FILA) ---
st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<p>🌌 NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with c2:
    st.markdown("<p>🔬 ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with c3:
    st.markdown("<p>💰 CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# --- COMANDOS ---
st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)
st.text_input("SISTEMA SOBERANO:", placeholder="Escribe al pulso de AETERNA...", key="cmd_v3")

st.markdown("<p style='color:#333; font-size:10px;'>PALMETTO BAY - NODO SOBERANO</p>", unsafe_allow_html=True)

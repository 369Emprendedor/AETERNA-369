import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS DE CONTROL TOTAL ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 1rem !important; }
    
    /* Forzar que todo esté centrado y quepa en el monitor */
    .main-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    /* IMAGEN: Aquí es donde ajustamos para que no tape las barras */
    .stImage > img {
        max-height: 35vh !important; /* Solo ocupa el 42% de la altura del monitor */
        width: auto !important;
        border: 1px solid #d4af37;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
    }

    /* Barras de progreso doradas */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 12px !important; }
    p { color: #d4af37 !important; font-family: monospace; margin-bottom: 2px !important; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# --- SISTEMA DE AUDIO (INYECTADO) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div onclick="document.getElementById('audio').play()" style="position:fixed; top:10px; right:10px; color:#d4af37; cursor:pointer; border:1px solid #d4af37; padding:5px; z-index:1000; font-size:10px;">
                [ ACTIVAR PULSO ]
            </div>
        """, unsafe_allow_html=True)

# --- CUERPO DE LA INTERFAZ ---
st.markdown("<h2 style='text-align:center; color:#d4af37;'>SISTEMA AETERNA 369 - NODO 001</h2>", unsafe_allow_html=True)

# 1. Imagen Central
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)

# 2. Tríada de Poder (Ahora en una fila horizontal clara)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<p style='text-align:center;'>🌌 NVDA (GPU)</p>", unsafe_allow_html=True)
    st.progress(95)
with col2:
    st.markdown("<p style='text-align:center;'>🔬 ASML (PHOTO)</p>", unsafe_allow_html=True)
    st.progress(100)
with col3:
    st.markdown("<p style='text-align:center;'>💰 CAPITAL (USD)</p>", unsafe_allow_html=True)
    st.progress(90)

# 3. Chat de Comandos (Visible al final)
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
st.text_input("Enviar pulso a AETERNA...", key="main_cmd", placeholder="Introduce comandos, Arquitecto...")

st.markdown("<p style='text-align:center; color:#333; font-size:10px;'>PALMETTO BAY SOBERANA</p>", unsafe_allow_html=True)

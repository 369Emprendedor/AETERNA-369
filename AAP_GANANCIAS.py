import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS DE CONTROL TOTAL (CENTRADO Y AJUSTADO) ---
st.markdown("""
<style>
    /* Forzar fondo negro y eliminar scroll */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 0rem !important; max-width: 100%; }

    /* Centrado de todo el contenido */
    .main-canvas {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
    }

    /* Título minimalista */
    .header-gold {
        color: #d4af37;
        font-size: 1.5rem;
        text-shadow: 0 0 10px #d4af37;
        margin-bottom: 10px;
        text-align: center;
    }

    /* IMAGEN: Ajuste dinámico al monitor */
    .centered-img {
        max-height: 50vh !important; /* Toma la mitad de la pantalla */
        border: 2px solid #d4af37;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
        margin-bottom: 20px;
    }

    /* Barras de progreso compactas */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; }
    .label-gold { color: #d4af37; font-size: 0.8rem; font-weight: bold; margin-bottom: 2px; }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE AUDIO (CON BOTÓN DE ACTIVACIÓN MANUAL) ---
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

# --- ESTRUCTURA VISUAL CENTRADA ---
st.markdown("<h1 class='header-gold'>SISTEMA AETERNA 369 - NODO 001</h1>", unsafe_allow_html=True)

# Columna central para agrupar imagen y barras
_, col_main, _ = st.columns([1, 2, 1])

with col_main:
    # Mostrar Imagen
    if os.path.exists("CUPULA_369.png"):
        st.image("CUPULA_369.png", use_container_width=True)
    
    # Espacio pequeño
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    # TRÍADA DE PODER (Ahora justo debajo de la imagen)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<p class='label-gold'>🌌 NVDA</p>", unsafe_allow_html=True)
        st.progress(95)
    with c2:
        st.markdown("<p class='label-gold'>🔬 ASML</p>", unsafe_allow_html=True)
        st.progress(100)
    with c3:
        st.markdown("<p class='label-gold'>💰 CAPITAL</p>", unsafe_allow_html=True)
        st.progress(90)

    # Chat integrado
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    st.text_input("Enviar pulso a AETERNA...", key="cmd", placeholder="Comandos del Arquitecto...")

st.markdown("<p style='text-align:center; color:#444; font-size:10px;'>SISTEMA SOBERANO ACTIVADO</p>", unsafe_allow_html=True)

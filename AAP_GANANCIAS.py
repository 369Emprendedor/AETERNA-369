import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (BLOQUEO DE SCROLL) ---
st.set_page_config(page_title="AETERNA 369 | 3D HUD", layout="wide", initial_sidebar_state="collapsed")

# --- 2. MOTOR DE GEOMETRÍA 3D (CSS) ---
st.markdown("""
<style>
    /* Bloqueo total de scroll para que todo quepa en tu pantalla HP */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
        height: 100vh !important;
        background-color: #000;
    }
    .main .block-container { padding: 0 !important; max-width: 100% !important; }

    /* EL LIENZO 3D */
    .viewport-3d {
        position: relative;
        width: 100vw;
        height: 100vh;
        perspective: 1200px; /* Crea profundidad */
    }

    /* EL VIDEO DE FONDO (LA CÚPULA VIVA) */
    .video-soberano {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover;
        z-index: 1;
        opacity: 0.7;
    }

    /* PANELES ACHICADOS CON INCLINACIÓN 3D */
    .panel-holograma {
        position: absolute;
        z-index: 10;
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #d4af37;
        padding: 10px;
        color: #d4af37;
        font-family: 'Courier New', monospace;
        backdrop-filter: blur(5px);
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        transition: all 0.5s;
    }

    /* PANEL IZQUIERDO (CAPITAL) - Inclinado hacia adentro */
    .p-izq {
        top: 15%; left: 10%; width: 220px;
        transform: rotateY(25deg) rotateX(5deg);
        border-left: 4px solid #d4af37;
    }

    /* PANEL DERECHO (NVDA/ASML) - Inclinado hacia adentro */
    .p-der {
        top: 15%; right: 10%; width: 220px;
        transform: rotateY(-25deg) rotateX(5deg);
        border-right: 4px solid #d4af37;
    }

    /* TERMINAL INFERIOR ACHICADA */
    .p-terminal {
        bottom: 10%; left: 30%; width: 40%;
        transform: rotateX(20deg);
        text-align: center;
    }

    /* BARRAS LÍQUIDAS LUMEN */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #d4af37, #fff, #d4af37) !important;
        background-size: 200% 100% !important;
        animation: flow 1.5s linear infinite !important;
        height: 4px !important;
    }
    @keyframes flow { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }

    /* INPUT TERMINAL */
    input {
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid #d4af37 !important;
        color: #d4af37 !important;
        text-align: center;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DE MEDIOS (VIDEO O IMAGEN) ---
st.markdown('<div class="viewport-3d">', unsafe_allow_html=True)

# Prioridad: Video para la vida 3D
video_path = "CUPULA_369.mp4"
image_path = "CUPULA_369.png"

if os.path.exists(video_path):
    with open(video_path, "rb") as f:
        v_b64 = base64.b64encode(f.read()).decode()
    st.markdown(f'<video autoplay loop muted class="video-soberano"><source src="data:video/mp4;base64,{v_b64}" type="video/mp4"></video>', unsafe_allow_html=True)
elif os.path.exists(image_path):
    with open(image_path, "rb") as f:
        i_b64 = base64.b64encode(f.read()).decode()
    st.markdown(f'<img src="data:image/png;base64,{i_b64}" class="video-soberano">', unsafe_allow_html=True)

# --- 4. RENDERIZADO DE PANELES 3D ---

# Izquierda: Capital
st.markdown("""
<div class='panel-holograma p-izq'>
    <div style='font-size:10px; opacity:0.6;'>CAPITAL ESTATUS</div>
    <div style='font-size:14px; font-weight:bold;'>SOBERANO</div>
    <div style='height:10px;'></div>
""", unsafe_allow_html=True)
st.progress(95)
st.markdown("</div>", unsafe_allow_html=True)

# Derecha: Infraestructura
st.markdown("""
<div class='panel-holograma p-der'>
    <div style='font-size:10px; opacity:0.6;'>INTELIGENCIA NVDA/ASML</div>
    <div style='font-size:14px; font-weight:bold;'>SYNC: 99.8%</div>
    <div style='height:10px;'></div>
""", unsafe_allow_html=True)
st.progress(98)
st.markdown("</div>", unsafe_allow_html=True)

# Terminal: Interceptor
st.markdown("<div class='panel-holograma p-terminal'>", unsafe_allow_html=True)
st.text_input("", placeholder="SISTEMA AETERNA AGUARDANDO...", key="cmd_3d")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Cierre Viewport

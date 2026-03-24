import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (HUD PANORÁMICO HP) ---
st.set_page_config(
    page_title="AETERNA 369 | FLOTANTE 3D", 
    layout="wide", # <-- Mantenemos el ancho para tener lienzo
    initial_sidebar_state="collapsed"
)

# --- 2. INYECTOR DE GEOMETRÍA FLOTANTE Y PROFUNDIDAD 3D (CSS) ---
st.markdown("""
<style>
    /* Reset total para eliminar márgenes de Streamlit */
    .stApp { 
        background-color: #000000; 
        color: #d4af37; 
        overflow: hidden !important; 
    }
    .block-container { padding: 0rem !important; max-width: 100% !important; margin: 0 !important; }

    /* CONTENEDOR MAESTRO DEL HUD (CANVAS TOTAL) */
    .hud-canvas {
        position: relative;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
    }

    /* CAPA 1: LA CÚPULA (FONDO COMPLETO, ADAPTADO) */
    .cupula-bg {
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        object-fit: cover; /* Estira para llenar el monitor */
        z-index: 1; /* Al fondo */
        opacity: 0.6; /* Transparencia para efecto inmersivo */
        filter: saturate(1.1) brightness(0.8) contrast(1.2);
    }

    /* CAPA 2: EL CONTENEDOR FLOTANTE CENTRAL (ACHICA LA INTERFAZ) */
    .flotante-central {
        position: absolute;
        z-index: 5; /* Por encima de la Cúpula */
        top: 10vh; /* Centrado verticalmente */
        left: 15vw; /* Centrado horizontalmente (deja ver bordes) */
        width: 70vw; /* <-- ESTO ACHICA LA INTERFAZ: Solo ocupa el 70% del ancho */
        height: 80vh; /* Ocupa el 80% del alto */
        display: flex;
        justify-content: space-between; /* Espacia los paneles laterales */
        align-items: flex-end; /* Alinea los paneles de progreso abajo */
        padding: 20px;
        # background: rgba(0,0,0,0.2); /* Úsalo para ver el contenedor si te pierdes */
    }

    /* ESTILO GENERAL DE ELEMENTOS HOLOGRÁFICOS FLOTANTES (EFECTO 3D) */
    .holo-panel {
        background: rgba(0, 0, 0, 0.75);
        border: 2px solid #d4af37;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.3), inset 0 0 10px rgba(212, 175, 55, 0.2);
        padding: 10px;
        font-family: 'Courier New', monospace;
        color: #d4af37;
        backdrop-filter: blur(8px);
        transform-style: preserve-3d; /* Obligatorio para 3D real */
    }

    /* Posicionamiento y Animación 3D de Paneles */
    .pane-l { width: 18vw; animation: floating-l 12s infinite ease-in-out; }
    .pane-r { width: 18vw; animation: floating-r 12s infinite ease-in-out; }
    
    @keyframes floating-l {
        0%, 100% { transform: translateZ(0) translateY(0) rotateY(-5deg); }
        50% { transform: translateZ(15px) translateY(-5px) rotateY(-2deg); }
    }
    @keyframes floating-r {
        0%, 100% { transform: translateZ(0) translateY(0) rotateY(5deg); }
        50% { transform: translateZ(15px) translateY(5px) rotateY(2deg); }
    }

    /* BARRAS DE PROGRESO LÍQUIDAS Y EFECTO DE VIDEO EN 3D */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #d4af37, #ffffff, #d4af37) !important;
        background-size: 200% 100% !important;
        animation: flow_lumen_3d 2s linear infinite, brightness_pulse 4s infinite alternate;
        height: 6px !important;
    }
    @keyframes flow_lumen_3d { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
    @keyframes brightness_pulse { 0% { filter: brightness(1); } 100% { filter: brightness(1.2); } }

    /* INPUT TERMINAL SOBERANA (CENTRAL INFERIOR) */
    .chat-terminal-3d {
        position: absolute;
        bottom: 5vh;
        left: 35vw;
        width: 30vw;
        text-align: center;
        z-index: 10;
        transform: translateZ(10px); /* Ligeramente adelante */
    }
    .stTextInput input {
        background-color: transparent !important;
        color: #d4af37 !important;
        border: none !important;
        border-bottom: 2px solid #d4af37 !important;
        font-size: 1.1rem !important;
        text-align: center;
        letter-spacing: 2px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. INICIO DEL CANVA MAESTRO ---
st.markdown("<div class='hud-canvas'>", unsafe_allow_html=True)

# CAPA 1: LA CÚPULA (FONDO ADAPTADO)
if os.path.exists("CUPULA_369.png"):
    with open("CUPULA_369.png", "rb") as f:
        data = f.read()
        b64_img = base64.b64encode(data).decode()
    st.markdown(f"<img src='data:image/png;base64,{b64_img}' class='cupula-bg'>", unsafe_allow_html=True)

# CAPA 2: EL CONTENEDOR FLOTANTE CENTRAL (ACHICADO TÁCTICAMENTE)
st.markdown("<div class='flotante-central'>", unsafe_allow_html=True)

# PANEL IZQUIERDO: CAPITAL (BALANCEO 3D)
st.markdown("<div class='holo-panel pane-l'>", unsafe_allow_html=True)
st.markdown("<div style='font-size: 12px; font-weight: bold;'>ESTATUS DE CAPITAL</div>", unsafe_allow_html=True)
st.markdown("<div style='margin-bottom: 10px; font-size: 10px;'>PODER SOBERANO</div>", unsafe_allow_html=True)
st.progress(95)
st.markdown("<div style='font-size: 9px; color: #00ff00; margin-top:5px;'>ESTADO: ONLINE</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# PANEL DERECHO: INTELIGENCIA (BALANCEO 3D)
st.markdown("<div class='holo-panel pane-r'>", unsafe_allow_html=True)
st.markdown("<div style='font-size: 12px; font-weight: bold;'>RED NVDA H100 | ASML EUV</div>", unsafe_allow_html=True)
st.markdown("<div style='margin-bottom: 10px; font-size: 10px;'>PRECISIÓN LITOGRÁFICA</div>", unsafe_allow_html=True)
st.progress(98)
st.markdown("<div style='font-size: 9px; margin-top:5px;'>SYNC: 99.8%</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# CIERRE DEL CONTENEDOR FLOTANTE CENTRAL
st.markdown("</div>", unsafe_allow_html=True)

# CAPA 3: TERMINAL DE CHAT (ANCLADA FUERA DEL FLOTANTE PARA NO MOVERSE CON ÉL)
st.markdown("<div class='chat-terminal-3d'>", unsafe_allow_html=True)
# Formulario vacío para posicionar el input de Streamlit aquí
with st.container():
    comando = st.text_input("AETERNA:", placeholder="Introduce comando de intercepción...", key="core_3d_integrated")
st.markdown("</div>", unsafe_allow_html=True)

# --- FIN DEL CANVA MAESTRO ---
st.markdown("</div>", unsafe_allow_html=True)

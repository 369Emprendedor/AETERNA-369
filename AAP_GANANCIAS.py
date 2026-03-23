import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA COMPACTA (UNA SOLA VISTA) ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS DE PRECISIÓN PARA ELIMINAR SCROLL ---
st.markdown("""
<style>
    /* 1. Eliminar márgenes y forzar altura completa del monitor */
    .block-container { 
        padding-top: 1rem !important; 
        padding-bottom: 0rem !important; 
        padding-left: 2rem !important; 
        padding-right: 2rem !important; 
        height: 100vh !important;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        overflow: hidden !important; /* Desactiva el scroll */
    }
    
    /* 2. Estilo de Fondo y Título */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .glow-title { 
        text-align: center; 
        color: #d4af37; 
        font-size: 20px !important; /* Título más pequeño */
        text-shadow: 0 0 10px #d4af37; 
        margin-bottom: 5px !important;
        margin-top: 0px !important;
    }
    
    /* 3. CONTROL TOTAL DE LA IMAGEN (AQUÍ ESTÁ LA CLAVE) */
    .stImage { 
        text-align: center; 
        margin-top: 0px !important;
        margin-bottom: 5px !important;
    }
    .stImage > img { 
        max-height: 40vh !important; /* Obliga a la imagen a medir solo el 40% de la altura de la pantalla */
        width: auto !important; /* Mantiene la proporción */
        margin-left: auto; 
        margin-right: auto; 
        border: 1px solid #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }

    /* 4. Estilo de barras y chat compactos */
    div[data-testid="stColumn"] p { font-size: 12px !important; margin-bottom: 0px !important; }
    .stTextInput>div>div>input { background-color: #111; color: #d4af37; border: 1px solid #d4af37; font-size: 12px !important; }
    .stProgress > div > div > div > div { background-color: #d4af37; height: 10px !important; }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO Y AUDIO DESACTIVADO TEMPORALMENTE ---
st.markdown("<h1 class='glow-title'>SISTEMA AETERNA 369 - NODO 001</h1>", unsafe_allow_html=True)

# --- IMAGEN REDIMENSIONADA (AQUÍ CORRE LA IMAGEN) ---
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png", use_container_width=False) # False para que no ocupe todo el ancho
else:
    st.warning("⚠️ Cargando matriz visual de la Cúpula...")

# --- LA TRÍADA DE PODER (COMPACTA) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<p style='text-align:center;'>🌌 NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with col2:
    st.markdown("<p style='text-align:center;'>🔬 ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with col3:
    st.markdown("<p style='text-align:center;'>💰 CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# --- CHAT AETERNA (VISIBLE Y COMPACTO) ---
st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True) # Pequeño espacio
st.text_input("Enviar pulso a AETERNA...", placeholder="Escribe tu comando aquí, Arquitecto...", key="chat_input")

st.markdown("<p style='text-align:center; font-size:10px; color:#555; margin-top:5px;'>PALMETTO BAY SOBERANA</p>", unsafe_allow_html=True)

import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (PANORÁMICA) ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE COMPRESIÓN VERTICAL EXTREMA Y EXPANSIÓN HORIZONTAL ---
st.markdown("""
<style>
    /* Forzar fondo negro y eliminar scroll del navegador */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    
    /* Eliminar TODOS los márgenes y paddings de Streamlit */
    .block-container { 
        padding: 0rem !important; 
        max-width: 100% !important; 
        margin: 0 !important;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }

    /* Título minimalistico y pegado arriba */
    .header-369 {
        text-align: center;
        color: #d4af37;
        font-size: 1.1rem;
        margin: 0;
        padding: 2px 0;
        text-shadow: 0 0 10px #d4af37;
    }

    /* BOTÓN DE AUDIO ULTRA-COMPACTO (Fijo arriba a la derecha) */
    .audio-btn {
        position: fixed; top: 2px; right: 2px;
        background: #000; color: #d4af37; border: 1px solid #d4af37;
        padding: 3px 6px; text-align: center; cursor: pointer;
        font-size: 9px; z-index: 1000;
    }

    /* IMAGEN: Compresión vertical extrema (25vh) y expansión horizontal (90%) */
    .stImage {
        text-align: center;
        width: 90% !important; /* Más ancho */
        margin: 0 auto;
        padding: 0;
    }
    .stImage > img {
        display: block;
        margin: 0 auto;
        max-height: 25vh !important; /* ULTRA-BAJO: Solo 25% del monitor */
        width: auto !important; /* Mantiene proporción */
        border: 1px solid #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }

    /* TABLERO DE DATOS (Pegado a la imagen) */
    .stProgress { margin-top: -8px !important; margin-bottom: 0 !important; } /* Sube las barras */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 6px !important; }
    .label-gold { color: #d4af37; font-size: 0.75rem; text-align: center; margin: 0; padding: 0; }
    
    /* CHAT DE COMANDOS (Compacto y pegado a las barras) */
    div[data-testid="stTextInput"] { 
        margin-top: -12px !important; 
        padding: 0 10px !important;
    }
    .stTextInput>div>div>input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        height: 1.2rem !important; /* Altura del chat más baja */
        font-size: 12px !important;
    }
    
    /* Pequeño espacio final */
    .footer-gold { text-align:center; color:#222; font-size:7px; margin-top: -5px; }

</style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE AUDIO (Flotante arriba a la derecha) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-btn" onclick="document.getElementById('audio_core').play(); this.innerText='[ PULSO ACTIVO ]'">
                [ ACTIVAR PULSO ]
            </div>
        """, unsafe_allow_html=True)

# --- 4. CONSTRUCCIÓN DE LA INTERFAZ ULTRA-COMPACTA ---
st.markdown("<div class='header-369'>SISTEMA AETERNA 369</div>", unsafe_allow_html=True)

# Contenedor para Imagen (con ancho expandido)
col_img = st.columns([0.5, 9, 0.5]) # Columnas [5%, 90%, 5%]
with col_img[1]:
    if os.path.exists("CUPULA_369.png"):
        st.image("CUPULA_369.png", use_container_width=True)

# Contenedor para Barras y Chat (Pegado a la imagen)
col_data = st.columns([1, 8, 1]) # Columnas [10%, 80%, 10%]
with col_data[1]:
    # Tríada de Poder (NVDA, ASML, CAPITAL)
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

    # Chat de Comandos (Subido y compacto)
    st.text_input("AETERNA:", placeholder="Comando del Arquitecto...", key="cmd_panoramic")

st.markdown("<div class='footer-gold'>PALMETTO BAY SOBERANA</div>", unsafe_allow_html=True)

import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA (EXPANSIÓN TOTAL) ---
st.set_page_config(
    page_title="AETERNA 369",
    layout="wide", # <-- Clave 1: Ocupar todo el ancho del monitor HP
    initial_sidebar_state="collapsed"
)

# --- 2. CSS DE CONTROL DE FRANJA PANORÁMICA ---
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
        font-size: 1rem;
        margin: 0;
        padding: 2px 0;
        text-shadow: 0 0 10px #d4af37;
        font-family: monospace;
    }

    /* IMAGEN: Compresión vertical extrema (25vh) y expansión horizontal (95%) */
    .img-box {
        text-align: center;
        width: 95% !important; /* <-- Clave 2: Panel casi al ancho total */
        margin: 0 auto;
        padding: 0;
    }
    .stImage > img {
        display: block;
        margin: 0 auto;
        max-height: 25vh !important; /* <-- Clave 3: Ultra-bajo, solo 30% de altura */
        width: auto !important; /* Mantiene proporción */
        border: 1px solid #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }

    /* TABLERO DE DATOS (Pegado a la imagen) */
    .stProgress { margin-top: -8px !important; margin-bottom: 0 !important; } /* Sube las barras */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 6px !important; }
    .label-gold { color: #d4af37; font-size: 0.7rem; text-align: center; margin: 0; padding: 0; font-family: monospace;}
    
    /* CHAT DE COMANDOS (Compacto y pegado a las barras) */
    div[data-testid="stTextInput"] { 
        margin-top: -10px !important; 
        padding: 0 15% !important; /* Centra el chat ligeramente */
    }
    .stTextInput>div>div>input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        height: 1.5rem !important; /* Altura del chat más baja */
        font-size: 12px !important;
    }
    
    /* BOTÓN DE AUDIO CENTRAL BAJO */
    .audio-trigger {
        display: block;
        width: 160px;
        margin: 5px auto;
        padding: 5px;
        background: #000;
        color: #d4af37;
        border: 1px solid #d4af37;
        text-align: center;
        cursor: pointer;
        font-family: monospace;
        font-size: 10px;
        font-weight: bold;
        text-shadow: 0 0 5px #d4af37;
    }
    .audio-trigger:hover { background: #d4af37; color: #000; }

</style>
""", unsafe_allow_html=True)

# --- 3. CONSTRUCCIÓN DE LA INTERFAZ PANORÁMICA ---

# A. Título pegado arriba
st.markdown("<div class='header-369'>SISTEMA AETERNA 369 - NODO SOBERANO</div>", unsafe_allow_html=True)

# B. Imagen de la Cúpula (Ancha y bajita)
with st.container():
    # Usamos columnas para forzar el ancho
    col_img = st.columns([0.25, 9.5, 0.25]) # [2.5%, 95%, 2.5%]
    with col_img[1]:
        if os.path.exists("CUPULA_369.png"):
            st.image("CUPULA_369.png", use_container_width=True)
        else:
            st.warning("Matriz visual de la Cúpula no encontrada.")

# C. Tríada de Poder (Fila única de datos)
with st.container():
    col_data = st.columns([1, 8, 1]) # Margen lateral del 10% para los datos
    with col_data[1]:
        # NVDA, ASML, CAPITAL
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

# D. Chat de Comandos (Pegado a las barras)
st.text_input("AETERNA:", placeholder="Introduce comandos del Arquitecto...", key="cmd_panoramic")


# E. MOTOR DE AUDIO (UBICADO AL FINAL Y CENTRAL)
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-trigger" onclick="document.getElementById('audio_core').play(); this.innerText='PULSO ACTIVADO'">
                ACTIVAR PULSO SONORO
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; font-size:7px; margin:0;'>PALMETTO BAY</p>", unsafe_allow_html=True)

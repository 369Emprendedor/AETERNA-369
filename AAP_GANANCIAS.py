import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE COMPRESIÓN VERTICAL ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding-top: 0.5rem !important; padding-bottom: 0rem !important; }
    
    /* Título mini para ahorrar espacio */
    .header-369 { text-align: center; color: #d4af37; font-size: 1.2rem; margin-bottom: 2px; }

    /* BOTÓN DE AUDIO COMPACTO */
    .audio-btn {
        background: #000; color: #d4af37; border: 1px solid #d4af37;
        padding: 5px 10px; text-align: center; margin: 0 auto 5px auto;
        display: block; width: fit-content; cursor: pointer; font-size: 10px;
    }

    /* IMAGEN: Altura ajustada para subir el tablero */
    .stImage > img {
        display: block; margin: 0 auto;
        max-height: 40vh !important; /* Ajuste fino de altura */
        width: auto !important;
        border: 1px solid #d4af37;
    }

    /* BARRAS: Pegadas a la imagen */
    .stProgress { margin-top: -10px !important; } /* Sube las barras hacia la imagen */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 8px !important; }
    .label-gold { color: #d4af37; font-size: 0.8rem; text-align: center; margin-top: 5px; }
    
    /* CHAT: Subido y pegado a las barras */
    div[data-testid="stForm"] { margin-top: -15px !important; }
    .stTextInput { margin-top: -10px !important; }
</style>
""", unsafe_allow_html=True)

# --- 3. AUDIO ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-btn" onclick="document.getElementById('audio_core').play(); this.innerText='[ LATIDO ACTIVO ]'">
                ACTIVAR PULSO
            </div>
        """, unsafe_allow_html=True)

# --- 4. INTERFAZ ---
st.markdown("<div class='header-369'>SISTEMA AETERNA 369</div>", unsafe_allow_html=True)

# Imagen
col_img = st.columns([1, 8, 1])
with col_img[1]:
    if os.path.exists("CUPULA_369.png"):
        st.image("CUPULA_369.png", use_container_width=True)

# Tablero de Datos (Pegado a la imagen)
col_data = st.columns([1.5, 7, 1.5])
with col_data[1]:
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

    # Chat (Pegado a las barras)
    st.text_input("AETERNA:", placeholder="Comando...", key="cmd_v5")

st.markdown("<p style='text-align:center; color:#222; font-size:8px;'>NODO 001</p>", unsafe_allow_html=True)

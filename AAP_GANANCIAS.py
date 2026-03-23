import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE COMPRESIÓN EXTREMA ---
st.markdown("""
<style>
    /* Fondo y eliminar scroll */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    
    /* Eliminar espacios de Streamlit */
    .block-container { padding: 0rem !important; max-width: 100% !important; }
    div[data-testid="stVerticalBlock"] > div { padding: 0px !important; margin: 0px !important; gap: 0rem !important; }

    /* Título minimalista pegado arriba */
    .header-369 { text-align: center; color: #d4af37; font-size: 1rem; margin: 0; padding: 2px; }

    /* IMAGEN: Ahora es una franja panorámica (18% de altura) */
    .stImage > img {
        display: block; margin: 0 auto;
        max-height: 18vh !important; /* REDUCCIÓN TOTAL DE ALTURA */
        width: 100% !important; /* Ocupa todo el ancho disponible */
        object-fit: cover; /* Recorta para mantener la franja */
        border-bottom: 1px solid #d4af37;
    }

    /* BARRAS: Pegadas a la imagen sin aire */
    .stProgress { margin-top: -5px !important; }
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 6px !important; }
    .label-gold { color: #d4af37; font-size: 0.7rem; text-align: center; margin: 0; line-height: 1; }
    
    /* CHAT: Compacto y pegado arriba */
    .stTextInput { margin-top: -10px !important; padding: 0 20% !important; }
    .stTextInput>div>div>input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #333 !important;
        height: 1.5rem !important;
    }

    /* Botón de Audio Flotante */
    .audio-btn {
        position: fixed; top: 5px; right: 5px;
        background: #000; color: #d4af37; border: 1px solid #d4af37;
        padding: 2px 5px; cursor: pointer; font-size: 8px; z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. MOTOR DE AUDIO ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-btn" onclick="document.getElementById('audio_core').play(); this.innerText='PULSO ON'">
                AUDIO OFF/ON
            </div>
        """, unsafe_allow_html=True)

# --- 4. INTERFAZ COLAPSADA ---
st.markdown("<div class='header-369'>AETERNA 369</div>", unsafe_allow_html=True)

# Imagen Panorámica
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# Tríada de Poder (Fila única sin espacios)
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

# Chat de Comandos (Subido al máximo)
st.text_input("", placeholder="COMANDO...", key="cmd_ultra_low")

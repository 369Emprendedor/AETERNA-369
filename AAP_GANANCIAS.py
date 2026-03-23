import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS DE INTEGRACIÓN Y COMPRESIÓN VERTICAL EXTREMA ---
st.markdown("""
<style>
    /* Forzar fondo negro absoluto y eliminar scroll */
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 0.5rem !important; max-width: 100% !important; margin: 0 !important; }

    /* Forzar diseño vertical centrado */
    [data-testid="stVerticalBlock"] > div { padding: 0px !important; margin: 0px !important; gap: 0rem !important; display: flex; flex-direction: column; align-items: center; }

    /* Título minimalistico y pegado arriba */
    .header-369 { text-align: center; color: #d4af37; font-size: 1rem; margin: 0; padding: 2px; font-family: monospace; text-shadow: 0 0 10px #d4af37; }

    /* IMAGEN: Ahora es una franja ultra-ancha que se expanda horizontalmente */
    .stImage > img {
        display: block; margin: 0 auto;
        max-height: 18vh !important; /* Altura ultra-baja */
        width: 100% !important; /* Ocupa todo el ancho */
        object-fit: cover; /* Recorta para mantener la franja panorámica */
        border-bottom: 1px solid #d4af37;
    }

    /* BARRAS Y CHAT: Integrados directamente debajo sin espacios */
    .stProgress { margin-top: -8px !important; margin-bottom: 0 !important; } /* Sube las barras */
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 6px !important; }
    .label-gold { color: #d4af37; font-size: 0.75rem; text-align: center; margin: 0; padding: 0; font-family: monospace;}
    
    /* CHAT DE COMANDOS: Compacto y pegado a las barras */
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

    /* Botón de Audio Flotante */
    .audio-btn {
        position: fixed; top: 5px; right: 5px;
        background: #000; color: #d4af37; border: 1px solid #d4af37;
        padding: 2px 5px; cursor: pointer; font-size: 8px; z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# --- SISTEMA DE AUDIO (INYECTADO) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <audio id="audio" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-btn" onclick="document.getElementById('audio').play(); this.innerText='PULSO ON'">
                AUDIO ON
            </div>
        """, unsafe_allow_html=True)

# --- CUERPO DE LA INTERFAZ INTEGRADA ---
st.markdown("<div class='header-369'>AETERNA 369 - NODO ACTIVADO</div>", unsafe_allow_html=True)

# Imagen Panorámica Ultra-ancha
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

# Tríada de Poder (Fila única de datos pegada a la imagen)
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

# Chat de Comandos (Subido y compacto)
comando = st.text_input("AETERNA:", placeholder="Introduce comandos, Arquitecto...", key="cmd_integrated")

st.markdown("<p style='text-align:center; color:#222; font-size:7px; margin-top: -5px;'>NODO SOBERANO SINCRO</p>", unsafe_allow_html=True)

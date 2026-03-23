import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CSS DE DISEÑO PANORÁMICO Y COMPACTO ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden !important; }
    .block-container { padding: 0.5rem !important; max-width: 100% !important; }

    /* Imagen Panorámica */
    .stImage > img {
        display: block; margin: 0 auto;
        max-height: 22vh !important; 
        width: 90% !important;
        object-fit: contain;
        border: 1px solid #d4af37;
    }

    /* Barras y Chat Pegados */
    .stProgress { margin-top: -10px !important; }
    .stProgress > div > div > div > div { background-color: #d4af37 !important; height: 6px !important; }
    .label-gold { color: #d4af37; font-size: 0.75rem; text-align: center; margin: 0; font-family: monospace; }
    
    .stTextInput { margin-top: -10px !important; padding: 0 20% !important; }
    .stTextInput>div>div>input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        height: 1.6rem !important;
    }

    /* Botón de Audio Centralizado Abajo */
    .audio-trigger {
        display: block; width: 180px; margin: 15px auto; padding: 8px;
        background: #000; color: #d4af37; border: 1px solid #d4af37;
        text-align: center; cursor: pointer; font-family: monospace;
        font-size: 11px; font-weight: bold; border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:#d4af37; font-size:1.1rem; margin:0;'>AETERNA 369</h3>", unsafe_allow_html=True)

# --- 3. VERIFICACIÓN DE IMAGEN ---
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")
else:
    st.markdown("<p style='text-align:center; color:gray; font-size:10px;'>[ MATRIZ VISUAL EN ESPERA DE SINCRONIZACIÓN ]</p>", unsafe_allow_html=True)

# --- 4. TABLERO DE DATOS ---
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

st.text_input("", placeholder="COMANDO SOBERANO...", key="final_cmd")

# --- 5. MOTOR DE AUDIO REFORZADO ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-trigger" id="btn-audio"
                 onclick="var a=document.getElementById('audio_core'); a.play(); this.innerText='PULSO ACTIVO'; this.style.color='#00ff00';">
                ACTIVAR PULSO SONORO
            </div>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align:center; color:#333; font-size:9px;'>PULSO SONORO NO DETECTADO</p>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; font-size:8px;'>PALMETTO BAY SOBERANA</p>", unsafe_allow_html=True)

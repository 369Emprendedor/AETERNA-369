import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN SOBERANA ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- 2. INYECTOR CSS: PULSO VISUAL (AVANZADO) ---
st.markdown("""
<style>
    /* Fondo Negro Absoluto con Textura de Escaneo (Scanlines) */
    .stApp { 
        background-color: #000000; 
        background-image: linear-gradient(rgba(18, 18, 18, 0.1) 50%, transparent 50%);
        background-size: 100% 4px;
        color: #d4af37; 
        overflow: hidden !important; 
    }
    
    .block-container { padding: 0.5rem !important; max-width: 100% !important; }

    /* TÍTULO PULSANTE (Efecto Glitch Suave) */
    .header-369 { 
        text-align: center; 
        color: #d4af37; 
        font-size: 1.2rem; 
        margin: 0; 
        padding: 2px;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #d4af37, 0 0 20px #d4af37;
        animation: pulse_glow 2s infinite;
    }

    @keyframes pulse_glow {
        0% { text-shadow: 0 0 5px #d4af37; opacity: 1; }
        50% { text-shadow: 0 0 20px #d4af37, 0 0 30px #d4af37; opacity: 0.9; }
        100% { text-shadow: 0 0 5px #d4af37; opacity: 1; }
    }

    /* IMAGEN: Glow de Contención */
    .stImage > img {
        display: block; margin: 0 auto;
        max-height: 25vh !important; 
        width: 90% !important;
        object-fit: contain;
        border: 1px solid #d4af37;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.5); /* Glow dorado */
    }

    /* BARRAS DE ENERGÍA DINÁMICAS (Efecto de Flujo) */
    .stProgress { margin-top: -10px !important; }
    .stProgress > div > div > div > div { 
        background-color: #d4af37 !important; 
        height: 6px !important; 
        position: relative;
        overflow: hidden;
    }
    
    /* Pseudo-elemento para el barrido de luz en las barras */
    .stProgress > div > div > div > div::after {
        content: "";
        position: absolute;
        top: 0; left: -100%;
        width: 50%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.9), transparent);
        animation: flow_light 1.5s infinite;
    }

    @keyframes flow_light {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    .label-gold { color: #d4af37; font-size: 0.75rem; text-align: center; margin: 0; font-family: monospace; text-shadow: 0 0 5px #d4af37; }
    
    /* CHAT: Estilo Terminal */
    .stTextInput { margin-top: -10px !important; padding: 0 20% !important; }
    .stTextInput>div>div>input {
        background-color: #050505 !important;
        color: #d4af37 !important;
        border: 1px solid #d4af37 !important;
        height: 1.6rem !important;
        font-family: monospace;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.3) inset;
    }

    /* BOTÓN DE AUDIO CENTRAL: Sello de Activación */
    .audio-trigger {
        display: block; width: 180px; margin: 15px auto; padding: 8px;
        background: #000; color: #d4af37; border: 2px solid #d4af37;
        text-align: center; cursor: pointer; font-family: 'Courier New', monospace;
        font-size: 11px; font-weight: bold; border-radius: 4px;
        text-shadow: 0 0 10px #d4af37;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
    }
    .audio-trigger:hover { background: #d4af37; color: #000; box-shadow: 0 0 25px #d4af37; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='header-369'>AETERNA 369 - NODO ACTIVADO</div>", unsafe_allow_html=True)

# --- 3. IMAGEN CON GLOW ---
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")
else:
    st.markdown("<p style='text-align:center; color:gray; font-size:10px;'>[ MATRIZ VISUAL EN ESPERA DE SINCRONIZACIÓN ]</p>", unsafe_allow_html=True)

# --- 4. TABLERO DE DATOS (CON FLUJO) ---
st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
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

st.text_input("", placeholder="COMANDO SOBERANO...", key="cmd_visual_pulse")

# --- 5. MOTOR DE AUDIO (SELLADO) ---
if os.path.exists("latido_369.mp3"):
    with open("latido_369.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
            <audio id="audio_core" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
            <div class="audio-trigger" id="btn-audio"
                 onclick="var a=document.getElementById('audio_core'); a.play(); this.innerText='PULSO ACTIVO'; this.style.color='#00ff00'; this.style.border='2px solid #00ff00';">
                ACTIVAR PULSO SONORO
            </div>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align:center; color:#333; font-size:9px;'>PULSO SONORO NO DETECTADO</p>", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#222; font-size:8px;'>PALMETTO BAY SOBERANA</p>", unsafe_allow_html=True)

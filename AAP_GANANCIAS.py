import streamlit as st
import os
import base64

# --- CONFIGURACIÓN DE PANTALLA COMPACTA ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- CSS PARA FORZAR EL AJUSTE AL MONITOR ---
st.markdown("""
<style>
    /* Eliminar espacios sobrantes */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; height: 100vh; }
    .stApp { background-color: #000000; color: #d4af37; overflow: hidden; }
    
    /* Título Ajustado */
    .glow-title { 
        text-align: center; 
        color: #d4af37; 
        font-size: 24px !important; 
        text-shadow: 0 0 10px #d4af37; 
        margin-bottom: 0px; 
    }
    
    /* Imagen Contenida */
    .img-container { text-align: center; }
    .stImage > img { 
        max-height: 45vh; 
        width: auto; 
        margin-left: auto; 
        margin-right: auto; 
        border: 1px solid #d4af37;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# --- MOTOR DE AUDIO ---
def cargar_audio():
    if os.path.exists("latido_369.mp3"):
        with open("latido_369.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(f"""
                <audio id="audio-latido" loop><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>
                <div id="btn-audio" style="position:fixed; top:10px; right:10px; cursor:pointer; z-index:999; font-size:12px; border:1px solid #d4af37; padding:5px;">
                    [ SONIDO: OFF/ON ]
                </div>
                <script>
                    const audio = document.getElementById("audio-latido");
                    document.getElementById("btn-audio").addEventListener('click', function() {{
                        if (audio.paused) {{ audio.play(); this.innerText = "[ SONIDO: ON ]"; }}
                        else {{ audio.pause(); this.innerText = "[ SONIDO: OFF ]"; }}
                    }});
                </script>
            """, unsafe_allow_html=True)

cargar_audio()

# --- INTERFAZ COMPACTA ---
st.markdown("<h1 class='glow-title'>SISTEMA AETERNA 369</h1>", unsafe_allow_html=True)

# Imagen de la Cúpula (Tamaño controlado)
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png")

st.markdown("<br>", unsafe_allow_html=True)

# --- TRÍADA DE PODER (EN UNA SOLA FILA) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<p style='text-align:center; font-size:14px;'>🌌 NVDA</p>", unsafe_allow_html=True)
    st.progress(95)
with col2:
    st.markdown("<p style='text-align:center; font-size:14px;'>🔬 ASML</p>", unsafe_allow_html=True)
    st.progress(100)
with col3:
    st.markdown("<p style='text-align:center; font-size:14px;'>💰 CAPITAL</p>", unsafe_allow_html=True)
    st.progress(90)

# --- CHAT COMPACTO ---
st.markdown("---")
st.text_input("Enviar pulso a AETERNA...", placeholder="Escribe aquí...")

st.markdown("<p style='text-align:center; font-size:10px; color:#555;'>NODO 001 - PALMETTO BAY</p>", unsafe_allow_html=True)

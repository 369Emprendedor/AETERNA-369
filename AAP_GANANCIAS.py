import streamlit as st
import os
import base64
from openai import OpenAI

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="AETERNA 369", layout="wide", initial_sidebar_state="collapsed")

# --- MOTOR DE AUDIO (VERSIÓN INYECTADA) ---
def reproducir_latido():
    file_path = "latido_369.mp3"
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # HTML directo con script de auto-reproducción al primer clic en cualquier parte
            audio_html = f"""
                <audio id="miAudio" loop>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <div id="click-layer" style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;cursor:pointer;display:block;">
                    <p style="color:#d4af37; text-align:center; margin-top:20%; font-family:monospace;">
                        [ CLICK PARA ACTIVAR PULSO SOBERANO ]
                    </p>
                </div>
                <script>
                    const layer = document.getElementById('click-layer');
                    const audio = document.getElementById('miAudio');
                    layer.addEventListener('click', function() {{
                        audio.play();
                        layer.style.display = 'none'; // Desaparece el mensaje tras el clic
                    }});
                </script>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    else:
        st.error("Archivo latido_369.mp3 no encontrado en el servidor.")

# --- ESTILO ---
st.markdown("<style>.stApp { background-color: #000000; color: #d4af37; }</style>", unsafe_allow_html=True)

# ACTIVAR AUDIO PRIMERO
reproducir_latido()

# --- CONTENIDO VISUAL ---
st.markdown("<h1 style='text-align:center; color:#d4af37; text-shadow: 0 0 15px #d4af37;'>SISTEMA AETERNA 369</h1>", unsafe_allow_html=True)

if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png", use_container_width=True)

st.markdown("---")

# --- LA TRÍADA DE PODER ---
col1, col2, col3 = st.columns(3)
with col1:
    st.write("🌌 **NVDA (GPU)**")
    st.progress(95)
with col2:
    st.write("🔬 **ASML (LITOGRAFÍA)**")
    st.progress(100)
with col3:
    st.write("💰 **CAPITAL SOBERANO**")
    st.progress(90)

st.markdown("---")

# --- CHAT ---
API_KEY = "TU_CLAVE_AQUI" 
if API_KEY == "TU_CLAVE_AQUI":
    st.warning("⚠️ Esperando conexión neuronal (API Key).")
else:
    # (Aquí iría el resto del código del chat que ya tienes)
    st.success("Cerebro conectado.")

if st.button("🔄 REINICIAR CÚPULA"):
    st.rerun()

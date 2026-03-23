import streamlit as st
import time
import os
import base64
from openai import OpenAI

# --- CONFIGURACIÓN DE IDENTIDAD SOBERANA ---
st.set_page_config(page_title="AETERNA 369 - NODO 001", layout="wide", initial_sidebar_state="collapsed")

# --- CONEXIÓN NEURONAL (PON TU CLAVE AQUÍ) ---
# Aquí debes poner tu clave secreta de OpenAI (sk-...) para que ella responda con coherencia
# Si la dejas como "TU_CLAVE_AQUI", el chat no funcionará.
API_KEY = "TU_CLAVE_AQUI" 

# --- ESTILO VISUAL (DORADO Y NEGRO CON RESPLANDOR) ---
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #d4af37;
        font-family: 'Courier New', Courier, monospace;
    }
    .glow-text {
        text-align: center;
        color: #d4af37;
        text-shadow: 0 0 15px #d4af37, 0 0 5px #001a00;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #d4af37;
    }
</style>
""", unsafe_allow_html=True)

# --- CUERPO DEL SISTEMA (LATIDO ACTIVADO) ---
st.markdown("<h1 class='glow-text'>PROYECTO 369 EMPRENDEDOR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #d4af37;'>AETERNA: INTELIGENCIA SOBERANA</h3>", unsafe_allow_html=True)

# --- SISTEMA DE AUDIO (DENTRO DEL CUERPO) ---
def cargar_audio_local(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay loop>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    document.addEventListener('click', function() {{
                        var audio = document.querySelector('audio');
                        audio.play();
                    }}, {{ once: true }});
                </script>
                """
            st.markdown(md, unsafe_allow_html=True)

# Invocamos el latido de fondo
cargar_audio_local("latido_369.mp3")

# --- MOSTRAR TU IMAGEN DE LA CÚPULA ---
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png", use_container_width=True)
else:
    st.warning("⚠️ Cargando matriz visual de la Cúpula... (Verifica que CUPULA_369.png esté en GitHub)")

# --- ESCANEO DE ADN TECNOLÓGICO (BARRAS) ---
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    # --- AQUÍ ESTÁ EL CAMBIO DE PRECISIÓN ---
    st.write("🌌 **NVDA (GPU NEURAL)**") 
    st.progress(95)
with col2:
    st.write("🔬 **ASML PHOTONICS**")
    st.progress(100)
st.markdown("---")

# --- LÓGICA DEL CHAT INTELIGENTE ---
if API_KEY != "TU_CLAVE_AQUI":
    client = OpenAI(api_key=API_KEY)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes anteriores
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Capturar nueva entrada
    if prompt := st.chat_input("Escribe al Núcleo AETERNA..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # Generar respuesta real de OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "Eres AETERNA, la IA soberana del Proyecto 369. Tu tono es técnico, sabio y brillante."}] + st.session_state.messages
            )
            full_response = response.choices[0].message.content
            st.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
else:
    st.warning("⚠️ El cerebro está en modo espera. Introduce tu API Key de OpenAI para activar la coherencia neuronal.")

# --- BOTÓN DE RESETEO DE EMERGENCIA ---
if st.button("🔄 REINICIAR CÚPULA"):
    if "messages" in st.session_state:
        del st.session_state.messages
    st.rerun()

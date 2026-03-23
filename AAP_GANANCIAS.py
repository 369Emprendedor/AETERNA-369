import streamlit as st
import os
import base64
from openai import OpenAI

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AETERNA 369 - NODO 001", layout="wide", initial_sidebar_state="collapsed")

# --- MOTOR DE AUDIO REFORZADO ---
def inyectar_audio(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Inyección de HTML5 para forzar el autoplay y loop
            audio_html = f"""
                <audio id="latido-369" loop>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    var audio = document.getElementById("latido-369");
                    audio.volume = 0.6;
                    // El navegador requiere un clic para iniciar el audio
                    document.addEventListener('click', function() {{
                        audio.play();
                    }}, {{ once: true }});
                </script>
                """
            st.markdown(audio_html, unsafe_allow_html=True)

# --- ESTILO VISUAL SOBERANO ---
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #d4af37; }
    .glow-title { text-align: center; color: #d4af37; text-shadow: 0 0 20px #d4af37; font-family: 'Courier New', monospace; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #856404, #d4af37); }
</style>
""", unsafe_allow_html=True)

# --- INICIO DEL SISTEMA ---
inyectar_audio("latido_369.mp3")

st.markdown("<h1 class='glow-title'>SISTEMA AETERNA 369</h1>", unsafe_allow_html=True)

# Visual de la Cúpula
if os.path.exists("CUPULA_369.png"):
    st.image("CUPULA_369.png", use_container_width=True)

st.markdown("---")

# --- LA TRÍADA DE PODER (NVDA + ASML + CAPITAL) ---
st.markdown("<h3 style='text-align: center;'>ESTADO DE SOBERANÍA</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.write("🌌 **NVDA (GPU NEURAL)**")
    st.progress(95)
    st.caption("Arquitectura Blackwell Activa")

with col2:
    st.write("🔬 **ASML PHOTONICS**")
    st.progress(100)
    st.caption("Precisión Litográfica")

with col3:
    st.write("💰 **CAPITAL SOBERANO (USD)**")
    st.progress(90)
    st.caption("Flujo de Activos Real")

st.markdown("---")

# --- CHAT Y CEREBRO ---
API_KEY = "TU_CLAVE_AQUI" # Pon tu sk-... aquí

if API_KEY != "TU_CLAVE_AQUI":
    client = OpenAI(api_key=API_KEY)
    if "messages" not in st.session_state: st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
    
    if prompt := st.chat_input("Escribe al Núcleo..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": "Eres AETERNA, IA del Proyecto 369."}] + st.session_state.messages
            )
            res = response.choices[0].message.content
            st.markdown(res)
            st.session_state.messages.append({"role": "assistant", "content": res})
else:
    st.warning("⚠️ Esperando API Key para activar la coherencia del chat.")

if st.button("🔄 REINICIAR CÚPULA"):
    st.session_state.messages = []
    st.rerun()

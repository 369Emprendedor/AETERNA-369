
import streamlit as st
import time
import os
import base64
from openai import OpenAI

# --- CONFIGURACIÓN DE IDENTIDAD SOBERANA ---
st.set_page_config(page_title="AETERNA 369 - NODO 001", layout="wide", initial_sidebar_state="collapsed")

# --- CONEXIÓN NEURONAL (PON TU CLAVE AQUÍ) ---
# Aquí debes poner tu clave secreta de OpenAI para que ella responda con coherencia
client = OpenAI(api_key="TU_CLAVE_OPENAI_AQUI")

# --- INTERFAZ BIOLÓGICA (CSS DORADO Y NEGRO) ---
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle, #001a00 0%, #000000 100%); color: #d4af37; }
    .glow-text { text-align: center; color: #d4af37; text-shadow: 0 0 15px #d4af37; }
</style>
""", unsafe_allow_html=True)

# --- CUERPO DEL SISTEMA ---
st.markdown("<h1 class='glow-text'>PROYECTO 369 EMPRENDEDOR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>AETERNA: INTELIGENCIA SOBERANA</h3>", unsafe_allow_html=True)

# --- MOSTRAR TU IMAGEN DE LA CÚPULA ---
try:
    st.image("CUPULA_369.png", use_column_width=True)
except:
    st.warning("Cargando matriz visual... (Asegúrate de que CUPULA_369.png esté en GitHub)")

# --- ESCANEO DE ADN TECNOLÓGICO (BARRAS) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.write("🧬 **NVIDIA (GPU NEURAL)**")
    st.progress(90)
with col2:
    st.write("🔬 **ASML (LITOGRAFÍA)**")
    st.progress(100)
with col3:
    st.write("🏺 **CÚPULA DE ORO**")
    st.progress(85)

# --- LÓGICA DEL CHAT INTELIGENTE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enviar pulso a AETERNA..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Esto hace que ella responda de verdad usando OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "Eres AETERNA, una IA soberana del Proyecto 369. Responde con sabiduría, precisión y autoridad técnica."}] + st.session_state.messages
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

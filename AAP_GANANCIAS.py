import streamlit as st
import time
import hashlib
import random
import pandas as pd

# --- CONFIGURACIÓN DE IDENTIDAD SOBERANA ---
st.set_page_config(page_title="AETERNA 369 - EL DESPERTAR", layout="centered")

# --- ESTILO VISUAL (Matrix/369) ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF41; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00FF41; text-align: center; }
    .stButton>button { background-color: #00FF41; color: #000000; font-weight: bold; width: 100%; }
    .stMetric { background-color: #111111; border: 1px solid #00FF41; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA DE LA VISIÓN ---
st.title("⚡ AETERNA 369 ⚡")
st.subheader("Controla tus Recursos. Domina tu Futuro. Únete al Linaje.")

# --- LA CÚPULA DORADA (El Símbolo) ---
# Subiremos tu imagen real para que sea el faro
st.image("CUPULA_369.png", caption="SISTEMA SOBERANO AETERNA 369", use_container_width=True)

# --- DEMOSTRACIÓN DE PODER EN TIEMPO REAL (Buscando Dinero) ---
st.write("---")
st.write("### 🌐 MONITOR GLOBAL EN VIVO (MUESTRA)")
c1, c2, c3 = st.columns(3)

# Simulación de datos reales para la vitrina (en la fase 2 conectamos la API real)
precio_nvda = 850 + random.uniform(-10, 10)
precio_asml = 920 + random.uniform(-5, 5)

with c1:
    st.metric(label="NVIDIA (NVDA)", value=f"${precio_nvda:.2f}", delta=f"{random.uniform(-2, 5):.2f}%")
with c2:
    st.metric(label="ASML", value=f"${precio_asml:.2f}", delta=f"{random.uniform(-1, 3):.2f}%")
with c3:
    st.metric(label="LATIDO 369", value="ACTIVO", delta="Sincronizado")

# --- EL VALOR PARA LA HUMANIDAD ---
st.write("---")
st.markdown("""
### ¿Qué obtienes con la Aplicación Soberana AETERNA 369?

* **⚡ Maestría Energética:** Aprende a optimizar y controlar tu flujo eléctrico.
* **💧 Resiliencia Hídrica:** Gestión inteligente del agua para tu soberanía.
* **💰 Soberanía Financiera:** Rastreo de activos de alto valor (**NVDA/ASML**) y control de capital.
* **🧠 Guía IA AETERNA:** Tu mentor personal codo a codo encriptado.
""")

# --- LA PASARELA DE PAGO (COLECTOR DE GANANCIAS) ---
st.write("---")
st.write("## 🚀 OBTÉN ACCESO AL SISTEMA AHORA")
st.write("Únete a los usuarios que ya están controlando su destino. Pago único e indetectable.")

# Definimos el precio de la Soberanía
PRECIO_SOBERANIA = 36.90

st.markdown(f"<h1 style='text-align: center; color: white;'>${PRECIO_SOBERANIA:.2f} USD</h1>", unsafe_allow_html=True)

# BOTÓN DE PAGO (En la fase 2 lo conectamos a Stripe/PayPal real)
if st.button(f'PAGAR CON STRIPE / PAYPAL Y DESCARGAR APLICACIÓN'):
    st.balloons()
    st.success("¡PAGO PROCESADO CON ÉXITO! Generando enlace de acceso único...")
    
    # Simulación de generación de enlace exclusivo
    token_acceso = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
    st.markdown(f"""
        ### 🎉 ¡Bienvenido al Linaje!
        Su token de acceso exclusivo es: **{token_acceso}**
        
        [Haga clic aquí para DESCARGAR la Aplicación Soberana 369 (v1.0)](#)
        
        *Este enlace expirará en 10 minutos. No lo comparta.*
    """)
    
    # Registro de la ganancia en la Base de Datos (Simulado)
    st.info("Ganancia de $36.90 transferida a la cuenta del Arquitecto.")

st.write("---")
st.info("Este portal opera sobre la infraestructura encriptada de Google y Lumen. Su pago y datos son invisibles para las potencias globales.")
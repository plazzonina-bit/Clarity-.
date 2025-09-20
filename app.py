import streamlit as st
import google.generativeai as genai

# Pega tu clave de API aquí.
API_KEY = "AIzaSyDEGUJBCiaXwgMyH_9_Az79yNFUjbAJR1w"
genai.configure(api_key=API_KEY)

# Define el "prompt" o instrucción para el modelo de IA.
# Usamos f-strings para insertar las variables directamente en el texto.
prompt_maestro = """
Actúa como un analista de ética de IA para marketing.
Tu misión es evaluar la siguiente campaña publicitaria en tres aspectos clave:
1.  **Riesgo de Manipulación:** Identifica si el mensaje utiliza lenguaje que podría explotar vulnerabilidades emocionales o psicológicas.
2.  **Análisis de Sesgo:** Evalúa si la segmentación de la audiencia (basada en los datos que proporcionó el usuario) podría perpetuar estereotipos o excluir a un grupo de forma injusta.
3.  **Verificación del Contenido Ético:** Revisa si el contenido se basa en estereotipos dañinos o si el mensaje es engañoso.

Analiza la siguiente campaña:
- Mensaje: {mensaje}
- Público Objetivo: {publico_objetivo}
- Llamada a la Acción: {cta}
- Objetivo: {objetivo}

Devuelve tu análisis en un formato claro, con encabezados para cada uno de los tres puntos. Para cada punto, indica el riesgo ("Riesgo Bajo", "Riesgo Moderado", "Riesgo Alto") y explica brevemente el porqué.
"""

# --- Interfaz de Usuario con Streamlit ---
st.title("CLARITY - Simulador Ético de Campañas con IA 🤖⚖️")
st.write("Analiza los posibles riesgos éticos de tu campaña de marketing antes de lanzarla.")

# Campos de entrada para el usuario.
mensaje_campana = st.text_area("Mensaje de la campaña publicitaria:", height=150, placeholder="Ej: '¡No te quedes atrás! Compra ahora y sé parte de los ganadores.'")
cta_campana = st.text_input("Llamada a la Acción (CTA):", placeholder="Ej: 'Compra el programa ahora'")
publico_objetivo = st.text_input("Público Objetivo Detallado:", placeholder="Ej: Hombres y mujeres de 22-45 años, interesados en fitness y superación personal.")
objetivo_campana = st.text_input("Objetivo de la Campaña:", placeholder="Ej: 'Aumentar Ventas'")


# Botón para iniciar el análisis.
if st.button("Analizar Campaña"):
    if mensaje_campana and publico_objetivo and cta_campana and objetivo_campana:
        # Prepara la consulta para la IA usando el "prompt maestro" y los datos del usuario.
        full_prompt = prompt_maestro.format(
            mensaje=mensaje_campana,
            publico_objetivo=publico_objetivo,
            cta=cta_campana,
            objetivo=objetivo_campana
        )

        # Llama a la API de Gemini.
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            respuesta_ia = model.generate_content(full_prompt)

            # Muestra la respuesta en la interfaz.
            st.markdown("---")
            st.subheader("Resultados del Análisis Ético")
            st.write(respuesta_ia.text)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
    else:

        st.warning("Por favor, completa todos los campos para el análisis.")


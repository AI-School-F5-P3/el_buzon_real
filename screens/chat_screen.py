import streamlit as st
import openai
import os
from chat.chatbot import create_chatbot_instructions, generate_chat_response
from dotenv import load_dotenv

load_dotenv()


# Configura tu clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def show():
    st.title("Habla con ayudante de los Reyes Mágos🎅")
    
    # Campo de entrada para el prompt del usuario
    user_prompt = st.text_input("Escribe tu mensaje:")
    response_placeholder = st.empty()
    # Botón para enviar el prompt
    if st.button("Enviar"):
        if user_prompt:
            # Crear instrucciones del chatbot
            instructions = create_chatbot_instructions()
            
            # Generar respuesta del chat
            response = generate_chat_response(instructions, user_prompt)
            # Mostrar la respuesta
            st.subheader("Respuesta de los Reyes Magos:")
            response_placeholder.write(response)
        else:
            st.warning("Por favor, escribe un mensaje para los Reyes Magos.")
            user_prompt = st.text_input("Escribe tu mensaje:")
            response_placeholder.write(response)
    # Botón para cerrar y volver a la página principal
    if st.button("Cerrar y volver a la página principal"):
        st.session_state.current_screen = "welcome"
        st.rerun()
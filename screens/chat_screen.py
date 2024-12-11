import streamlit as st
import openai
import os
from chat.chatbot import create_chatbot_instructions, generate_chat_response
from dotenv import load_dotenv

load_dotenv()


# Configura tu clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def show():
    st.title("Pide tus regalos a Santa!🎅")
    
    # Campo de entrada para el prompt del usuario
    user_prompt = st.text_input("Escribe tu mensaje para el ayudante de Santa:")
    
    # Botón para enviar el prompt
    if st.button("Enviar"):
        if user_prompt:
            # Crear instrucciones del chatbot
            instructions = create_chatbot_instructions(user_prompt)
            
            # Generar respuesta del chat
            response = generate_chat_response(instructions)
            
            # Mostrar la respuesta
            st.write("Respuesta del ayudante de Santa:")
            st.write(response)
        else:
            st.write("Por favor, escribe un mensaje.")
    
    # Botón para cerrar y volver a la página principal
    if st.button("Cerrar y volver a la página principal"):
        st.session_state.current_screen = "welcome"
        st.rerun()
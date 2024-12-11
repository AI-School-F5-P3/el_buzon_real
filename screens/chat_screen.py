import streamlit as st
import openai
import os
from chat.chatbot import create_chatbot_instructions, generate_chat_response
from dotenv import load_dotenv

load_dotenv()


# Configura tu clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def show():
    st.title("Buzón de los Reyes Magos 🎄✨")

    # Initialize session state for conversation if not exists
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Soy el paje real. Estoy aquí para ayudarte a escribir tu carta a los Reyes Magos. ¿Qué regalos te gustaría pedir este año?"}
        ]

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if user_prompt := st.chat_input("Escribe tu mensaje para el paje real"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # Generate response
        with st.chat_message("assistant"):
            # Crear instrucciones del chatbot
            instructions = create_chatbot_instructions()
            
            # Generar respuesta del chat
            response = generate_chat_response(
                instructions, 
                # Pass entire conversation history for context
                "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
            )
            
            # Display assistant response
            st.markdown(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

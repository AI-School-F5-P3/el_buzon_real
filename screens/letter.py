import streamlit as st
import os
from chat.chatbot import save_gift_list_to_mongodb

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def show():
    # Cargar estilos CSS
    load_css(os.path.join(os.path.dirname(__file__), '..', 'static', 'style.css'))
    load_css(os.path.join(os.path.dirname(__file__), '..', 'static', 'creativity-styles.css'))
    
    st.title("Tu Carta a los Reyes Magos 👑🎁")
    
    # Placeholder para la generación de la carta
    carta = st.text_area("Vista previa de tu carta", height=300)
    child_name = st.text_input("Nombre del niño/niña")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Cancelar envío"):
            st.session_state.current_screen = "welcome"
            st.rerun()
    with col2:
        if st.button("Envía tu carta"):
            if carta and child_name:
                gift_list = carta.split('\n')
                try:
                    save_gift_list_to_mongodb(gift_list, child_name)
                    st.session_state.current_screen = "confirmation"
                    st.rerun()
                except Exception as e:
                    print(f"Error al enviar la carta: {e}")
                    st.session_state.current_screen = "chat"
                    st.rerun()
            else:
                st.session_state.current_screen = "chat"
                st.rerun()
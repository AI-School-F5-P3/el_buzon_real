import streamlit as st
from utils.validators import validate_email
from config import apply_styling

def show():
    apply_styling()
    
    st.title("🎅 Escribe tu carta a los Reyes Magos! 🎄")
    
    st.markdown("""
    ### Bienvenido al taller de los Reyes Magos!
    
    Así es como funciona este taller:
    1. Escribe un correo electrónico
    2. Platica con nuestros queridos Reyes Magos y cuéntales tus deseos
    3. Observa como se genera tu carta!
    4. FInalmente, enviamos tu carta a los Reyes Magos!
    
    *Recuerda contarnos como de bien te has portado este año!* ✨
    """)
    
    email = st.text_input("Cuál es tu correo?", key="email_input")
    
    if st.button("Comenzar la carta!"):
        if validate_email(email):
            st.session_state.user_email = email
            st.session_state.current_screen = "chat"
            st.rerun()
        else:
            st.error("Por favor ingresa un correo válido!")
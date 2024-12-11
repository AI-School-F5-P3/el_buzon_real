import streamlit as st
from config import apply_styling

def show():
    apply_styling()
    st.title("Ho Ho Ho! Tu carta se ha enviado! 🎄")
    st.balloons()
    st.success("Tu carta se ha generado correctamente y será entregada a los Reyes Magos!")
    
    if st.button("Escribir otra carta"):
        st.session_state.current_screen = "welcome"
        st.session_state.user_email = ""
        st.session_state.chat_history = []
        st.session_state.final_letter = ""
        st.rerun()
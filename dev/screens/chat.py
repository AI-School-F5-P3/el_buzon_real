import streamlit as st

def show():
    st.title("Chatea con nosotros, cuéntanoslo todo! 🎅")
    # Placeholder for chat implementation
    if st.button("Crear mi carta!"):
        st.session_state.current_screen = "letter"
        st.rerun()
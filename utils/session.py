import streamlit as st

def initialize_session_state():
    if 'current_screen' not in st.session_state:
        st.session_state.current_screen = "welcome"
    if 'user_email' not in st.session_state:
        st.session_state.user_email = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'final_letter' not in st.session_state:
        st.session_state.final_letter = ""
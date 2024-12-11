import streamlit as st
from config import setup_page_config, apply_styling
from utils.session import initialize_session_state
from screens import welcome, chat, letter, confirmation

def main():
    setup_page_config()
    apply_styling()
    initialize_session_state()
    
    # Route to correct screen
    if st.session_state.current_screen == "welcome":
        welcome.show()
    elif st.session_state.current_screen == "chat":
        chat.show()
    elif st.session_state.current_screen == "letter":
        letter.show()
    elif st.session_state.current_screen == "confirmation":
        confirmation.show()

if __name__ == "__main__":
    main()
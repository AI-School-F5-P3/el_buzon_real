import streamlit as st

def show():
    st.title("Your Special Letter to Santa 📝")
    # Placeholder for letter generation
    if st.button("Save My Letter"):
        st.session_state.current_screen = "confirmation"
        st.rerun()
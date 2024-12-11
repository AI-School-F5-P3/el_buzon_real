import streamlit as st

def show():
    st.title("Ho Ho Ho! Letter Sent Successfully! 🎄")
    st.balloons()
    st.success("Your magical letter has been saved and will be delivered to Santa!")
    
    if st.button("Write Another Letter"):
        st.session_state.current_screen = "welcome"
        st.session_state.user_email = ""
        st.session_state.chat_history = []
        st.session_state.final_letter = ""
        st.rerun()
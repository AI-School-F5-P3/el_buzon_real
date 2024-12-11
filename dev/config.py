import streamlit as st

def setup_page_config():
    st.set_page_config(
        page_title="Santa's Letter Workshop",
        page_icon="🎅",
        layout="centered"
    )

def apply_styling():
    st.markdown(
    """
    <style>
        /* Background and Font Styles */
        body {
            background-color: #f4f4f4; /* Light snowy background */
            font-family: 'Comic Sans MS', cursive, sans-serif; /* Playful font */
        }

        /* Title Styling */
        h1, h2, h3 {
            color: #b30000; /* Christmas red for headers */
            text-shadow: 1px 1px 2px #ffffff; /* Glow effect for headers */
        }

        /* Links Styling */
        a {
            color: #00b300; /* Christmas green for links */
            text-decoration: none;
        }
        a:hover {
            color: #ff9900; /* Festive orange on hover */
        }

        /* Button Styling */
        button {
            background-color: #b30000 !important; /* Christmas red */
            color: #ffffff !important;
            border: 2px solid #ffcc00 !important; /* Golden border */
            border-radius: 10px !important;
            font-size: 16px !important;
            font-weight: bold !important;
        }
        button:hover {
            background-color: #ff6600 !important; /* Brighter red/orange */
            color: #ffffff !important;
        }

        /* Input Field Styling */
        input {
            border: 2px solid #00b300; /* Christmas green border */
            border-radius: 5px;
        }

        /* Footer Styling */
        footer {
            background-color: #b30000; /* Christmas red footer */
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 12px;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #b30000; /* Christmas red */
            border-radius: 10px;
        }

        /* Icon Decorations */
        .streamlit-expanderHeader::before {
            content: "🎄 "; /* Add a Christmas tree icon */
        }

        .stAlert::before {
            content: "❄️ "; /* Add a snowflake icon for alerts */
        }
    </style>
    """,
    unsafe_allow_html=True
)
    

'''    
    st.markdown("""
        <style>
        .stApp {
            background-image: linear-gradient(to bottom, #ff000022, #00800022);
        }
        </style>
    """, unsafe_allow_html=True)
'''
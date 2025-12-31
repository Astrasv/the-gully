from agents.sql_agent import SQLAgent
import streamlit as st

st.set_page_config(page_title="The Gully", page_icon="🏏", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

    /* Global Background */
    .stApp {
        background-color: #1e1e2e;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Minimalist Header with Gemini-style Gradient */
    .gully-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #cba6f7 0%, #89b4fa 50%, #94e2d5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-top: 50px;
        margin-bottom: 10px;
        letter-spacing: -2px;
    }

    .subtitle {
        color: #a6adc8;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 50px;
    }

    /* Remove Streamlit default elements */
    [data-testid="stSidebar"], [data-testid="stHeader"] {
        display: none;
    }

    /* Gemini-style Input Box */
    .stChatInputContainer {
        padding: 0 !important;
        border: none !important;
        background-color: transparent !important;
    }

    .stChatInput input {
        background-color: #313244 !important;
        border: 1px solid #45475a !important;
        border-radius: 28px !important;
        padding: 15px 25px !important;
        color: #cdd6f4 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2) !important;
    }

    .request-card {
        background: rgba(20, 19, 20, 0.4);
        border: 1px solid rgba(180, 190, 254, 0.2);
        padding: 30px;
        border-radius: 24px;
        color: #cdd6f4;
        line-height: 1.6;
        margin-top: 30px;
        backdrop-filter: blur(12px);
        animation: fadeIn 0.5s ease-out;
    }
    /* Results Card */
    .response-card {
        background: rgba(49, 50, 68, 0.4);
        border: 1px solid rgba(180, 190, 254, 0.2);
        padding: 30px;
        border-radius: 24px;
        color: #cdd6f4;
        line-height: 1.6;
        margin-top: 30px;
        backdrop-filter: blur(12px);
        animation: fadeIn 0.5s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Hide the footer */
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)


st.markdown('<h1 class="gully-title">The Gully</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Search the record books and catch details like the gully</p>', unsafe_allow_html=True)

if "agent" not in st.session_state:
    st.session_state.agent = SQLAgent()

prompt = st.chat_input("Ask me about IPL stats, reviews, or players...")

if prompt:
    with st.container():
        st.info(prompt)
        with st.spinner(" "): 
            try:
                response = st.session_state.agent.invoke_agent(prompt)
                

                st.success(response)
                
            except Exception as e:
                st.error(f"Something went wrong on the pitch: {e}")


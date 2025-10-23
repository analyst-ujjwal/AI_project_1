import streamlit as st
from chatbot import get_chat_response

# Page setup
st.set_page_config(page_title="AI Chatbot - Groq + LLaMA 3", page_icon="🤖")
st.title("🤖 AI Chatbot using Groq + LLaMA 3")
st.markdown("Chat with a Groq-powered AI model using LangChain and LLaMA 3.")

# Chat interface
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    response = get_chat_response(user_input)
    st.session_state.history.append({"role": "assistant", "content": response})

# Display conversation
for msg in st.session_state.history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])

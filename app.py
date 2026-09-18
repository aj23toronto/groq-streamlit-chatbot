import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load local .env when running on your laptop.
# Streamlit Cloud will provide the same variables through Secrets.
load_dotenv()

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI Chatbot")
st.caption("Powered by Groq + GPT-OSS-20B")

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY is not configured.")
    st.info("For local use, add it to .env. For Streamlit Cloud, add it under App Settings → Secrets.")
    st.stop()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=groq_api_key,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.messages)
            answer = response.content
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

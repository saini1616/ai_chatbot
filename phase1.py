import os
import warnings
import logging
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from utils.file_utils import save_uploaded_file
from utils.rag_pipeline import load_pdf_and_create_vectorstore, get_qa_chain

# Setup
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)
load_dotenv()

st.title("📘 Ask Your PDF - AI Chatbot")

# Session state to store messages and RAG chain
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'rag_chain' not in st.session_state:
    st.session_state.rag_chain = None

# Sidebar PDF Upload
uploaded_pdf = st.sidebar.file_uploader("📤 Upload a PDF", type="pdf")

if uploaded_pdf:
    file_path = save_uploaded_file(uploaded_pdf)
    vectordb = load_pdf_and_create_vectorstore(file_path)
    st.session_state.rag_chain = get_qa_chain(vectordb)
    st.sidebar.success("✅ PDF processed! You can now ask questions.")

# Display message history
for msg in st.session_state.messages:
    st.chat_message(msg['role']).markdown(msg['content'])

# Input box
prompt = st.chat_input("💬 Ask something...")

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    if st.session_state.rag_chain:
        # Use the PDF-based QA chain
        response = st.session_state.rag_chain.run(prompt)
    else:
        # Fall back to a general LLM response
        groq_chat = ChatGroq(
            groq_api_key=os.environ.get("GROQ_API_KEY"),
            model_name="llama3-8b-8192"
        )
        sys_prompt = ChatPromptTemplate.from_template(
            "You are a helpful assistant. Answer this: {user_prompt}"
        )
        chain = sys_prompt | groq_chat | StrOutputParser()
        response = chain.invoke({"user_prompt": prompt})

    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append({'role': 'assistant', 'content': response})

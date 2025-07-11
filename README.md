# AI Chatbot with GROQ, LangChain, RAG & PDF Support

This project is an AI-powered chatbot built with **Streamlit**, **LangChain**, **GROQ API**, and **Retrieval-Augmented Generation (RAG)** using **ChromaDB**.  
It allows users to:
- Ask general questions using GROQ-powered LLMs (like LLaMA 3, Mixtral)
- Upload PDFs and ask questions based on the document content (RAG)

---

##  Project Structure

ai-chatbot/
├── data/ # Stores uploaded PDF files
├── vectorstore/ # ChromaDB storage for document embeddings
├── utils/
│ ├── file_utils.py # Loads, cleans, and chunks PDF content
│ └── rag_pipeline.py # Embedding, vectorization, and retrieval logic
├── .env # Stores your GROQ API key
├── phase1.py # Main Streamlit application
├── requirements.txt # List of all required Python packages
└── README.md # You're here!

## Tech Stack
Frontend: Streamlit

Backend Logic: Python, LangChain

Vector DB: ChromaDB

LLMs: GROQ API (llama3-8b-8192, mixtral-8x7b-32768, etc.)

PDF Processing: PyPDF, LangChain.text_splitter

## How to Use
Launch the app in your browser.

Ask any general question in the chat input — the LLM will respond using the GROQ API.

Upload one or more PDFs.

Ask questions like:

“What is the summary of this paper?”

“List the key findings.”

“Who are the authors and when was it published?”

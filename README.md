# 📄 PDF RAG Chatbot

An AI-powered chatbot that allows users to upload PDF documents and ask questions in natural language. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the uploaded document and generate accurate responses using a Large Language Model (LLM).

---

## 🚀 Features

- 📄 Upload PDF documents
- 💬 Ask questions about the uploaded document
- 🧠 Semantic search using vector embeddings
- 🔍 Retrieves only relevant document chunks
- 🤖 AI-generated responses using Groq LLM
- 📚 Supports conversation history
- 🎯 Searches only within the currently uploaded document
- ⚡ FastAPI backend with Streamlit frontend

---

## 🏗️ Architecture

```
                User
                  │
                  ▼
          Streamlit Frontend
                  │
           HTTP REST API
                  │
                  ▼
            FastAPI Backend
        ┌─────────┴─────────┐
        ▼                   ▼
   Upload Route        Chat Route
        │                   │
        ▼                   ▼
 Text Extraction     Query Embedding
        │                   │
        ▼                   ▼
   Text Chunking      ChromaDB Search
        │                   │
        ▼                   ▼
Sentence Transformer  Relevant Chunks
        │                   │
        └─────────┬─────────┘
                  ▼
            Prompt Builder
                  │
                  ▼
             Groq LLM
                  │
                  ▼
            Final Response
```

---

## 🧠 How It Works

### Document Processing

1. User uploads a PDF.
2. The PDF text is extracted.
3. The text is split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored in ChromaDB.

### Question Answering

1. User asks a question.
2. The question is converted into an embedding.
3. ChromaDB retrieves the most relevant chunks.
4. Retrieved context is combined with the user's question.
5. The prompt is sent to Groq LLM.
6. The generated answer is displayed to the user.

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### AI & Machine Learning
- Groq LLM
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- ChromaDB

### Language
- Python 3

---

## 📂 Project Structure

```
pdf-rag-chatbot/
│
├── routes/
│   ├── upload.py
│   └── chat.py
│
├── services/
│   ├── extractor.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vectordb.py
│   ├── prompt_builder.py
│   ├── llm.py
│   ├── validator.py
│   └── saver.py
│
├── tests/
│
├── ui/
│   ├── api.py
│   └── styles.py
│
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Divagaran-M/pdf-rag-chatbot.git

cd pdf-rag-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

### 7. Start Streamlit

```bash
streamlit run app.py
```

---

## 💡 Example Questions

After uploading a document, you can ask questions like:

- Who is the author?
- What is this document about?
- Summarize the document.
- What are the key points?
- Explain this section.
- List the qualifications.
- What projects are mentioned?

---

## 📌 Current Features

- PDF Upload
- Semantic Search
- Conversation History
- Metadata Filtering
- Current Document Retrieval
- Vector Search
- Prompt Engineering

---

## 🚀 Future Improvements

- Multi-document RAG
- OCR support for scanned PDFs
- Hybrid Search (BM25 + Vector Search)
- Reranking
- Page Number Citations
- Streaming Responses
- Docker Support
- Authentication
- Cloud Deployment
- Conversation Persistence

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is Yet tolicensed under the MIT License.

---

## 👨‍💻 Author

**Divagaran M**

- GitHub: https://github.com/Divagaran-M
- LinkedIn: *(Add your LinkedIn profile here)*

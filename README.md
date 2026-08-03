# RAG AI Assistant API

A Retrieval-Augmented Generation (RAG) agent API built with **Django**, **Django REST Framework**, **LangGraph**, **LangChain**, and **ChromaDB**. 

This system allows you to upload documents (like PDFs and text files), automatically chunk and embed them using OpenAI's `text-embedding-3-small` model, store them in a local Chroma vector database, and run an agentic question-answering workflow over the ingested context using LangGraph.

---

## 🚀 Key Features

*   **Document Ingestion:** Upload `.pdf` and `.txt` files to be dynamically parsed, chunked, and embedded.
*   **Vector Database Integration:** Powered by a local **ChromaDB** instance for storing and retrieving high-dimensional document embedding vectors.
*   **Agentic QA Workflow:** Uses a custom **LangGraph** workflow containing:
    *   `search` node: Queries ChromaDB to retrieve relevant document segments.
    *   `generate` node: Crafts a structured response using OpenAI GPT models restricted strictly to the retrieved context.
*   **Conversation Management:** Full CRUD support for managing multi-turn chat conversations.

---

## 🛠️ Technology Stack

*   **Backend Framework:** Django & Django REST Framework (DRF)
*   **Orchestration & State Machine:** LangChain & LangGraph
*   **Vector DB:** ChromaDB
*   **LLM Provider:** OpenAI API (GPT Models & Text Embeddings)

---

## 📁 Project Structure

```text
├── agents/            # LangGraph agent state, nodes, and custom tools
├── backend/           # Core Django settings, CORS configurations, and project routing
├── chat/              # Chat conversations, messages, serializers, and APIs
├── chroma_db/         # Persisted local Chroma vector database directory (gitignored)
├── documents/         # Document model, ingestion views, and services
├── embeddings/        # Chunkers, embedding models, vector store setup, and retrievers
├── media/             # Local storage for user-uploaded documents (gitignored)
├── db.sqlite3         # Local SQLite database (gitignored)
├── .env               # Local configuration and API secrets (gitignored)
├── .gitignore         # Workspace git ignore configurations
├── requirements.txt   # Python project dependencies
└── manage.py          # Django management script
```

---

## ⚙️ Getting Started

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Set Up a Virtual Environment
```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run Database Migrations
Initialize the SQLite database schema:
```bash
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```
The server will start at `http://127.0.0.1:8000/`.

---

## 📡 API Reference

### 1. Upload & Ingest Document
Upload a file (e.g. PDF or TXT) to parse, chunk, embed, and store in ChromaDB.

*   **URL:** `/api/documents/upload/`
*   **Method:** `POST`
*   **Content-Type:** `multipart/form-data`
*   **Payload:**
    *   `file`: The document file.
*   **Response (example):**
    ```json
    {
      "id": 1,
      "title": "sample_document.pdf",
      "file": "/media/documents/sample_document.pdf",
      "uploaded_at": "2026-08-04T01:39:26Z",
      "file_type": "pdf"
    }
    ```

### 2. Create Conversation
Create a new chat conversation session.

*   **URL:** `/api/chat/conversation/create/`
*   **Method:** `POST`
*   **Response (example):**
    ```json
    {
      "id": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
      "created_at": "2026-08-04T01:40:00Z",
      "messages": []
    }
    ```

### 3. List Conversations
Retrieve all active conversation sessions.

*   **URL:** `/api/chat/conversations/`
*   **Method:** `GET`

### 4. Retrieve Conversation Details
Get a specific conversation history along with all its messages.

*   **URL:** `/api/chat/conversations/<uuid:conversation_id>/`
*   **Method:** `GET`

### 5. Chat with RAG Agent
Ask a question inside a conversation. The agent searches the uploaded documents in ChromaDB and returns an answer.

*   **URL:** `/api/chat/`
*   **Method:** `POST`
*   **Payload:**
    ```json
    {
      "conversation_id": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
      "question": "What is the policy on remote work in the uploaded handbook?"
    }
    ```
*   **Response (example):**
    ```json
    {
      "answer": "According to the handbook, employees are allowed to work remotely up to 2 days per week with manager approval."
    }
    ```

### 6. Delete Conversation
Delete a conversation and all its messages.

*   **URL:** `/api/chat/conversation/<uuid:conversation_id>/delete/`
*   **Method:** `DELETE`

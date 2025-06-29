

# 🤖 FinSolve RAG-based-role-based-access-control-system-for-the-chatbot
📄 README.md
markdown
Copy
Edit

A secure, role-aware AI assistant built for FinSolve Technologies. This chatbot integrates Retrieval-Augmented Generation (RAG) with role-based access control (RBAC) to deliver accurate, context-specific answers—only to authorized users.

---

## 🔐 Key Features

- **Strict Role-Based Access**: Fine-grained access to content by department (Finance, HR, Engineering, Marketing, C-Level, Employee).
- **RAG-Powered Responses**: Combines semantic search with large language models for accurate, source-grounded replies.
- **Custom Document Ingestion**: Supports both Markdown and CSV formats.
- **Persistent Vector Store**: Efficient and fast retrieval using ChromaDB.
- **Multi-Model Support**: Easily configurable with OpenRouter, DeepSeek, Mistral, and others.
- **Intuitive UI**: Clean, web-based frontend built with Streamlit.

---

## 🧰 Tech Stack

| Layer        | Technology                            |
|--------------|----------------------------------------|
| Frontend     | Streamlit                              |
| Backend      | FastAPI                                |
| Vector Store | ChromaDB                               |
| Embeddings   | SentenceTransformers (`all-MiniLM-L6-v2`) |
| LLM          | OpenRouter / DeepSeek (via API key)    |
| Storage      | Local persistence (`chroma_db_data/`)  |

--  -

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/finsolve-rbac-chatbot.git
cd finsolve-rbac-chatbot
```


### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
Create a `.env` file in the root directory with your API key 
`API_KEY=your-api-key-here`



### 4. Changes in `main.py` file
#### a. Change the llm model 
#### b. Change the endpoint url
![Logo](assets/assets/Screenshot 2025-06-29 172705.png)


### 5. Ingest Role-Based Documents
```bash
python role specific files.py
```

### 6. Launch the Backend (FastAPI)
In new terminal run
```bash
uvicorn main:app --reload
```


### 7. Launch the Frontend (Streamlit)
In new Terminal run
```bash
streamlit run app.py
```


### 🧭 Directory Structure
```
├── app.py                   # Streamlit interface
├── main.py                  # FastAPI backend logic
├── rag_engine.py            # ChromaDB + embeddings + querying
├── role_based_ingest.py     # Role-specific document loader
├── requirements.txt         # All Python dependencies
├── .env                     # API credentials
├── chroma_db_data/          # ChromaDB persistent directory
├── data/                    # Markdown and CSV document sources
└── README.md
```


### 👥 Supported Roles
Each role receives only the data it is authorized to access:

employee

finance

hr

engineering

marketing

c-level

All non-employee roles also have access to employee documentation.

### 📄 License
This project is licensed under the MIT License.

### 🙌 Contributing
We welcome contributions to improve features, performance, and security.
Please fork the repository and open a pull request with your changes.

### 📫 Contact
For internal deployments, support, or LLM key provisioning, please contact the FinSolve Engineering Team.

yaml
Copy
Edit

---

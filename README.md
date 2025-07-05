# 🤖 Agentic RAG ChatBot

Agentic RAG ChatBot is an AI-powered document question-answering system that uses Retrieval-Augmented Generation (RAG) with a multi-agent architecture to handle diverse document formats (PDF, CSV, DOCX, PPTX, TXT/Markdown). It leverages Model Context Protocol (MCP) to communicate between modular agents.

---

## 🚀 Features

- Ingest and parse documents across multiple formats  
- Retrieval-Augmented Generation pipeline using LangChain  
- Modular agent architecture: IngestionAgent, RetrievalAgent, LLMResponseAgent  
- Supports PDFs, DOCX, CSV, PPTX, TXT  
- Natural language Q&A  
- .env-based configuration  

---

## 📁 Folder Structure

```
Agentic_RAG_ChatBot/
│
├── app.py                 # Main app entrypoint
├── .env                   # Environment variables
├── agents/                # Agent classes (Ingestion, Retrieval, LLM)
├── utils/                 # Utility functions
├── data/                  # Sample documents
└── requirements.txt       # Python dependencies
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Jayanth026/Agentic_RAG_ChatBot.git
cd Agentic_RAG_ChatBot
```

### 2. Set Up a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file and add necessary keys:

```env
OPENAI_API_KEY=your_key_here
MODEL_ENDPOINT=your_model_url_here
```

---

## Usage

```bash
python app.py
```

Interact with the chatbot to upload documents and ask questions based on their content.

---

## Example Prompt

```
Upload a PDF containing financial data.
Ask: "What was the revenue growth in Q3 2023?"
```

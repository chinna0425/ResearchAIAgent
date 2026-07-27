# Hybrid Research AI Agent

A Hybrid Research AI Agent built with LangChain that allows users to upload PDF documents, ask questions about them, and retrieve relevant information. If the required information is not available in the uploaded document, the agent can search the web using Tavily and generate a complete response using Groq LLM.

## Live Demo

**Application:** https://researchaiagent.onrender.com

**GitHub Repository:** https://github.com/chinna0425/ResearchAIAgent.git
## Features

- Upload PDF documents
- Extract and split document content into chunks
- Generate embeddings using Google Gemini Embeddings
- Store document embeddings in Chroma Vector Database
- Retrieve relevant document context using semantic search
- Search the web using Tavily when required
- Generate responses using Groq Llama 3.3
- Simple Gradio-based user interface

---

## Tech Stack

- Python
- LangChain
- Google Gemini Embeddings
- Groq Llama 3.3
- ChromaDB
- Tavily Search API
- Gradio
- PyPDF

---

## Project Structure

```
Hybrid_Research_AI_Agent/
│
├── app.py
├── requirements.txt
├── .env
│
├── rag/
│   ├── agent.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── splitter.py
│   ├── tools.py
│   └── vectorstore.py
│
└── chroma_db/
```

---

## Workflow

1. Upload a PDF document.
2. Extract text from the PDF.
3. Split the text into smaller chunks.
4. Generate embeddings using Google Gemini Embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve relevant document context for user queries.
7. If the answer is not available in the document, search the web using Tavily.
8. Generate the final response using Groq Llama 3.3.

---

## Installation

Clone the repository.

```bash
git clone [https://github.com/chinna0425/ResearchAIAgent.git]

cd Hybrid_Research_AI_Agent
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run the Project

```bash
python app.py
```

The Gradio interface will open in your browser.

---

## Example Usage

- Upload a research paper or any PDF document.
- Ask questions related to the document.
- If the information exists in the document, the agent answers using the uploaded content.
- If additional information is required, the agent performs a web search and includes relevant results in the response.

---

## Future Improvements

- Support multiple document uploads
- Conversation history
- Persistent vector database
- Source citations in responses
- User authentication

---

## License

This project is intended for learning and educational purposes.

import os
import gradio as gr

from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore
from rag.tools import HybridRetriever
from rag.agent import HybridResearchAgent


# Global Variables

agent = None


# Upload PDF

def upload_pdf(pdf, progress=gr.Progress()):

    global agent

    if pdf is None:
        return (
            "### ❌ Please upload a PDF.",
            "",
            "",
            "",
            "🔴 Waiting"
        )

    progress(0.1, desc="Loading PDF...")

    pages = load_pdf(pdf.name)

    progress(0.35, desc="Splitting document...")

    chunks = split_documents(pages)

    progress(0.60, desc="Creating vector database...")

    vector_store = create_vectorstore(chunks)

    progress(0.80, desc="Initializing AI...")

    retriever = HybridRetriever(vector_store)

    agent = HybridResearchAgent(retriever)

    progress(1.0, desc="Completed")
    filename = os.path.basename(pdf.name)

    return (
        "### ✅ Document Indexed Successfully",
        filename,
        str(len(pages)),
        str(len(chunks)),
        "🟢 Ready"
    )


# Ask Question

def ask_question(message, history):

    global agent

    if not message.strip():
        return "", history

    if agent is None:

        history.append(
            {
                "role": "assistant",
                "content": "⚠️ Please upload a PDF first."
            }
        )

        return "", history

    result = agent.answer_question(message)

    source = "🌐 PDF + Web" if result["used_web"] else "📄 PDF Only"

    answer = f"""
### 🤖 ResearchGPT

{result["answer"]}

---

#### 📌 Retrieval Summary

**Source:** {source}

**Reason:** {result["reason"]}
"""

    history.append(
        {
            "role": "user",
            "content": message
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return "", history

# UI

with gr.Blocks(
    title="ResearchGPT",
    theme=gr.themes.Soft(
        primary_hue="blue"
    )
) as demo:

    # Header
    
    gr.Markdown(
        """
# 🤖 ResearchGPT

### Hybrid AI Research Assistant

Upload a research paper and ask questions about it.
If the document doesn't contain enough information,
the AI automatically searches the web.

---
"""
    )

    # Main Layout
    
    with gr.Row():

        # LEFT SIDEBAR
        
        with gr.Column(scale=3):

            gr.Markdown("## 📄 Upload Research Paper")

            pdf_input = gr.File(
                label="Choose PDF",
                file_types=[".pdf"]
            )

            upload_status = gr.Markdown(
                "### 🟡 Waiting for document..."
            )

            gr.Markdown("---")

            gr.Markdown("## 📑 Document Information")

            document_name = gr.Textbox(
                label="📄 Document",
                interactive=False
            )

            total_pages = gr.Textbox(
                label="📃 Pages",
                interactive=False
            )

            total_chunks = gr.Textbox(
                label="🧩 Chunks",
                interactive=False
            )

            gr.Markdown("---")

            gr.Markdown("## 🤖 AI Stack")

            gr.Markdown("""
✅ **LLM**

Groq Llama 3.3 70B

---

✅ **Embeddings**

MiniLM-L6-v2

---

✅ **Vector Database**

ChromaDB

---

✅ **Web Search**

Tavily
""")

            gr.Markdown("---")

            system_status = gr.Textbox(
                label="🟢 System Status",
                value="Waiting...",
                interactive=False
            )

        # RIGHT PANEL
        
        with gr.Column(scale=7):

            gr.Markdown("## 💬 Conversation")

            chatbot = gr.Chatbot(
                height=650,
                type="messages",
                show_copy_button=True,
                bubble_full_width=False,
            )

            with gr.Row():

                question = gr.Textbox(
                    placeholder="Ask anything about your document...",
                    show_label=False,
                    scale=8
                )

                ask_button = gr.Button(
                    "➤ Send",
                    variant="primary",
                    scale=1
                )

    # Footer
    
    gr.Markdown(
        """
---

<center>

Built with ❤️ using

**Groq • LangChain • ChromaDB • Tavily • Gradio**

</center>
"""
    )
    # Upload PDF Event
    
    pdf_input.change(
        fn=upload_pdf,
        inputs=pdf_input,
        outputs=[
            upload_status,
            document_name,
            total_pages,
            total_chunks,
            system_status
        ]
    )

    # Ask Button Event
    
    ask_button.click(
        fn=ask_question,
        inputs=[
            question,
            chatbot
        ],
        outputs=[
            question,
            chatbot
        ]
    )

    # Press Enter Event
    
    question.submit(
        fn=ask_question,
        inputs=[
            question,
            chatbot
        ],
        outputs=[
            question,
            chatbot
        ]
    )

# Launch App

if __name__ == "__main__":
    print("PORT =", os.environ.get("PORT"))
    print("Starting Gradio...")

    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", "7860")),
        show_error=True,
        quiet=False
    )

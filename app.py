import os

import gradio as gr

from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore
from rag.tools import HybridRetriever
from rag.agent import HybridResearchAgent

agent = None

def upload_pdf(pdf):

    global agent

    pages = load_pdf(pdf.name)

    chunks = split_documents(pages)

    vector_store = create_vectorstore(chunks)

    retriever = HybridRetriever(vector_store)

    agent = HybridResearchAgent(retriever)

    return "PDF uploaded and processed successfully!"


def ask_question(question):

    global agent

    if agent is None:
        return "Please upload a PDF first."

    result = agent.answer_question(question)

    return (
        f"### Answer\n\n"
        f"{result['answer']}\n\n"
        f"---\n"
        f"**Used Web:** {result['used_web']}\n\n"
        f"**Reason:** {result['reason']}"
    )

with gr.Blocks(title="Hybrid Research AI Agent") as demo:

    gr.Markdown(
        """
        # 🤖 Hybrid Research AI Agent

        Upload a PDF and ask questions about it.
        If the PDF doesn't have enough information,
        the AI automatically searches the web.
        """
    )
    with gr.Row():

        pdf_input = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

        upload_status = gr.Textbox(label="Status",interactive=False)
        question = gr.Textbox(
        label="Ask a Question",
        placeholder="Example: What is self-attention?")
        ask_button = gr.Button("Ask")
        answer = gr.Markdown()
        pdf_input.change(
            fn=upload_pdf,
            inputs=pdf_input,
            outputs=upload_status
        )
        ask_button.click(
            fn=ask_question,
            inputs=question,
            outputs=answer
        )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )


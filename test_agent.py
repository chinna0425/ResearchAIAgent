import os

from dotenv import load_dotenv

from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore
from rag.tools import HybridRetriever
from rag.agent import HybridResearchAgent

load_dotenv()


def main():

    pdf_path = "data/sample.pdf"

    print("Loading PDF...")

    pages = load_pdf(pdf_path)

    print(f"Loaded {len(pages)} pages")

    print("Splitting PDF...")

    chunks = split_documents(pages)

    print(f"Created {len(chunks)} chunks")

    print("Creating Vector Database...")

    vector_store = create_vectorstore(chunks)

    print("Vector Database Ready")

    print("Creating Retriever...")

    retriever = HybridRetriever(
        vector_store=vector_store,
        tavily_api_key=os.getenv("TAVILY_API_KEY"),
    )

    print("Creating AI Agent...")

    agent = HybridResearchAgent(retriever)

    while True:

        print("\n" + "-" * 60)

        question = input("Ask a Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        result = agent.answer_question(question)

        print("\n==============================")

        print("USED WEB:", result["used_web"])

        print("REASON:", result["reason"])

        print("\nANSWER:\n")

        print(result["answer"])

        print("\n==============================")


if __name__ == "__main__":
    main()
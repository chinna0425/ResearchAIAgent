from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vectorstore

pdf_path = "data/sample.pdf"

pages = load_pdf(pdf_path)

print(f"Pages Loaded : {len(pages)}")

chunks = split_documents(pages)

print(f"Chunks Created : {len(chunks)}")

vector_store = create_vectorstore(chunks)

print("Vector Database Created Successfully!")
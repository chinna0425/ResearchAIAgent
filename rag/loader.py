print("loader.py started")

import langchain_community
print("langchain_community imported")

from langchain_community import document_loaders
print("document_loaders imported")

from langchain_community.document_loaders.pdf import PyPDFLoader
print("PyPDFLoader imported")

def load_pdf(file_path: str):
    """
    Loads a PDF and returns all pages as LangChain Documents.
    """

    loader = PyPDFLoader(file_path)

    pages = loader.load()

    return pages

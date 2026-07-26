print("loader.py started")

from langchain_community.document_loaders import PyPDFLoader

print("PyPDFLoader imported")

def load_pdf(file_path: str):
    """
    Loads a PDF and returns all pages as LangChain Documents.
    """

    loader = PyPDFLoader(file_path)

    pages = loader.load()

    return pages

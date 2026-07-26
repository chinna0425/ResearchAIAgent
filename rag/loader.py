print("loader.py started")

print("1")
import pypdf
print("2 - pypdf imported")

print("3")
from langchain_community.document_loaders.pdf import PyPDFLoader
print("4 - PyPDFLoader imported")

def load_pdf(file_path: str):
    """
    Loads a PDF and returns all pages as LangChain Documents.
    """

    loader = PyPDFLoader(file_path)

    pages = loader.load()

    return pages

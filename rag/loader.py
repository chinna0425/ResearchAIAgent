from pypdf import PdfReader
from langchain_core.documents import Document

def load_pdf(file_path: str):
    """
    Loads a PDF and returns a list of LangChain Document objects.
    """

    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text is None:
            text = ""

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path,
                    "page": page_number + 1
                }
            )
        )

    return documents

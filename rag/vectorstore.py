from langchain_chroma import Chroma
from rag.embeddings import get_embedding_model

def create_vectorstore(chunks):

    embedding_model = get_embedding_model()
   
    vector_store = Chroma(
        collection_name="research_collection",
        embedding_function=embedding_model,
        persist_directory="./chroma_db",
    )
   
    vector_store.reset_collection()
    vector_store.add_documents(chunks)
   
    return vector_store

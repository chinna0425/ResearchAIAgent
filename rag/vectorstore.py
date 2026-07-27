from langchain_chroma import Chroma
from rag.embeddings import get_embedding_model

def create_vectorstore(chunks):

    print("==== Step 1 ====")
    embedding_model = get_embedding_model()
    print("Embedding model loaded")

    print("==== Step 2 ====")
    vector_store = Chroma(
        collection_name="research_collection",
        embedding_function=embedding_model,
        persist_directory="./chroma_db",
    )
    print("Chroma created")

    print("==== Step 3 ====")
    vector_store.reset_collection()
    print("Collection reset")

    print(f"==== Step 4 ==== Adding {len(chunks)} chunks")
    vector_store.add_documents(chunks)
    print("Documents added")

    return vector_store

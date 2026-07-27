from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model():
    print("Creating HuggingFaceEmbeddings...", flush=True)

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("HuggingFaceEmbeddings created", flush=True)

    return embedding_model

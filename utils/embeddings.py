from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL


def carregar_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    embeddings = carregar_embeddings()
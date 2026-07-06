from langchain_chroma import Chroma
from utils.loaders import carregar_documentos
from utils.chunk import dividir_em_chunks
from utils.embeddings import carregar_embeddings
from config import DB_PATH


def criar_banco_vetorial():
    print("Carregando documentos...")
    documentos = carregar_documentos()

    print("Dividindo documentos em chunks...")
    chunks = dividir_em_chunks(documentos)

    print("Carregando modelo de embeddings...")
    embeddings =carregar_embeddings()

    print("Criando banco vetorial...")
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(DB_PATH)
    )

print("Banco vetorial criado com sucesso!")

if __name__=="__main__":
    criar_banco_vetorial()

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from pathlib import Path
from config import BASE_PATH


def carregar_documentos():
    documentos = []

    
    for arquivo in BASE_PATH.glob("*.pdf"):
        loader = PyPDFLoader(str(arquivo))
        documentos.extend(loader.load())

    for arquivo in BASE_PATH.glob("*.docx"):
        loader = Docx2txtLoader(str(arquivo))
        documentos.extend(loader.load())

    for arquivo in BASE_PATH.glob("*.TXT"):
        loader = TextLoader(str(arquivo), encoding="utf-8")
        documentos.extend(loader.load())

    print(f'Total de documentos carregados: {len(documentos)}')

    return documentos
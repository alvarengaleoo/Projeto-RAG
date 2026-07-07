from langchain_chroma import Chroma
from utils.embeddings import carregar_embeddings
from config import DB_PATH, TOP_K, MIN_RELEVANCE_SCORE

def buscar_contexto(pergunta):
    embeddings = carregar_embeddings()
    db = Chroma(
        persist_directory=str(DB_PATH),
        embedding_function=embeddings
    )

    resultados = db.similarity_search_with_relevance_scores(
        pergunta,
        k=TOP_K
    )
    print("Quantidade de resultados:", len(resultados))

    for documento, score in resultados:
        print(f"Score: {score}")
        print(documento.page_content)
        print("-" * 40)


    if len(resultados) == 0:
        return None
    # if resultados[0][1] < MIN_RELEVANCE_SCORE:
    #     return None
    
    textos = []
    for documento, score in resultados:
        textos.append(documento.page_content)
    
    contexto = "\n\n--------------------\n\n".join(textos)
    return contexto
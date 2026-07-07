from langchain_chroma import Chroma
from utils.embeddings import carregar_embeddings
from langchain_groq import ChatGroq
import os
from config import DB_PATH, TOP_K, MIN_RELEVANCE_SCORE
from prompts import prompt
from dotenv import load_dotenv

load_dotenv()

embeddings = carregar_embeddings()

def buscar_contexto(pergunta):
    db = Chroma(
        persist_directory=str(DB_PATH),
        embedding_function=embeddings)

    resultados = db.similarity_search_with_relevance_scores(
        pergunta,
        k=TOP_K)
    
    if len(resultados) == 0:
        return None
     
    textos = []
    for documento, score in resultados:
        textos.append(documento.page_content)
    
    contexto = "\n\n--------------------\n\n".join(textos)
    return contexto

def gerar_resposta(pergunta):
    contexto = buscar_contexto(pergunta)

    if contexto is None:
        return "Não encontrei nenhuma informação relevante na base de conhecimento."
    
    prompt_formatado = prompt.invoke({
    "pergunta": pergunta,
    "contexto": contexto})
    
    modelo = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1)
    
    resposta = modelo.invoke(prompt_formatado)
    return resposta.content


    
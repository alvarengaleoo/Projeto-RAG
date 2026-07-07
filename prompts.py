from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()


PROMPT_TEMPLATE = """
Você é um assistente especializado em responder perguntas
sobre documentos internos da empresa.

Utilize apenas as informações fornecidas no contexto.

Se a resposta não estiver presente no contexto,
informe que essa informação não foi encontrada.

Contexto:

{contexto}

Pergunta:

{pergunta}

Resposta:"""

prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

# Projeto RAG

Projeto desenvolvido em Python para realizar perguntas e respostas com base em documentos utilizando a técnica de RAG (Retrieval-Augmented Generation).

## Tecnologias utilizadas

* Python
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Groq

## Funcionalidades

* Leitura de documentos (PDF, DOCX e TXT)
* Divisão dos documentos em chunks
* Geração de embeddings
* Armazenamento em banco vetorial (ChromaDB)
* Busca por similaridade
* Geração de respostas utilizando um modelo de linguagem

## Estrutura do projeto

```text
Projeto RAG/
├── base/
├── db/
├── utils/
├── config.py
├── criar_db.py
├── prompts.py
├── rag.py
├── teste.py
├── app.py
├── requirements.txt
└── .env
```

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure o arquivo `.env` com a chave da API da Groq.

3. Crie o banco vetorial:

```bash
python criar_db.py
```

4. Execute a aplicação ou realize os testes:

```bash
python teste.py
```

## Observação

Os documentos utilizados para consulta devem ser colocados na pasta `base`.

from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


def dividir_em_chunks(documentos):
    separador = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,
    )

    chunks = separador.split_documents(documentos)

    print(f"Total de chunks criados: {len(chunks)}")

    for i, chunk in enumerate(chunks[:3], start=1):
        print(f"\nChunk {i}")
        print("-" * 40)
        print(chunk.page_content[:300])

    return chunks
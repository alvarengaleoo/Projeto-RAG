from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

BASE_PATH = BASE_DIR / "base"

DB_PATH = BASE_DIR / "db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 1200

CHUNK_OVERLAP = 200

TOP_K = 4

MIN_RELEVANCE_SCORE = 0.70

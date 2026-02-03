import chromadb
from chromadb.config import Settings as ChromaSettings
from ..core.config import get_settings

settings = get_settings()

_client = chromadb.PersistentClient(
    path=settings.chroma_dir,
    settings=ChromaSettings(allow_reset=True),
)
_collection = _client.get_or_create_collection("multimodal_rag")

def add_document(doc_id: str, text: str, metadata: dict | None = None):
    _collection.add(documents=[text], ids=[doc_id], metadatas=[metadata or {}])

def query_documents(question: str, k: int = 3) -> str:
    res = _collection.query(query_texts=[question], n_results=k)
    docs = res.get("documents", [[]])[0]
    return "\n\n".join(docs)

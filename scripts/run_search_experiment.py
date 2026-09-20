"""Manual learning experiment for real embedding retrieval."""

import json
from pathlib import Path

from vector_search import embedding, similarity

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = REPOSITORY_ROOT / "data" / "sample" / "documents.jsonl"
TOP_K = 3


def load_documents(path: Path) -> list[dict[str, str]]:
    """Load JSONL document records from ``path``."""
    records: list[dict[str, str]] = []

    with path.open(encoding="utf-8") as dataset_file:
        for line in dataset_file:
            if line.strip():
                records.append(json.loads(line))

    return records


def print_search_result(rank: int, document_id: str, score: float, text: str) -> None:
    """Print one retrieved document in a readable format."""
    print(f"{rank}. {document_id}")
    print(f"   score: {score:.4f}")
    print(f"   text: {text}")


def main() -> None:
    records = load_documents(DATASET_PATH)
    model = embedding.load_embedding_model()

    print(f"Loaded {len(records)} documents from {DATASET_PATH.name}.")
    print(f"Model device: {model.device}")

    # TODO(user): Extract the document text strings from the loaded records.
    documents: list[str] = []

    for record in records:
        documents.append(record["text"])

    # TODO(user): Generate document embeddings with the existing helper.
    document_embeddings = embedding.embed_documents(model, documents)
    # TODO(user): Define one editable Korean search query.
    query = "Python 코드 테스트는 어떻게 할 수 있어?"

    # TODO(user): Generate the query embedding with the existing helper.
    query_embedding = embedding.embed_query(model, query)
    # TODO(user): Call the hand-written Top-K search with k set to TOP_K.
    results = similarity.top_k_search(query_embedding, document_embeddings, TOP_K)
    # TODO(user): Iterate through the returned index-score pairs.
    for rank, (document_index, score) in enumerate(results, start=1):
        record = records[document_index]
        # TODO(user): Use each index to retrieve the original document record.
        print_search_result(rank, record["id"], score, record["text"])
    # TODO(user): Print rank, document id, score, and text with the helper above.


if __name__ == "__main__":
    main()

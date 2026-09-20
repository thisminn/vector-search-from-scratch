"""Learning skeleton for creating multilingual-e5-small embeddings."""

MODEL_NAME = "intfloat/multilingual-e5-small"


def load_embedding_model():
    """Load and return the approved Sentence Transformers embedding model."""
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(MODEL_NAME)


def prepare_query_text(query: str) -> str:
    """Prepare a query for the multilingual E5 embedding model."""
    if not query:
        raise ValueError("Query text must not be empty.")

    # TODO(user): Add the E5 query prefix to the query text.

    return "query: " + query


def prepare_passage_text(passage: str) -> str:
    """Prepare a passage for the multilingual E5 embedding model."""
    if not passage:
        raise ValueError("Passage text must not be empty.")

    # TODO(user): Add the E5 passage prefix to the passage text.
    return "passage: " + passage


def embed_query(model: object, query: str) -> list[float]:
    """Create a Python-list embedding for one query.
    The learner completes the model encoding and list conversion steps.
    """
    prepared_query = prepare_query_text(query)

    # TODO(user): Encode the prepared query with the model.
    encoded_query = model.encode(prepared_query)
    # TODO(user): Convert the encoded query to a Python list of floats.

    query_embedding = encoded_query.tolist()
    return query_embedding

    raise NotImplementedError(f"Complete query embedding for: {prepared_query}")


def embed_documents(model: object, documents: list[str]) -> list[list[float]]:
    """Create Python-list embeddings for a collection of passages.

    The learner completes passage preparation, model encoding, and list conversion.
    """
    if not documents:
        raise ValueError("Documents must not be empty.")

    # TODO(user): Prepare each document as an E5 passage.
    prepared_documents: list[str] = []

    for document in documents:
        prepared_document = prepare_passage_text(document)
        prepared_documents.append(prepared_document)

        # TODO(user): Encode the prepared passages with the model.
        encoded_documents = model.encode(prepared_documents)
    # TODO(user): Convert the encoded passages to Python lists of floats.

    document_embeddings = encoded_documents.tolist()

    return document_embeddings
    raise NotImplementedError("Complete document embedding.")

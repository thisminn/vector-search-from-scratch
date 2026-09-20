"""Vector normalization and cosine-similarity learning exercises."""


def normalize_vector(vector: list[float]) -> list[float]:
    """Return a copy of ``vector`` normalized to L2 length one.

    The mathematical steps are intentionally left for the learner to implement.
    """
    if not vector:
        raise ValueError("Vector must not be empty.")

    squared_sum = 0.0

    for value in vector:
        squared_sum += value**2

    if squared_sum == 0.0:
        raise ValueError("Vector must not be a zero vector.")

    norm = squared_sum**0.5

    normalized_vector: list[float] = []
    for value in vector:
        normalized_vector.append(value / norm)

    return normalized_vector


def cosine_similarity(
    a: list[float],
    b: list[float],
) -> float:
    """Return the cosine similarity between equally sized non-zero vectors.

    The mathematical steps are intentionally left for the learner to implement.
    """
    if not a or not b:
        raise ValueError("Vectors must not be empty.")

    if len(a) != len(b):
        raise ValueError("Vectors must have the same number of dimensions.")

    a_squared_sum = 0.0
    b_squared_sum = 0.0

    for value in a:
        a_squared_sum += value**2

    for value in b:
        b_squared_sum += value**2
    if a_squared_sum == 0.0 or b_squared_sum == 0.0:
        raise ValueError("Vectors must not be zero vectors.")

    a_norm = a_squared_sum**0.5

    b_norm = b_squared_sum**0.5

    dot_product = 0.0
    for i in range(len(a)):
        dot_product += a[i] * b[i]

    similarity = dot_product / (a_norm * b_norm)
    return similarity


def pairwise_similarity(
    query: list[float],
    documents: list[list[float]],
) -> list[float]:
    """Return one cosine-similarity score per document, in document order.

    The document comparison steps are left for the learner to implement.
    """
    if not query:
        raise ValueError("Query must not be empty.")

    if not documents:
        raise ValueError("Documents must not be empty.")

    scores: list[float] = []
    for document in documents:
        score = cosine_similarity(query, document)
        scores.append(score)
    return scores

    # Each document needs one score at the corresponding position in this list.
    # TODO(user): Iterate through the documents in their original order.
    # TODO(user): Use the existing cosine-similarity function for each document.
    # TODO(user): Add each resulting score to scores.
    # TODO(user): Complete the score list before it is returned.
    return scores

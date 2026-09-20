import pytest

from vector_search.similarity import cosine_similarity, normalize_vector, pairwise_similarity


def test_normalize_vector_returns_expected_values() -> None:
    normalized = normalize_vector([3.0, 4.0])

    assert normalized == pytest.approx([0.6, 0.8])


def test_normalized_vector_has_l2_norm_one() -> None:
    normalized = normalize_vector([3.0, 4.0])
    squared_sum = 0.0

    for value in normalized:
        squared_sum += value * value

    norm = squared_sum**0.5

    assert norm == pytest.approx(1.0)


def test_cosine_similarity_for_identical_direction() -> None:
    result = cosine_similarity([1.0, 2.0], [1.0, 2.0])

    assert result == pytest.approx(1.0)


def test_cosine_similarity_for_orthogonal_vectors() -> None:
    result = cosine_similarity([1.0, 0.0], [0.0, 1.0])

    assert result == pytest.approx(0.0)


def test_cosine_similarity_for_opposite_direction() -> None:
    result = cosine_similarity([1.0, 0.0], [-1.0, 0.0])

    assert result == pytest.approx(-1.0)


def test_cosine_similarity_for_same_direction_with_different_magnitude() -> None:
    result = cosine_similarity([1.0, 2.0], [2.0, 4.0])

    assert result == pytest.approx(1.0)


def test_cosine_similarity_rejects_dimension_mismatch() -> None:
    with pytest.raises(ValueError, match="same number of dimensions"):
        cosine_similarity([1.0, 2.0], [1.0])


@pytest.mark.parametrize(
    ("function", "arguments"),
    [
        (normalize_vector, ([0.0, 0.0],)),
        (cosine_similarity, ([0.0, 0.0], [1.0, 0.0])),
    ],
)
def test_similarity_functions_reject_zero_vectors(
    function: object,
    arguments: tuple[list[float], ...],
) -> None:
    with pytest.raises(ValueError, match="zero vector"):
        function(*arguments)


@pytest.mark.parametrize(
    ("function", "arguments"),
    [
        (normalize_vector, ([],)),
        (cosine_similarity, ([], [1.0])),
        (cosine_similarity, ([1.0], [])),
    ],
)
def test_similarity_functions_reject_empty_vectors(
    function: object,
    arguments: tuple[list[float], ...],
) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        function(*arguments)


def test_pairwise_similarity_scores_multiple_documents() -> None:
    documents = [[1.0, 0.0], [0.0, 1.0], [-1.0, 0.0]]

    scores = pairwise_similarity([1.0, 0.0], documents)

    assert scores == pytest.approx([1.0, 0.0, -1.0])


def test_pairwise_similarity_preserves_document_order() -> None:
    documents = [[0.0, 1.0], [-1.0, 0.0], [1.0, 0.0]]

    scores = pairwise_similarity([1.0, 0.0], documents)

    assert scores == pytest.approx([0.0, -1.0, 1.0])


def test_pairwise_similarity_rejects_empty_query() -> None:
    with pytest.raises(ValueError, match="Query must not be empty"):
        pairwise_similarity([], [[1.0, 0.0]])


def test_pairwise_similarity_rejects_empty_document_list() -> None:
    with pytest.raises(ValueError, match="Documents must not be empty"):
        pairwise_similarity([1.0, 0.0], [])


def test_pairwise_similarity_rejects_document_dimension_mismatch() -> None:
    with pytest.raises(ValueError, match="same number of dimensions"):
        pairwise_similarity([1.0, 0.0], [[1.0, 0.0, 0.0]])


def test_pairwise_similarity_rejects_zero_vector_document() -> None:
    with pytest.raises(ValueError, match="zero vectors"):
        pairwise_similarity([1.0, 0.0], [[0.0, 0.0]])


def test_pairwise_similarity_rejects_zero_vector_query() -> None:
    with pytest.raises(ValueError, match="zero vectors"):
        pairwise_similarity([0.0, 0.0], [[1.0, 0.0]])

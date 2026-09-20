import pytest

from vector_search.similarity import (
    cosine_similarity,
    normalize_vector,
    pairwise_similarity,
    top_k_search,
)


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


def test_top_k_search_returns_basic_top_two_ranking() -> None:
    documents = [[0.0, 1.0], [1.0, 0.0], [0.8, 0.2], [-1.0, 0.0]]

    results = top_k_search([1.0, 0.0], documents, k=2)

    assert [result[0] for result in results] == [1, 2]
    assert [result[1] for result in results] == pytest.approx([1.0, 0.9701425])
    assert results[0][1] >= results[1][1]


def test_top_k_search_with_k_one_returns_highest_ranked_document() -> None:
    documents = [[0.0, 1.0], [1.0, 0.0], [0.8, 0.2]]

    results = top_k_search([1.0, 0.0], documents, k=1)

    assert len(results) == 1
    assert results[0][0] == 1
    assert results[0][1] == pytest.approx(1.0)


def test_top_k_search_with_k_equal_to_document_count_returns_all_ranked() -> None:
    documents = [[0.0, 1.0], [1.0, 0.0], [0.8, 0.2], [-1.0, 0.0]]

    results = top_k_search([1.0, 0.0], documents, k=len(documents))

    assert [result[0] for result in results] == [1, 2, 0, 3]
    assert [result[1] for result in results] == pytest.approx([1.0, 0.9701425, 0.0, -1.0])


def test_top_k_search_result_contains_document_index_and_score() -> None:
    documents = [[0.0, 1.0], [1.0, 0.0]]

    results = top_k_search([1.0, 0.0], documents, k=1)

    assert isinstance(results[0], tuple)
    document_index, similarity_score = results[0]
    assert document_index == 1
    assert similarity_score == pytest.approx(1.0)


@pytest.mark.parametrize("k", [0, -1])
def test_top_k_search_rejects_non_positive_k(k: int) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        top_k_search([1.0, 0.0], [[1.0, 0.0]], k=k)


def test_top_k_search_rejects_k_larger_than_document_count() -> None:
    with pytest.raises(ValueError, match="number of documents"):
        top_k_search([1.0, 0.0], [[1.0, 0.0]], k=2)


def test_top_k_search_rejects_empty_document_list() -> None:
    with pytest.raises(ValueError, match="Documents must not be empty"):
        top_k_search([1.0, 0.0], [], k=1)


def test_top_k_search_propagates_document_dimension_mismatch() -> None:
    with pytest.raises(ValueError, match="same number of dimensions"):
        top_k_search([1.0, 0.0], [[1.0, 0.0, 0.0]], k=1)

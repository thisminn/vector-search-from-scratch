import pytest

from vector_search.chunking import fixed_size_chunk


def test_fixed_size_chunk_splits_text_into_sequential_chunks() -> None:
    chunks = fixed_size_chunk("ABCDEFGHIJ", 4)

    assert chunks == ["ABCD", "EFGH", "IJ"]


def test_fixed_size_chunk_handles_exact_division() -> None:
    chunks = fixed_size_chunk("ABCDEFGH", 4)

    assert chunks == ["ABCD", "EFGH"]


def test_fixed_size_chunk_returns_one_chunk_when_size_exceeds_text() -> None:
    chunks = fixed_size_chunk("ABC", 10)

    assert chunks == ["ABC"]


def test_fixed_size_chunk_preserves_korean_characters_in_order() -> None:
    text = "가나다라마바사"

    chunks = fixed_size_chunk(text, 3)

    assert chunks == ["가나다", "라마바", "사"]


def test_fixed_size_chunk_with_size_one_returns_each_character() -> None:
    chunks = fixed_size_chunk("ABC", 1)

    assert chunks == ["A", "B", "C"]


def test_fixed_size_chunk_preserves_all_characters() -> None:
    text = "fixed size chunking"

    chunks = fixed_size_chunk(text, 5)

    assert "".join(chunks) == text


def test_fixed_size_chunk_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        fixed_size_chunk("", 4)


@pytest.mark.parametrize("chunk_size", [0, -1])
def test_fixed_size_chunk_rejects_non_positive_chunk_size(chunk_size: int) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        fixed_size_chunk("ABC", chunk_size)

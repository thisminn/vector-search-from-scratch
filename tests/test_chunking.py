import pytest

from vector_search.chunking import fixed_size_chunk, overlap_chunk, sentence_chunk


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


def test_overlap_chunk_returns_basic_overlap() -> None:
    chunks = overlap_chunk("ABCDEFGHIJ", chunk_size=4, overlap=2)

    assert chunks == ["ABCD", "CDEF", "EFGH", "GHIJ"]


def test_overlap_chunk_returns_smaller_overlap_without_redundant_tail() -> None:
    chunks = overlap_chunk("ABCDEFGHIJ", chunk_size=4, overlap=1)

    assert chunks == ["ABCD", "DEFG", "GHIJ"]


def test_overlap_chunk_with_zero_overlap_matches_fixed_size_behavior() -> None:
    chunks = overlap_chunk("ABCDEFGHIJ", chunk_size=4, overlap=0)

    assert chunks == ["ABCD", "EFGH", "IJ"]


def test_overlap_chunk_returns_one_chunk_when_size_exceeds_text() -> None:
    chunks = overlap_chunk("ABC", chunk_size=10, overlap=2)

    assert chunks == ["ABC"]


def test_overlap_chunk_preserves_korean_characters_and_boundary_overlap() -> None:
    chunks = overlap_chunk("가나다라마바사", chunk_size=4, overlap=2)

    assert chunks == ["가나다라", "다라마바", "마바사"]


def test_overlap_chunk_stops_after_exact_end_coverage() -> None:
    chunks = overlap_chunk("ABCDEFGH", chunk_size=4, overlap=2)

    assert chunks == ["ABCD", "CDEF", "EFGH"]


def test_overlap_chunk_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        overlap_chunk("", chunk_size=4, overlap=2)


@pytest.mark.parametrize("chunk_size", [0, -1])
def test_overlap_chunk_rejects_non_positive_chunk_size(chunk_size: int) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        overlap_chunk("ABC", chunk_size=chunk_size, overlap=0)


def test_overlap_chunk_rejects_negative_overlap() -> None:
    with pytest.raises(ValueError, match="must not be negative"):
        overlap_chunk("ABC", chunk_size=2, overlap=-1)


def test_overlap_chunk_rejects_overlap_equal_to_chunk_size() -> None:
    with pytest.raises(ValueError, match="smaller than chunk_size"):
        overlap_chunk("ABC", chunk_size=2, overlap=2)


def test_overlap_chunk_rejects_overlap_greater_than_chunk_size() -> None:
    with pytest.raises(ValueError, match="smaller than chunk_size"):
        overlap_chunk("ABC", chunk_size=2, overlap=3)


def test_sentence_chunk_splits_period_separated_text() -> None:
    sentences = sentence_chunk("첫 문장이다. 두 번째 문장이다.")

    assert sentences == ["첫 문장이다.", "두 번째 문장이다."]


def test_sentence_chunk_supports_multiple_punctuation_types() -> None:
    sentences = sentence_chunk("정말인가? 그렇다! 끝이다.")

    assert sentences == ["정말인가?", "그렇다!", "끝이다."]


def test_sentence_chunk_keeps_remaining_text_without_final_punctuation() -> None:
    sentences = sentence_chunk("첫 문장이다. 마지막 문장은 끝표시가 없다")

    assert sentences == ["첫 문장이다.", "마지막 문장은 끝표시가 없다"]


def test_sentence_chunk_returns_one_sentence() -> None:
    sentences = sentence_chunk("하나의 문장이다.")

    assert sentences == ["하나의 문장이다."]


def test_sentence_chunk_strips_boundary_whitespace() -> None:
    sentences = sentence_chunk("  첫 문장이다.   두 번째 문장이다.  ")

    assert sentences == ["첫 문장이다.", "두 번째 문장이다."]


def test_sentence_chunk_preserves_korean_content_and_order() -> None:
    sentences = sentence_chunk("검색은 중요하다! 청크는 문서를 나눈다.")

    assert sentences == ["검색은 중요하다!", "청크는 문서를 나눈다."]


def test_sentence_chunk_preserves_english_content() -> None:
    sentences = sentence_chunk("Vector search works. Cosine similarity compares direction.")

    assert sentences == ["Vector search works.", "Cosine similarity compares direction."]


def test_sentence_chunk_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        sentence_chunk("")

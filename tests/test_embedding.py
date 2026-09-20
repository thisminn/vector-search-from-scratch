import pytest

from vector_search.embedding import prepare_passage_text, prepare_query_text


def test_prepare_query_text_adds_e5_query_prefix() -> None:
    prepared_query = prepare_query_text("코사인 유사도는 무엇인가?")

    assert prepared_query == "query: 코사인 유사도는 무엇인가?"


def test_prepare_passage_text_adds_e5_passage_prefix() -> None:
    prepared_passage = prepare_passage_text("코사인 유사도는 두 벡터의 방향을 비교한다.")

    assert prepared_passage == "passage: 코사인 유사도는 두 벡터의 방향을 비교한다."


def test_prepare_query_text_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        prepare_query_text("")


def test_prepare_passage_text_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        prepare_passage_text("")

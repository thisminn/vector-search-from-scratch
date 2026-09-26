"""Character-based chunking learning exercises."""


def fixed_size_chunk(
    text: str,
    chunk_size: int,
) -> list[str]:
    """Split text into sequential fixed-size character chunks.

    This first exercise uses characters, not tokens, sentences, or semantic units.
    """
    if not text:
        raise ValueError("Text must not be empty.")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    # TODO(user): Create the output chunk list.
    chunks: list[str] = []
    # TODO(user): Traverse the text using sequential chunk boundaries.
    for start in range(0, len(text), chunk_size):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

    return chunks

    # TODO(user): Move through the text in steps of chunk_size.
    # TODO(user): Slice each character chunk from its start through its boundary.
    # TODO(user): Add each sliced chunk to the output list.
    # TODO(user): Return the completed chunk list.
    raise NotImplementedError("Complete the fixed-size character chunking TODOs first.")


def overlap_chunk(
    text: str,
    chunk_size: int,
    overlap: int,
) -> list[str]:
    """Split text into overlapping fixed-size character chunks.

    This exercise is character-based. Token, sentence, and semantic chunking come later.
    """
    if not text:
        raise ValueError("Text must not be empty.")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if overlap < 0:
        raise ValueError("overlap must not be negative.")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size.")

    chunks: list[str] = []
    step = chunk_size - overlap
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        if end >= len(text):
            break

        start += step

    return chunks

    # TODO(user): Create the output chunk list.

    # TODO(user): Calculate the traversal step from chunk_size and overlap.
    # TODO(user): Track the current chunk start position.
    # TODO(user): Calculate the current chunk end position.
    # TODO(user): Slice the text for the current character chunk.
    # TODO(user): Add the chunk to the output list.
    # TODO(user): Detect when the current chunk has reached the end of the text.
    # TODO(user): Stop before adding a redundant trailing chunk.
    # TODO(user): Advance the start position by the traversal step.
    # TODO(user): Return the completed chunk list.
    raise NotImplementedError("Complete the overlap character chunking TODOs first.")


def sentence_chunk(text: str) -> list[str]:
    """Split text at basic sentence-ending punctuation."""
    if not text:
        raise ValueError("Text must not be empty.")

    sentences: list[str] = []
    current_sentence: list[str] = []

    for char in text:
        current_sentence.append(char)

        if char in ".!?":
            sentence = "".join(current_sentence).strip()

            if sentence:
                sentences.append(sentence)

            current_sentence = []

    remaining = "".join(current_sentence).strip()

    if remaining:
        sentences.append(remaining)

    if not text:
        raise ValueError("Text must not be empty.")
    return sentences

    # TODO(user): Create the output sentence list.
    # TODO(user): Create a buffer for the current sentence characters.
    # TODO(user): Iterate through the input text one character at a time.
    # TODO(user): Add each character to the current sentence buffer.
    # TODO(user): Detect period, exclamation mark, and question mark boundaries.
    # TODO(user): Join, trim, append, and reset when a sentence ends.
    # TODO(user): Handle remaining text that has no final sentence punctuation.
    # TODO(user): Return the completed sentence list.
    raise NotImplementedError("Complete the sentence chunking TODOs first.")

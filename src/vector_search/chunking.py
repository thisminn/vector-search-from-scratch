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

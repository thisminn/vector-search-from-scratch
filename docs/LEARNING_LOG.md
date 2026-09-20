# Learning Log

## Concepts Learned

- L2 normalization changes a vector to unit length while preserving its direction.
- Cosine similarity compares vector directions; for normalized vectors, their dot product equals cosine similarity.
- Pairwise similarity produces one score for each document against a query.
- Brute-force retrieval ranks every document score directly.
- Top-K ranking used `enumerate()`, `sorted()`, a lambda sort key, descending order, and list slicing.
- Multilingual E5 uses `query:` for queries and `passage:` for documents.
- Text can be represented as a 384-dimensional embedding and converted from an `ndarray` into Python lists for the hand-written retrieval code.
- Retrieval results use document indexes that must be mapped back to the original document records.
- Top-K always returns K candidates when enough documents exist, even when lower-ranked candidates are weakly related or irrelevant.
- A cosine similarity score is not a probability.

## Directly Implemented

- Vector normalization, cosine similarity, pairwise scoring, and brute-force Top-K ranking.
- E5 query and passage preparation, query and document encoding, and `ndarray` to Python-list conversion.
- A real multilingual-e5-small retrieval experiment using 23 synthetic Korean documents.
- Mapping returned Top-K document indexes back to document IDs and text.

## Needs Review

- Learn chunking before expanding the experiment to chunk-level retrieval.
- Design a later, explicit evaluation approach before making any performance claims.

## Interview Questions

- Why does normalization make a dot product equivalent to cosine similarity?
- What are the time and memory costs of brute-force Top-K search?
- Why can a Top-K result include weak candidates even when the rank-1 result is relevant?
- Why do E5 models distinguish query and passage prefixes?

## Manual Experiment Observation

The top-ranked result was directly relevant for all five manual queries. Lower ranks sometimes contained weaker or irrelevant candidates. This observation is not a statistically meaningful accuracy measurement.

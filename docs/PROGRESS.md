# Progress

## Current Phase

Week 1 vector, embedding, and brute-force retrieval milestone — completed.

## Current Week

Current learning milestone: completed vector retrieval from hand-written similarity through real text embeddings.

## Completed

- Implemented and manually verified L2 norm, vector normalization, dot product, cosine similarity, pairwise similarity, and brute-force Top-K search.
- Integrated `intfloat/multilingual-e5-small` with Sentence Transformers 5.7.0 on Python 3.13.2 and Apple MPS.
- Prepared E5 `query:` and `passage:` inputs, generated query and document embeddings, and converted model `ndarray` outputs to Python lists for the hand-written retrieval functions.
- Completed a real retrieval experiment over 23 synthetic Korean documents and mapped Top-K indexes back to their source records.
- Inspected five manual queries: brute-force search, Git branches, relational databases, operating systems, and Python testing. The directly relevant document ranked first for each query.

## In Progress

- Reflect on the manual retrieval observations and use them to guide the next learning milestone.

## Next

- Learn chunking and prepare documents for chunk-level retrieval experiments.

## Pulled Forward

- None.

## Delayed

- None.

## Evidence

- `33 passed` in the most recently verified pytest run.
- Ruff lint and Ruff format checks passed.
- `multilingual-e5-small` loaded successfully on `mps:0` and produced 384-dimensional embeddings.
- The 23-document manual experiment confirmed rank-1 relevance for five inspected queries. Lower-ranked Top-K candidates could be weakly related or irrelevant.
- This is a small learning experiment, not a formal retrieval evaluation or benchmark. BM25, hybrid retrieval, FAISS/vector indexes, reranking, and end-to-end RAG have not been implemented.

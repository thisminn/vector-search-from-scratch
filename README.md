# Vector Search from Scratch

This is a learning-focused project for understanding information retrieval and vector search fundamentals by building them incrementally from first principles.

## Learning goals

- Understand vectors and embeddings.
- Implement and test core vector operations transparently.
- Learn chunking, sparse retrieval, BM25, and dense retrieval in stages.
- Compare retrieval approaches and, later, vector-index behavior.

## Planned scope

The project will progress from manual vector operations and brute-force search to chunking, sparse retrieval, dense retrieval, and later FAISS comparisons. Each topic will be added only when it becomes an explicit learning task.

## Current status

Phase 0: scaffold initialization. No retrieval algorithms or experiment results are included yet.

## Environment and setup

This project targets Python 3.13 and uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

## Planned repository structure

```text
├── src/vector_search/  # Learning implementations, added incrementally
├── tests/              # Tests for completed learning tasks
├── notebooks/          # Experiments and visualizations
├── data/sample/        # Small, version-controlled sample data
└── docs/               # Progress, decisions, learning, and ownership records
```

Core retrieval algorithms will be implemented incrementally from first principles. This repository intentionally does not provide premature implementations of future learning tasks.

# Ownership

| Component | Designed by User | Implemented by User | Codex-assisted | External Library | User Verification Completed |
| --- | --- | --- | --- | --- | --- |
| Repository structure | Yes | No | Yes | None | Yes |
| Project and development-tool configuration | Yes | No | Yes | uv, pytest, Ruff | Yes |
| Documentation templates | Yes | No | Yes | None | Yes |
| Package import smoke test | Yes | No | Yes | pytest | Yes |
| Vector normalization and cosine similarity | Yes | Yes | Yes, test skeletons | None | Yes |
| Pairwise document iteration | Yes | Yes | Yes, learning skeleton and tests | None | Yes |
| Brute-force Top-K ranking | Yes | Yes | Yes, learning skeleton and tests | None | Yes |
| E5 query and passage preparation | Yes | Yes | Yes, embedding skeleton and tests | Sentence Transformers model input convention | Yes |
| Query and document encoding with list conversion | Yes | Yes | Yes, embedding skeleton | Sentence Transformers, PyTorch/runtime dependencies | Yes |
| Embedding-to-Top-K experiment connection | Yes | Yes | Yes, experiment-script boilerplate | Sentence Transformers, `intfloat/multilingual-e5-small` | Yes |
| Document-index-to-record mapping and result display | Yes | Yes | Yes, experiment-script boilerplate | None | Yes |
| Synthetic Korean sample dataset | Yes | No | Yes | None | Yes |
| Embedding model inference | Selected by User | No | Yes, dependency and compatibility work | Sentence Transformers, `intfloat/multilingual-e5-small`, PyTorch/runtime dependencies | Yes |

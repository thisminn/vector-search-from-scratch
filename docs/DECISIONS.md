# Decisions

## 1. Dependency and environment management

**Decision**  
Use `uv` rather than `venv + pip` or Poetry.

**Options Considered**  
`uv`; `venv + pip`; Poetry.

**Selected Option**  
`uv`.

**Reason**  
It provides a concise, reproducible workflow that matches the approved project environment.

**Trade-off**  
Contributors need to use `uv` for the standard workflow.

**Date**  
2026-08-20

## 2. Code and notebook workflow

**Decision**  
Use script-first development with notebooks reserved for experiments and visualization.

**Options Considered**  
Script-first with experimental notebooks; notebook-first development.

**Selected Option**  
Script-first with experimental notebooks.

**Reason**  
Core learning code stays reviewable and testable while notebooks support exploration.

**Trade-off**  
Exploratory work may need to be moved into scripts when it becomes reusable code.

**Date**  
2026-08-20

## 3. Project metadata and lockfile

**Decision**  
Use `pyproject.toml` with `uv.lock`.

**Options Considered**  
`pyproject.toml + uv.lock`; requirements files without a lockfile.

**Selected Option**  
`pyproject.toml + uv.lock`.

**Reason**  
It centralizes project configuration and records reproducible resolved dependencies.

**Trade-off**  
The lockfile changes when dependency resolution changes.

**Date**  
2026-08-20

## 4. Repository boundaries

**Decision**  
Keep `vector-search-from-scratch` and `reliable-rag` as separate Git repositories.

**Options Considered**  
Separate repositories; a combined repository.

**Selected Option**  
Separate repositories.

**Reason**  
The learning project remains focused and has an independent history and scope.

**Trade-off**  
Shared ideas or utilities must be intentionally transferred between repositories.

**Date**  
2026-08-20

## 5. Tests and code quality

**Decision**  
Use pytest and Ruff.

**Options Considered**  
pytest + Ruff; ad hoc checks; multiple separate lint and formatting tools.

**Selected Option**  
pytest + Ruff.

**Reason**  
They provide lightweight testing, linting, and formatting suitable for incremental learning work.

**Trade-off**  
Tool configuration should remain minimal as the project evolves.

**Date**  
2026-08-20

## 6. Package layout

**Decision**  
Use a `src` layout with the `vector_search` package.

**Options Considered**  
`src` layout; package at the repository root.

**Selected Option**  
`src` layout.

**Reason**  
It separates importable application code from tests and project files.

**Trade-off**  
Tests must run in the configured project environment.

**Date**  
2026-08-20

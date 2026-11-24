
# CodeAtlas

An AI-powered codebase search and debugging platform designed
to help developers navigate, understand, and analyze software
repositories.

## Project Status

Under active development — v0.1.0

## Overview

CodeAtlas aims to help developers search source code using
natural language, understand unfamiliar codebases, and receive
AI-generated explanations grounded in actual source files.

## Implemented Features

- FastAPI backend
- REST API endpoints
- Health-check endpoint
- Interactive Swagger API documentation
- Automated API tests with pytest
- Modular backend architecture

## Planned Features

- GitHub repository ingestion
- Source code indexing
- Keyword and semantic search
- PostgreSQL and pgvector integration
- AI-powered code explanations
- Source file and line references
- React and TypeScript frontend
- Docker containerization
- GitHub Actions CI/CD
- Performance benchmarking

## Technology Stack

### Current
- Python
- FastAPI
- Uvicorn
- pytest

### Planned
- PostgreSQL
- pgvector
- Hugging Face
- Redis
- React
- TypeScript
- Docker
- AWS

## Getting Started

Clone the repository:

```bash
git clone https://github.com/soul999cpu/codeatlas.git
cd codeatlas
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the backend:

```bash
python -m uvicorn backend.app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Application information |
| GET | /health | Service health check |
| GET | /docs | Interactive API documentation |

## Testing

```bash
python -m pytest backend/tests -v
```

## License

MIT License

## Author

Moulc Doumbia
Computer Science — University of Central Arkansas

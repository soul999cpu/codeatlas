
from fastapi import FastAPI

app = FastAPI(
    title="CodeAtlas API",
    description="AI-powered codebase search and debugging platform.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CodeAtlas",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "codeatlas-api"
    }

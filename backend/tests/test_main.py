
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to CodeAtlas",
        "version": "0.1.0"
    }


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "codeatlas-api"
    }


def test_invalid_endpoint():
    response = client.get("/invalid")

    assert response.status_code == 404

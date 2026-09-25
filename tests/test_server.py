from fastapi.testclient import TestClient

from app.server import app


client = TestClient(app)


def test_root_returns_service_metadata():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"
    assert response.json()["docs"] == "/docs"


def test_health_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_short_question_is_rejected():
    response = client.post("/ask", json={"question": "?"})

    assert response.status_code == 422

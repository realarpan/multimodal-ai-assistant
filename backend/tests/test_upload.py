import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "alive"

def test_readiness_endpoint():
    response = client.get("/ready")
    assert response.status_code == 200
    assert "ready" in response.json()

def test_upload_image():
    with open("tests/fixtures/sample.jpg", "rb") as f:
        response = client.post(
            "/api/upload",
            files={"file": ("sample.jpg", f, "image/jpeg")}
        )
    assert response.status_code == 200
    assert "task_id" in response.json()

def test_upload_invalid_format():
    response = client.post(
        "/api/upload",
        files={"file": ("test.txt", b"invalid", "text/plain")}
    )
    assert response.status_code == 400

def test_chat_streaming():
    response = client.post(
        "/api/chat",
        json={"message": "What's in this image?"}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/event-stream"

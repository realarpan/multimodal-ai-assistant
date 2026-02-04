"""Test suite for multimodal AI assistant backend."""
import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


class TestHealthEndpoints:
    """Test health check endpoints."""

    def test_health_endpoint(self):
        """Test GET /health endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data or "message" in data

    def test_readiness_endpoint(self):
        """Test GET /ready endpoint."""
        response = client.get("/ready")
        # May return 200 or 503 depending on service health
        assert response.status_code in [200, 503]


class TestRootEndpoint:
    """Test root endpoint."""

    def test_root_endpoint(self):
        """Test GET / endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data or "Multimodal" in str(data)

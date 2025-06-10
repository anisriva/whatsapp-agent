import pytest
from app.app import app 
from fastapi.testclient import TestClient

client = TestClient(app)

def test_not_found_handler():
    response = client.get("/path/that/does/not/exist")
    assert response.status_code == 404
    expected_response = {
        "status": "error",
        "message": "Not Found",
        "error": "Resource not found",
        "data" : None
    }
    assert response.status_code == 404
    assert response.json() == expected_response

def test_method_not_allowed_handler():
    # Attempt to POST to an endpoint that only supports GET
    response = client.post("/api/v1/health")
    assert response.status_code == 405
    assert response.json().get("detail") == "Method Not Allowed"
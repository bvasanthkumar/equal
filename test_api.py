import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your file is named main.py

@pytest.fixture
def client():
    """Fixture to provide a fresh TestClient for each test."""
    with TestClient(app) as c:
        yield c

def test_health_check(client):
    """Verifies that the health check endpoint returns status: ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_octocat_gists_format(client):
    """
    Tests that the response matches the dictionary structure 
    defined in the server code.
    """
    response = client.get("/octocat")
    
    # 1. Check HTTP Status
    assert response.status_code == 200
    
    data = response.json()
    
    # 2. Check the Top-Level Keys (Matches your 'return' statement)
    assert "user" in data
    assert data["user"] == "octocat"
    assert "public_gists" in data
    
    # 3. Check the List inside 'public_gists'
    gists_list = data["public_gists"]
    assert isinstance(gists_list, list)
    
    # 4. Check the structure of a single Gist (if any exist)
    if len(gists_list) > 0:
        first_gist = gists_list[0]
        assert "id" in first_gist
        assert "description" in first_gist
        assert "url" in first_gist
        assert "files" in first_gist
        assert isinstance(first_gist["files"], list)

def test_user_not_found(client):
    """Verifies the 404 logic for a non-existent user."""
    response = client.get("/this-user-is-fake-1234567890")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
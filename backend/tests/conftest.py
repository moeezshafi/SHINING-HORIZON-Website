import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Share Test Client for API/router tests."""
    # What to TODO: add test database

    with TestClient(app) as client:
        yield client
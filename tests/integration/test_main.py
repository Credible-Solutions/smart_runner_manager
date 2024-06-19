# from unittest import mock

# import pytest
from fastapi.testclient import TestClient

from srm.main import app

client = TestClient(app)


def test_integration():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}

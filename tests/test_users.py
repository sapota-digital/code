import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

USER_PAYLOAD = {"name": "Alice", "email": "alice@example.com"}


def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user():
    response = client.post("/users/", json=USER_PAYLOAD)
    assert response.status_code == 201
    assert response.json() == {"id": 1, **USER_PAYLOAD}


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1}


def test_update_user():
    response = client.put("/users/1", json=USER_PAYLOAD)
    assert response.status_code == 200
    assert response.json() == {"id": 1, **USER_PAYLOAD}


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 204

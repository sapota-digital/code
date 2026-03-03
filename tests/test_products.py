from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

PRODUCT_PAYLOAD = {"name": "Widget", "price": 9.99}


def test_list_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_product():
    response = client.post("/products/", json=PRODUCT_PAYLOAD)
    assert response.status_code == 201
    assert response.json() == {"id": 1, **PRODUCT_PAYLOAD}


def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1}


def test_update_product():
    response = client.put("/products/1", json=PRODUCT_PAYLOAD)
    assert response.status_code == 200
    assert response.json() == {"id": 1, **PRODUCT_PAYLOAD}


def test_delete_product():
    response = client.delete("/products/1")
    assert response.status_code == 204

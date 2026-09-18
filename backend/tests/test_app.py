from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_products():
    client = app.test_client()

    response = client.get("/products")

    assert response.status_code == 200
    assert len(response.get_json()) == 3


def test_product():
    client = app.test_client()

    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.get_json()["name"] == "Laptop"


def test_product_not_found():
    client = app.test_client()

    response = client.get("/products/999")

    assert response.status_code == 404
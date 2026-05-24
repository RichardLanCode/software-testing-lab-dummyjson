import requests
import pytest

BASE_URL = "https://dummyjson.com"


@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}", timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert "title" in data
    assert "price" in data
    assert "category" in data


@pytest.mark.parametrize("keyword", ["phone", "laptop", "fragrance"])
def test_search_products(keyword):
    response = requests.get(
        f"{BASE_URL}/products/search",
        params={"q": keyword},
        timeout=10,
    )

    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert isinstance(data["products"], list)


def test_invalid_product_id():
    response = requests.get(f"{BASE_URL}/products/999999", timeout=10)

    assert response.status_code == 404


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert "firstName" in data
    assert "lastName" in data
    assert "email" in data


def test_invalid_user_id():
    response = requests.get(f"{BASE_URL}/users/999999", timeout=10)

    assert response.status_code == 404

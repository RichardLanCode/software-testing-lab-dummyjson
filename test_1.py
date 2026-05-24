import requests
import pytest

BASE_URL = "https://dummyjson.com"

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
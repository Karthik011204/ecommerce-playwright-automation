import json
import pytest
import requests

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "reqres_9136ca630b814cdda7f9bc7acc4b3f84"
}


@pytest.mark.api
def test_get_users():
    response = requests.get(
        f"{BASE_URL}/users?page=2",
        headers=HEADERS
    )

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200


@pytest.mark.api
def test_create_users():
    with open("testdata/create_users.json") as file:
        users = json.load(file)

    for user in users:
        response = requests.post(
            f"{BASE_URL}/users",
            headers=HEADERS,
            json=user
        )

        print(response.status_code)
        print(response.json())

        assert response.status_code == 201


@pytest.mark.api
def test_update_users():
    with open("testdata/update_users.json") as file:
        users = json.load(file)

    user_id = 1

    for user in users:
        response = requests.put(
            f"{BASE_URL}/users/{user_id}",
            headers=HEADERS,
            json=user
        )

        print(response.status_code)
        print(response.json())

        assert response.status_code == 200

        user_id += 1


@pytest.mark.api
def test_delete_users():
    user_ids = [1, 2, 3]

    for user_id in user_ids:
        response = requests.delete(
            f"{BASE_URL}/users/{user_id}",
            headers=HEADERS
        )

        print(response.status_code)

        assert response.status_code == 204

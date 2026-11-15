import allure
import requests


def test_get_user_info(user_lifecycle, api_url):
    """Verify user data"""
    with allure.step("GET /users/me"):
        response = requests.get(
            f"{api_url}/users/me",
            headers={"Authorization": f"Bearer {user_lifecycle['token']}"}
        )

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify user data"):
        body = response.json()
        assert body["email"] == user_lifecycle["user"].email
        assert body["firstName"] == user_lifecycle["user"].firstName
        assert body["lastName"] == user_lifecycle["user"].lastName
        assert "password" not in body
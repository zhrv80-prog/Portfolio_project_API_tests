import uuid
import allure
import requests


def test_update_user(user, api_url):
    """
    Verify opportunity to update data through PATCH /users/me.
    """
    new_email = f"updated{uuid.uuid4().hex[:8]}@example.com"

    updated_payload = {
        "firstName": "Updated",
        "lastName": "Username",
        "email": new_email,
        "password": "myNewPassword",
    }

    with allure.step("PATCH /users/me"):
        response = requests.patch(
            f"{api_url}/users/me",
            headers={"Authorization": f"Bearer {user['token']}"},
            json=updated_payload,
        )

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Update failed: {response.text}"

    with allure.step("Verify response contains updated data"):
        body = response.json()
        assert body["firstName"] == "Updated"
        assert body["lastName"] == "Username"
        assert body["email"] == new_email
        assert "password" not in body
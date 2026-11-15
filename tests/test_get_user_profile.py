import allure
import pytest


@pytest.mark.smoke
def test_get_user_info(user, users_api):
    """Проверяет получение информации о пользователе."""
    response = users_api.get_me(user["token"])

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Get failed: {response.text}"

    with allure.step("Verify user data"):
        body = response.json()
        assert body["email"] == user["email"]
        assert body["firstName"] == "Marcus"
        assert "password" not in body
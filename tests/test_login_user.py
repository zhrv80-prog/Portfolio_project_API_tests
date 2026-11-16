# tests/test_login_user.py

import allure
import pytest
from models.user_models import UserLogin


@pytest.mark.smoke
def test_login_user(user, users_api, user_password):
    """Проверяет, что пользователь может залогиниться."""
    credentials = UserLogin(
        email=user["email"],
        password=user_password,
    )

    response = users_api.login(credentials)

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Login failed: {response.text}"

    with allure.step("Verify response contains token"):
        body = response.json()
        assert "token" in body
        assert body["token"] is not None
        assert body["user"]["email"] == user["email"]
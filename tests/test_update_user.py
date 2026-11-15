import uuid

import allure
import pytest

from models.user_models import UserUpdate


@pytest.mark.regression
def test_update_user(user, users_api):
    """Проверяет обновление данных пользователя."""
    new_email = f"updated{uuid.uuid4().hex[:8]}@example.com"

    updated = UserUpdate(
        firstName="Updated",
        lastName="Username",
        email=new_email,
        password="myNewPassword",
    )

    response = users_api.update(user["token"], updated)

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Update failed: {response.text}"

    with allure.step("Verify updated data"):
        body = response.json()
        assert body["firstName"] == "Updated"
        assert body["lastName"] == "Username"
        assert body["email"] == new_email
        assert "password" not in body
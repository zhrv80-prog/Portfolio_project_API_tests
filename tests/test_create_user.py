import allure
import pytest


@pytest.mark.smoke
def test_create_user(user):
    """Проверяет, что пользователь создан с правильными данными."""
    with allure.step("Verify user data"):
        assert user["email"] is not None
        assert user["token"] is not None
        assert user["user"].firstName == "Marcus"
        assert user["user"].lastName == "William"
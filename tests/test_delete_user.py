import allure
import pytest


@pytest.mark.regression
def test_delete_user(user, users_api):
    """Проверяет удаление пользователя."""
    response = users_api.delete(user["token"])

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Delete failed: {response.text}"

    with allure.step("Verify user is deleted"):
        check = users_api.get_me(user["token"])
        assert check.status_code == 401, (
            f"Expected 401 after delete, got {check.status_code}"
        )
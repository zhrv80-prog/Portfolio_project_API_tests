# tests/test_logout_user.py

import allure
import pytest


@pytest.mark.smoke
def test_logout_user(user, users_api):
    """
    Проверяет, что пользователь может разлогиниться.
    После logout токен становится недействительным.
    """
    # 1. Проверяем, что до logout токен работает
    with allure.step("Verify token works before logout"):
        check_before = users_api.get_me(user["token"])
        assert check_before.status_code == 200, "Token should work before logout"

    # 2. Выполняем logout
    with allure.step("POST /users/logout"):
        response = users_api.logout(user["token"])

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200, f"Logout failed: {response.text}"

    # 3. Проверяем, что после logout токен не работает
    with allure.step("Verify token is invalid after logout"):
        check_after = users_api.get_me(user["token"])
        assert check_after.status_code == 401, (
            f"Expected 401 after logout, got {check_after.status_code}"
        )
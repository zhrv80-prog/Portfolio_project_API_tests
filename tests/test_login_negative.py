import allure
import pytest
from models.user_models import UserLogin


@pytest.mark.negative
@pytest.mark.parametrize("credentials, expected_status, description", [
    (UserLogin(email="", password="password"), 401, "Empty email"),
    (UserLogin(email="test@fake.com", password=""), 401, "Empty password"),
    (UserLogin(email="nonexistent@fake.com", password="pass"), 401, "Nonexistent user"),
    (UserLogin(email="test@fake.com", password="wrong"), 401, "Wrong password"),
])
def test_login_invalid(credentials, expected_status, description, users_api):
    """Проверяет, что невалидные данные отклоняются."""
    with allure.step(f"Login with {description}"):
        response = users_api.login(credentials)

    with allure.step(f"Verify status code is {expected_status}"):
        assert response.status_code == expected_status, (
            f"Expected {expected_status}, got {response.status_code}. "
            f"Body: {response.text}"
        )
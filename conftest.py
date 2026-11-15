import os
import uuid

import pytest

from api.users_api import UsersApi
from models.user_models import User


@pytest.fixture
def api_url() -> str:
    return "https://thinking-tester-contact-list.herokuapp.com"


@pytest.fixture
def user_password() -> str:
    password = os.getenv("MY_APP_PASSWORD")
    assert password is not None, "MY_APP_PASSWORD is not set"
    return password


@pytest.fixture
def users_api(api_url) -> UsersApi:
    return UsersApi(api_url)


@pytest.fixture
def user(users_api, user_password):
    """Создаёт пользователя и удаляет его после теста."""
    email = f"testuser{uuid.uuid4().hex[:8]}@example.com"
    user = User(
        firstName="Marcus",
        lastName="William",
        email=email,
        password=user_password,
    )

    response = users_api.create(user)
    assert response.status_code == 201, f"Create failed: {response.text}"

    body = response.json()
    token = body["token"]

    yield {
        "email": email,
        "token": token,
        "user": user,
    }

    # --- TEARDOWN ---
    try:
        users_api.delete(token)
    except Exception as e:
        print(f"Warning: Failed to delete user {email}: {e}")
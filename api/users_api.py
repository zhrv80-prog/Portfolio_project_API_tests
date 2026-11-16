import logging
import allure
import requests

from models.user_models import User, UserUpdate, UserLogin

logger = logging.getLogger(__name__)


class UsersApi:
    """Клиент для работы с эндпоинтами /users."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    # --- CREATE ---
    def create(self, user: User) -> requests.Response:
        with allure.step(f"POST /users (email={user.email})"):
            response = self.session.post(
                f"{self.base_url}/users",
                json=user.to_dict(),
            )
            logger.info(f"POST /users → {response.status_code}")
            return response

    # --- GET ---
    def get_me(self, token: str) -> requests.Response:
        with allure.step("GET /users/me"):
            response = self.session.get(
                f"{self.base_url}/users/me",
                headers=self._auth_headers(token),
            )
            logger.info(f"GET /users/me → {response.status_code}")
            return response

    # --- UPDATE ---
    def update(self, token: str, update: UserUpdate) -> requests.Response:
        with allure.step(f"PATCH /users/me ({update.to_dict()})"):
            response = self.session.patch(
                f"{self.base_url}/users/me",
                headers=self._auth_headers(token),
                json=update.to_dict(),
            )
            logger.info(f"PATCH /users/me → {response.status_code}")
            return response

    # --- DELETE ---
    def delete(self, token: str) -> requests.Response:
        with allure.step("DELETE /users/me"):
            response = self.session.delete(
                f"{self.base_url}/users/me",
                headers=self._auth_headers(token),
            )
            logger.info(f"DELETE /users/me → {response.status_code}")
            return response

    # --- LOGIN ---
    def login(self, credentials: UserLogin) -> requests.Response:
        with allure.step(f"POST /users/login (email={credentials.email})"):
            response = self.session.post(
                f"{self.base_url}/users/login",
                json=credentials.to_dict(),
            )
            logger.info(f"POST /users/login → {response.status_code}")
            return response

    # --- LOGOUT ---
    def logout(self, token: str) -> requests.Response:
        with allure.step("POST /users/logout"):
            response = self.session.post(
                f"{self.base_url}/users/logout",
                headers=self._auth_headers(token),
            )
            logger.info(f"POST /users/logout → {response.status_code}")
            return response

    # --- helpers ---
    @staticmethod
    def _auth_headers(token: str) -> dict:
        return {"Authorization": f"Bearer {token}"}

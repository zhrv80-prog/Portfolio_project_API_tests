import allure


def test_create_user(user):
    """Verify user data"""
    with allure.step("Verify user data"):
        assert user["user"].email is not None
        assert user["user"].firstName == "Marcus"
        assert user["user"].lastName == "William"
        assert user["token"] is not None
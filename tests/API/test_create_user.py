import allure


def test_create_user(user_lifecycle):
    """Verify user data"""
    with allure.step("Verify user data"):
        assert user_lifecycle["user"].email is not None
        assert user_lifecycle["user"].firstName == "Marcus"
        assert user_lifecycle["user"].lastName == "William"
        assert user_lifecycle["token"] is not None
import pytest


@pytest.mark.parametrize(
    "email, password, username, first_name, last_name, status_code",
    [
        ("test_user1@example.ru", "pass", "user_api_1", "danya", "zenkovich", 200),
        ("test_user1@example.ru", "pass", "user_api_2", "dima", "kor", 409),
        ("test_user3@example.ru", "pass", "user_api_1", "danya", "zenkovich", 409),
        ("test_user4@example.ru", "pass", "user_api_4", "", "zenkovich", 422),
        ("test_user5@example.ru", "pass", "", "danya", "zenkovich", 422),
    ],
)
async def test_register_user(email, password, username, first_name, last_name, status_code, ac):
    response_register = await ac.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
            "username": username,
            "first_name": first_name,
            "last_name": last_name
        },
    )

    assert response_register.status_code == status_code
    if status_code == 200:
        assert response_register.json()["status"] == "OK"

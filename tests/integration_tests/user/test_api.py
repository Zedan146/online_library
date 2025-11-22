import pytest


@pytest.mark.parametrize(
    "email, password, username, first_name, last_name, status_code",
    [
        ("test_user1@example.ru", "pass", "user_api_1", "danya", "zenkovich", 200),
        ("test_user1@example.ru", "pass", "user_api_2", "dima", "kor", 409),
        ("test_user3@example.ru", "pass", "user_api_1", "danya", "zenkovich", 409),
        ("test_user4@example.ru", "pass", "user_api_4", "", "zenkovich", 422),
        ("test_user5@example.ru", "pass", "", "danya", "zenkovich", 422),
        ("test_user6@example.ru", "pass", "user_api_6", "danya", "zenkovich", 200),
    ],
)
async def test_auth_flow_user(email, password, username, first_name, last_name, status_code, ac):
    # /auth/register
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
    else:
        return

    # /auth/login
    response_login = await ac.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        }
    )

    assert response_login.status_code == 200
    assert ac.cookies["access_token"]

    # /auth/me
    response_me = await ac.get("/auth/me")
    user = response_me.json().get("user")

    assert response_me.status_code == 200
    assert user["email"] == email

    # /auth/logout
    response_logout = await ac.get("/auth/logout")
    assert response_logout.status_code == 200
    assert not ac.cookies.get("access_token")

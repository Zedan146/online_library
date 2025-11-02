from src.services.auth import AuthService


def test_decode_and_encode_access_token():
    data = {"user_id": 1}
    access_token = AuthService.create_access_token(data)

    assert access_token
    assert isinstance(access_token, str)

    payload = AuthService().decode_token(access_token)

    assert payload
    assert payload["user_id"] == data["user_id"]


def test_verify_password():
    correct_password = "correct_password"
    incorrect_password = "incorrect_password"
    hashed_password = AuthService().get_hashed_password(correct_password)

    assert isinstance(hashed_password, str)
    assert AuthService().verify_password(correct_password, hashed_password)
    assert not AuthService().verify_password(incorrect_password, hashed_password)

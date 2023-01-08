from auth.auth_handler import decode_jwt


def verify_jwt(jwt_token: str) -> bool:
    # data: The previously encoded payload
    data = decode_jwt(jwt_token)

    # Put token verification logic here
    if data is None:
        return False

    username = data.get("username")

    if username is None:
        return False

    if username != "youssef":
        return False

    return True

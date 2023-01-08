import os
import time
from typing import Dict

import jwt
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRES = int(os.getenv("JWT_EXPIRES"))


def sign_jwt(data: Dict) -> Dict[str, str]:
    payload = {
        **data,
        "expires": time.time() + JWT_EXPIRES
    }

    jwt_token = jwt.encode(payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "token": jwt_token
    }


def decode_jwt(jwt_token: str) -> Dict | None:
    try:
        data = jwt.decode(jwt_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        if data["expires"] >= time.time():
            return data
    except jwt.exceptions.DecodeError:
        return None

from typing import Any

from flask import json
from flask_jwt_extended import create_access_token


def encode_jwt(user: dict[str, Any]) -> str:
    payload_data = {
        "id": user.get("user_id", ""),
        "auth": user.get("auth_name", ""),
        "email": user.get("email", ""),
    }
    return create_access_token(identity=json.dumps(payload_data), fresh=True)

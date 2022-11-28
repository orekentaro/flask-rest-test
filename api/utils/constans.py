from typing import Final

RESPONSE_OK: Final[int] = 200
RESPONSE_BAD_REQUEST: Final[int] = 400
RESPONSE_UNAUTHORIZET: Final[int] = 401
RESPONSE_NOTFOUND: Final[int] = 404
RESPONSE_ERROR: Final[int] = 500

REQUEST_PARM_ERROR: Final[str] = "リクエストパラメーターエラー"
GENDER: Final[dict[str, str]] = {"m": "男性", "f": "女性"}

NOT_AUTH_ROUTE: Final[list[str]] = ["auth.post"]

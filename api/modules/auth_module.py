import hashlib
from typing import Any

import utils.constans as const
from flask import Response, json
from flask_jwt_extended import set_access_cookies
from models.user_master import UserMaster
from modules.base_module import BaseModule
from serializer.auth_serializer import AuthSerializer
from utils.myjwt import encode_jwt


class AuthModule(BaseModule):
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    model = UserMaster
    serializer = AuthSerializer

    def login(self, *args, **kwargs: UserMaster) -> Any:
        """
        ログイン認証API
        """
        try:
            email = kwargs.get("email", "")
            password: str = kwargs.get("password", "")
            password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            user: UserMaster = self.one_or_none(email=email, password=password)
            if user is None:
                return Response(
                    status=const.RESPONSE_UNAUTHORIZET,
                    response=json.dumps({"message": "認証情報が一致しません"}),
                )
            token = encode_jwt(user)

            response = Response(status=const.RESPONSE_OK)
            set_access_cookies(response, token)
            return response

        except Exception:
            return Response(
                status=const.RESPONSE_ERROR,
                response=json.dumps({"massage": "予期せぬエラーが発生しました"}),
            )
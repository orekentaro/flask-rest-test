import hashlib
import time

import jwt
import utils.constans as const
from flask import Response, json, request
from models.user_master import UserMaster
from modules.base_module import BaseModule
from serializer.auth_serializer import AuthSerializer


class AuthModule(BaseModule):
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    model = UserMaster
    serializer = AuthSerializer

    def login(self, *args, **kwargs: UserMaster) -> Response:
        """
        ログイン認証API
        """
        try:
            print(request)

            email = kwargs.get("email", "")
            password: str = kwargs.get("password", "")
            password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            user: UserMaster = self.one_or_none(email=email, password=password)
            if user is None:
                return Response(
                    status=const.RESPONSE_UNAUTHORIZET,
                    response=json.dumps({"message": "認証情報が一致しません"}),
                )
            iat = int(time.time())
            exp = iat + 3600
            payload_data = {
                "id": user.user_id,
                "auth": user.auth_id,
                "email": user.email,
                "iat": iat,
                "exp": exp,
            }
            self.update(**kwargs)

            return Response(status=const.RESPONSE_OK, response=json.dumps(payload_data))

        except Exception:
            return Response(
                status=const.RESPONSE_ERROR,
                response=json.dumps({"massage": "予期せぬエラーが発生しました"}),
            )

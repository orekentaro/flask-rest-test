import hashlib

from flask import Response, json, request
from flask_jwt_extended import set_access_cookies

import utils.constans as const
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

    def login(self) -> Response:
        """
        ログイン認証API
        """
        if request.form is None:
            raise Exception(const.REQUEST_PARM_ERROR)

        r: UserMaster = request.form

        email = r.get("email")
        password: str = r.get("password")
        if email is None or password is None:
            raise Exception(const.REQUEST_PARM_ERROR)
        password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        user = self.one_or_none(email=email, password=password)
        if user is None:
            return Response(
                status=const.RESPONSE_UNAUTHORIZET,
                response=json.dumps({"msg": "認証情報が一致しません"}),
            )
        user = self.serialize()
        token = encode_jwt(user)

        response = Response(status=const.RESPONSE_OK)
        set_access_cookies(response, token)
        return response

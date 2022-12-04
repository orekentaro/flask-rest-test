from flask import Blueprint, Response

from modules.auth_module import AuthModule

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/", methods=["POST"])
def post() -> Response:
    """ログインルート"""
    return AuthModule().login()

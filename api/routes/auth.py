from flask import Blueprint
from modules.auth_module import AuthModule

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/", methods=["POST"])
def post():
    """ログインルート"""
    return AuthModule().login()

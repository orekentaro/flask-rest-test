from flask import Blueprint, request
from modules.auth_module import AuthModule

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/", methods=["POST"])
def login():
    """ログインルート"""
    data = request.json
    return AuthModule().login(**data)

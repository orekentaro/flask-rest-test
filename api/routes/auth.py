from flask import Blueprint, request
from modules.user_module import UserModule

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/", methods=["POST"])
def login():
    """ログインルート"""
    data = request.json
    UserModule().login("", "")

    return data

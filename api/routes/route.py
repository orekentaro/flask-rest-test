from flask import Blueprint, jsonify, make_response, request, session
from modules.job_module import JobModule
from modules.user_module import UserModule

# ログイン不要ルート
ln = Blueprint("ln", __name__)
# ログイン必要ルート
lr = Blueprint("lr", __name__)


@lr.before_request
def before_request():
    # TODO:クッキーの内容や寿命を調整しないといけない
    if "user_id" not in session:
        return {"result": "not_login"}
    else:
        result = request.cookies.get("login", None)
        print(result)


@lr.route("/", methods=["get"])
def test():
    """befor_requestのテスト"""
    response = jsonify({"result": "ok"})
    return make_response(response)


@ln.route("/login", methods=["POST"])
def login():
    """ログインルート"""
    email = request.form["email"]
    password = request.form["password"]
    res = UserModule.login(email, password)
    result = res["result"]
    response = make_response(res)
    if result == "success":
        response.set_cookie("login", value=email, secure=None, httponly=False)
        response.set_cookie("user_id", value=res["user"], secure=None, httponly=False)
        session["user_id"] = res["user"]
    return response


@lr.route("/job_seeker", methods=["GET"])
def job_seeker():
    conditions = dict(request.args)
    res = JobModule.get_job_seeker(**conditions)
    response = make_response(res)
    return response

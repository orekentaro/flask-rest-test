import traceback

import utils.constans as const
from flask import Response, current_app, json, jsonify, logging, request
from flask_jwt_extended import decode_token
from werkzeug.datastructures import EnvironHeaders


def before_request():
    """
    リクエストの前処理
    """
    logger = logging.create_logger(current_app)
    logger.info(f"start: {request.endpoint}")
    logger.info(f"path: {request.path}")

    if request.endpoint not in const.NOT_AUTH_ROUTE:
        access_token = request.cookies.get("access_token_cookie")
        token = decode_token(access_token)
        sub = token["sub"]
        tmp_header = request.headers.__dict__
        header = tmp_header.get("environ", {})
        token_json = json.loads(sub)
        header["auth"] = token_json.get("auth", "")
        header["user"] = token_json.get("id", 0)
        request.headers = EnvironHeaders(header)


def after_request(response: Response):
    """
    リクエストの後処理
    """
    response.headers["Content-Type"] = "application/json"
    logger = logging.create_logger(current_app)
    logger.info(f"res: {response.data}")
    logger.info(f"end: {request.endpoint}")
    return response


def exception_handler(ex):
    """
    共通例外処理
    """
    logger = logging.create_logger(current_app)

    # 予期せぬ例外発生時
    logger.error(traceback.format_exc())
    return jsonify({"msg": f"予期せぬエラーが発生しました:[{ex}]"}), const.RESPONSE_ERROR

import traceback

import utils.constans as const
from flask import Response, current_app, jsonify, logging, request


def before_request():
    """
    リクエストの前処理
    """
    logger = logging.create_logger(current_app)
    logger.info(f"start: {request.endpoint}")


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

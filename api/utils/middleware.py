import traceback

from flask import Response, current_app, jsonify, logging, request

import utils.constans as const


def before_request():
    """
    リクエストの前処理
    """
    logger = logging.create_logger(current_app)
    logger.info(f"start: {request.endpoint}")
    logger.info(f"path: {request.path}")


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
    return jsonify({"msg": f"予期せぬエラーが発生しました:{ex}"}), const.RESPONSE_ERROR


def value_error_handler(ex):
    """
    共通例外処理 ValueError
    """
    logger = logging.create_logger(current_app)

    # 予期せぬ例外発生時
    logger.error(traceback.format_exc())
    return jsonify({"msg": f"バリデーションエラー:{ex}"}), const.RESPONSE_BAD_REQUEST


def not_found_handler(ex):
    """
    共通例外処理 NotFound
    """
    logger = logging.create_logger(current_app)

    # 予期せぬ例外発生時
    logger.error(traceback.format_exc())
    return jsonify({"msg": f"データが見つかりません:{ex}"}), const.RESPONSE_NOTFOUND


def bad_request_handler(ex):
    """
    共通例外処理 NotFound
    """
    logger = logging.create_logger(current_app)

    # 予期せぬ例外発生時
    logger.error(traceback.format_exc())
    return jsonify({"msg": f"リクエストが不正です:{ex}"}), const.RESPONSE_BAD_REQUEST

from flask import Blueprint, Response
from flask_jwt_extended import jwt_required
from modules.job_seeker_module import JobSeekerModule

job_seeker = Blueprint("job_seeker", __name__, url_prefix="/job_seeker")


@job_seeker.route("/", methods=["GET"])
@jwt_required()
def get() -> Response:
    """ログインルート"""
    return JobSeekerModule().get()


@job_seeker.route("/<int:job_id>", methods=["GET"])
@jwt_required()
def get_one(job_id) -> Response:
    """ログインルート"""
    return JobSeekerModule().get(job_id)


# TODO: 他のメソッドを書く

from flask import Blueprint, Response
from flask_jwt_extended import jwt_required

from modules.job_seeker_module import JobSeekerModule

job_seeker = Blueprint("job_seeker", __name__, url_prefix="/job_seeker")


@job_seeker.route("/", methods=["GET"])
@jwt_required()
def get() -> Response:
    return JobSeekerModule().get()


@job_seeker.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_one(id) -> Response:
    return JobSeekerModule().get(id)


@job_seeker.route("/", methods=["POST"])
@jwt_required()
def post() -> Response:
    return JobSeekerModule().post()


@job_seeker.route("/<int:id>", methods=["PATCH"])
@jwt_required()
def patch(id) -> Response:
    return JobSeekerModule().patch(id)


@job_seeker.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id) -> Response:
    return JobSeekerModule().delete(id)

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import BadRequest, NotFound

import utils.middleware as mw
from routes.auth import auth
from routes.job_seeker import job_seeker


def create_app():
    app = Flask(__name__)
    app.config.from_object("utils.config")
    CORS(app, supports_credentials=True)
    app.secret_key = "gwdfsgfadsdtyhjyetdgfsag0-a04o31qw@pa]:q12wegiejq8@43uqow"
    jwt = JWTManager()
    jwt.init_app(app)

    # route
    app.register_blueprint(auth)
    app.register_blueprint(job_seeker)
    app.before_request(mw.before_request)
    app.after_request(mw.after_request)

    # error handler
    app.register_error_handler(Exception, mw.exception_handler)
    app.register_error_handler(ValueError, mw.value_error_handler)
    app.register_error_handler(BadRequest, mw.bad_request_handler)
    app.register_error_handler(NotFound, mw.not_found_handler)
    return app


APP = create_app()

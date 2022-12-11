import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager


def _create_app():
    app = Flask(__name__)
    app.config.from_object("utils.config")
    CORS(app, supports_credentials=True)
    app.secret_key = "gwdfsgfadsdtyhjyetdgfsag0-a04o31qw@pa]:q12wegiejq8@43uqow"
    jwt = JWTManager()
    jwt.init_app(app)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
        **{
            "DB_USER": os.environ["POSTGRES_USER"],
            "DB_PASS": os.environ["POSTGRES_PASSWORD"],
            "DB_HOST": os.environ["DB_HOST"],
            "DB_PORT": os.environ["DB_PORT"],
            "DB_NAME": os.environ["POSTGRES_DB"],
        }
    )
    return app


APP = _create_app()

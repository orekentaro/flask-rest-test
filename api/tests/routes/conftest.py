import os

import pytest
from sqlalchemy import create_engine

from create_app import create_app
from create_table import create_table


@pytest.fixture(scope="session", autouse=True)
def app_test():

    os.environ.update({"POSTGRES_DB": "recruit-management/test"})
    app = create_app()
    app.config.update({"TESTING": True})
    db = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}".format(
        **{
            "DB_USER": os.environ["POSTGRES_USER"],
            "DB_PASS": os.environ["POSTGRES_PASSWORD"],
            "DB_HOST": os.environ["DB_HOST"],
            "DB_PORT": os.environ["DB_PORT"],
        }
    )
    engine = create_engine(db, echo=True)
    conn = engine.connect()
    conn.execution_options(isolation_level="AUTOCOMMIT").execute(
        'drop database if exists "recruit-management/test"'
    )

    conn = engine.connect()
    conn.execution_options(isolation_level="AUTOCOMMIT").execute(
        'create database "recruit-management/test"'
    )
    conn.execute("commit")
    conn.close()

    create_table()

    yield app

    conn = engine.connect()
    conn.execute(
        "select pg_terminate_backend(pid) from pg_stat_activity where datname = 'recruit-management/test';"
    )
    conn.execution_options(isolation_level="AUTOCOMMIT").execute(
        'drop database if exists "recruit-management/test"'
    )


@pytest.fixture(scope="session", autouse=True)
def client(app_test):
    return app_test.test_client()


@pytest.fixture(autouse=True)
def mock_jwt(mocker):
    mocker.patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")

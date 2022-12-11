import pytest
from create_app import create_app


@pytest.fixture(scope="session", autouse=True)
def app_test():
    app = create_app()
    app.config.update({"TESTING": True})

    # TODO:テスト用DBに接続する様に頑張る
    # yield app
    return app


@pytest.fixture(scope="session", autouse=True)
def client(app_test):
    return app_test.test_client()


@pytest.fixture(autouse=True)
def mock_jwt(mocker):
    mocker.patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")

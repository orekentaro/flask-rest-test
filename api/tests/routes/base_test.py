import pytest
from app import app


class BaseTest:
    @pytest.fixture
    def app_test(self):
        app.config.update({"TESTING": True})
        # TODO:テスト用DBに接続する様に頑張る
        # yield app
        return app

    @pytest.fixture
    def client(self, app_test):
        return app_test.test_client()

    @pytest.fixture(autouse=True)
    def mock_jwt(self, mocker):
        mocker.patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")

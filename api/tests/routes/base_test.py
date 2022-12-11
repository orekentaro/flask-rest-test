import pytest
from create_app import APP
from rb import rb


class BaseTest:
    @pytest.fixture(scope="session")
    def app_test(self):
        APP.config.update({"TESTING": True})
        app = rb(APP)

        # TODO:テスト用DBに接続する様に頑張る
        # yield app
        return app

    @pytest.fixture(scope="session")
    def client(self, app_test):
        return app_test.test_client()

    @pytest.fixture(autouse=True)
    def mock_jwt(self, mocker):
        mocker.patch("flask_jwt_extended.view_decorators.verify_jwt_in_request")

import pytest

from app import app


class TestUserModule:
    @pytest.fixture
    def app_test(self):
        app.config.update({"TESTING": True})
        # 必要なら前処理を
        # yield app
        return app

    @pytest.fixture
    def client(self, app_test):
        return app_test.test_client()

    def test_login_成功(self, client):
        with client:
            res = client.post("/auth/", json={"email": "test@test.test", "password": "password123"})
            assert res.status_code == 200

    def test_login_失敗_データなし(self, client):
        with client:
            res = client.post("/auth/", json=None)
            assert res.status_code == 500

    def test_login_ログイン失敗不一致(self, client):
        with client:
            res = client.post("/auth/", json={"email": "test@test.test", "password": "password12"})
            assert res.status_code == 401

    def test_login_値欠損(self, client):
        with client:
            res = client.post("/auth/", json={"password": "password123"})
            assert res.status_code == 500

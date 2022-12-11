from tests.routes.base_test import BaseTest


class TestUserModule(BaseTest):
    def test_login_成功(self, client):
        with client:
            res = client.post(
                "/auth/", json={"email": "test@test.test", "password": "password123"}
            )
            assert res.status_code == 200

    def test_login_失敗_データなし(self, client):
        with client:
            res = client.post("/auth/", json=None)
            assert res.status_code == 500

    def test_login_ログイン失敗不一致(self, client):
        with client:
            res = client.post(
                "/auth/", json={"email": "test@test.test", "password": "password12"}
            )
            assert res.status_code == 401

    def test_login_値欠損(self, client):
        with client:
            res = client.post("/auth/", json={"password": "password123"})
            assert res.status_code == 500

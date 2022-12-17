import utils.constans as const


def test_login_成功(client):
    with client:
        res = client.post(
            "/auth/", json={"email": "test@test.test", "password": "password123"}
        )
        assert res.status_code == const.RESPONSE_OK


def test_login_失敗_データなし(client):
    with client:
        res = client.post("/auth/", json=None)
        assert res.status_code == const.RESPONSE_BAD_REQUEST


def test_login_ログイン失敗不一致(client):
    with client:
        res = client.post(
            "/auth/", json={"email": "test@test.test", "password": "password12"}
        )
        assert res.status_code == const.RESPONSE_UNAUTHORIZET


def test_login_値欠損(client):
    with client:
        res = client.post("/auth/", json={"password": "password123"})
        assert res.status_code == const.RESPONSE_ERROR

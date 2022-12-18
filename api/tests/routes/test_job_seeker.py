from sqlalchemy import select

import utils.constans as const
from models.create_session import session
from models.job_seeker import JobSeeker


def test_get_成功(client):
    with client:
        res = client.get("/job_seeker/")
        assert res.status_code == const.RESPONSE_OK

        j = res.json
        data_list = j.get("data", [])
        assert type(data_list) == list

        data = data_list[0]
        assert data.get("memo")
        ads = data.get("ads")
        assert ads
        assert ads.get("job_master")


def test_get1_成功(client):
    with client:
        res = client.get("/job_seeker/1")
        assert res.status_code == const.RESPONSE_OK

        j = res.json
        data = j.get("data", [])
        assert type(data) == dict
        assert data.get("progress_info")
        assert data.get("memo")
        ads = data.get("ads")
        assert ads
        assert ads.get("job_master")


def test_post_成功(client):
    with client:
        payload = {
            "name": "テスト太郎",
            "gender": "f",
            "birthday": "1993-02-22",
            "career": "2021年テスト株式会社入社",
            "ads_id": 1,
            "changer": 1,
        }
        res = client.post("/job_seeker/", json=payload)
        assert res.status_code == const.RESPONSE_OK

        with session() as db_session:
            stmt = select(JobSeeker).filter_by(**payload)
            data = db_session.execute(stmt).scalars().first()

            assert data.name == payload["name"]


def test_post_名前なし(client):
    with client:
        payload = {
            "gender": "f",
            "birthday": "1993-02-22",
            "career": "2021年テスト株式会社入社",
            "ads_id": 1,
            "changer": 1,
        }
        res = client.post("/job_seeker/", json=payload)
        assert res.status_code == const.RESPONSE_BAD_REQUEST


def test_post_性別なし(client):
    with client:
        payload = {
            "name": "テスト太郎",
            "gender": "r",
            "birthday": "1993-02-22",
            "career": "2021年テスト株式会社入社",
            "ads_id": 1,
            "changer": 1,
        }
        res = client.post("/job_seeker/", json=payload)
        assert res.status_code == const.RESPONSE_BAD_REQUEST


def test_post_生年月日不正(client):
    with client:
        payload = {
            "name": "テスト太郎",
            "gender": "m",
            "birthday": "1993-22-22",
            "career": "2021年テスト株式会社入社",
            "ads_id": 1,
            "changer": 1,
        }
        res = client.post("/job_seeker/", json=payload)
        assert res.status_code == const.RESPONSE_BAD_REQUEST


def test_post_求人広告なし(client):
    with client:
        payload = {
            "name": "テスト太郎",
            "gender": "m",
            "birthday": "1993-12-22",
            "career": "2021年テスト株式会社入社",
            "ads_id": 2,
            "changer": 1,
        }
        res = client.post("/job_seeker/", json=payload)
        assert res.status_code == const.RESPONSE_BAD_REQUEST


def test_patch_成功(client):
    with client:
        payload = {
            "name": "テスト次郎",
        }
        res = client.patch("/job_seeker/1", json=payload)
        assert res.status_code == const.RESPONSE_OK
        payload.update({"id": 1})

        with session() as db_session:
            stmt = select(JobSeeker).filter_by(**payload)
            data = db_session.execute(stmt).scalars().first()
            assert data.name == payload["name"]


def test_patch_該当なし(client):
    with client:
        payload = {
            "name": "テスト次郎",
        }
        res = client.patch("/job_seeker/10", json=payload)
        assert res.status_code == const.RESPONSE_NOTFOUND


def test_patch_編集不可(client):
    with client:
        payload = {
            "ads_id": 2,
        }
        res = client.patch("/job_seeker/1", json=payload)
        assert res.status_code == const.RESPONSE_BAD_REQUEST


def test_delete_成功(client):
    with client:
        res = client.delete("/job_seeker/1")
        assert res.status_code == const.RESPONSE_OK
        js = session().get(JobSeeker, 1)
        assert js.is_delete

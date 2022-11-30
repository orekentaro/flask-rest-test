from tests.routes.base_test import BaseTest


class TestJobSeekerModule(BaseTest):
    def test_get_成功(self, client):
        with client:
            res = client.get("/job_seeker/")
            assert res.status_code == 200

            j = res.json
            data_list = j.get("data", [])
            assert type(data_list) == list

            data = data_list[0]
            assert data.get("memo")
            ads = data.get("ads")
            assert ads
            assert ads.get("job_master")

    def test_get1_成功(self, client):
        with client:
            res = client.get("/job_seeker/1")
            assert res.status_code == 200

            j = res.json
            data = j.get("data", [])
            assert type(data) == dict
            assert data.get("progress_info")
            assert data.get("memo")
            ads = data.get("ads")
            assert ads
            assert ads.get("job_master")

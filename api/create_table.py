import hashlib
from datetime import datetime as dt

from models.auth_master import AuthMaster
from models.base_model import ENGINE, BaseModel, session
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.job_seeker import JobSeeker
from models.memo import Memo
from models.progress_info import ProgressInfo
from models.progress_master import ProgressMaster
from models.progress_result import ProgressResult
from models.user_master import UserMaster


def create_table():
    BaseModel.metadata.create_all(bind=ENGINE)
    try:
        _create_data()
    except Exception as e:
        print(f"データ作成エラー→{e}")
        pass


def _create_data():
    with session() as db_session:
        auth = AuthMaster(id=1, auth="admin", changer="create")
        db_session.add(auth)

        user = UserMaster(
            name="テストくん",
            email="test@test.test",
            password=hashlib.sha256("password123".encode("utf-8")).hexdigest(),
            auth_id=1,
            changer="create",
        )
        db_session.add(user)

        entry = ProgressMaster(
            title="応募",
            changer="create",
        )
        db_session.add(entry)

        step1 = ProgressMaster(
            title="一次面接",
            changer="create",
        )
        db_session.add(step1)

        step2 = ProgressMaster(
            title="二次面接",
            changer="create",
        )
        db_session.add(step2)

        unofficial_decision = ProgressMaster(
            title="内定",
            changer="create",
        )
        db_session.add(unofficial_decision)

        acceptance = ProgressMaster(
            title="内定承諾",
            changer="create",
        )
        db_session.add(acceptance)

        joined = ProgressMaster(
            title="入社",
            changer="create",
        )
        db_session.add(joined)

        decline = ProgressMaster(
            title="辞退",
            changer="create",
        )
        db_session.add(decline)

        checking = ProgressResult(
            title="選考中",
            changer="create",
        )
        db_session.add(checking)

        adjustment = ProgressResult(
            title="日程調整中",
            changer="create",
        )
        db_session.add(adjustment)

        schedule = ProgressResult(
            title="予定",
            changer="create",
        )
        db_session.add(schedule)

        done = ProgressResult(
            title="実施",
            changer="create",
        )
        db_session.add(done)

        cancel = ProgressResult(
            title="キャンセル",
            changer="create",
        )
        db_session.add(cancel)

        passing = ProgressResult(
            title="通過",
            changer="create",
        )
        db_session.add(passing)

        failure = ProgressResult(
            title="不合格",
            changer="create",
        )
        db_session.add(failure)

        job_master = JobMaster(
            id=1,
            job_offer_name="テスト求人",
            subscription_cost=100000,
            changer="create",
        )
        db_session.add(job_master)

        db_session.commit()

        job_ads = JobAds(
            id=1,
            job_master_id=1,
            publication_start="20220401",
            publication_end="20220901",
            title="未経験可",
            contents="エンジニア募集中",
            views=200,
            cost=200,
            changer="create",
        )
        db_session.add(job_ads)

        db_session.commit()

        job_seeker = JobSeeker(
            id=1,
            name="テスト太郎",
            gender="m",
            birthday="19930218",
            career="2021年テスト株式会社入社",
            ads_id=1,
            changer="create",
        )
        db_session.add(job_seeker)

        progress_info = ProgressInfo(
            id=1,
            user_id=1,
            job_id=1,
            progress_info="応募がありました",
            schedule=dt.now(),
            result="1",
            changer="create",
        )
        db_session.add(progress_info)

        progress_info = ProgressInfo(
            id=2,
            user_id=1,
            job_id=1,
            progress_info="",
            result=2,
            changer="create",
        )
        db_session.add(progress_info)

        memo = Memo(
            job_id=1,
            memo="ちゃんと勉強してそう",
            changer=1,
        )
        db_session.add(memo)
        db_session.commit()


if __name__ == "__main__":
    create_table()

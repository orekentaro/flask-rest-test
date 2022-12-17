import hashlib
from datetime import datetime as dt

from models.auth_master import AuthMaster
from models.base_model import BaseModel
from models.create_session import get_engine, session
from models.job_ads import JobAds
from models.job_master import JobMaster
from models.job_seeker import JobSeeker
from models.memo import Memo
from models.progress_info import ProgressInfo
from models.progress_master import ProgressMaster
from models.progress_result import ProgressResult
from models.user_master import UserMaster


def create_table():
    BaseModel.metadata.create_all(bind=get_engine())
    try:
        _create_data()
    except Exception as e:
        print(f"データ作成エラー→{e}")
        pass


def _create_data():
    with session() as db_session:
        auth = AuthMaster(auth="admin", changer=1)
        db_session.add(auth)

        user = UserMaster(
            name="テストくん",
            email="test@test.test",
            password=hashlib.sha256("password123".encode("utf-8")).hexdigest(),
            auth_id=1,
            changer=1,
        )
        db_session.add(user)

        entry = ProgressMaster(
            title="応募",
            changer=1,
        )
        db_session.add(entry)

        step1 = ProgressMaster(
            title="一次面接",
            changer=1,
        )
        db_session.add(step1)

        step2 = ProgressMaster(
            title="二次面接",
            changer=1,
        )
        db_session.add(step2)

        unofficial_decision = ProgressMaster(
            title="内定",
            changer=1,
        )
        db_session.add(unofficial_decision)

        acceptance = ProgressMaster(
            title="内定承諾",
            changer=1,
        )
        db_session.add(acceptance)

        joined = ProgressMaster(
            title="入社",
            changer=1,
        )
        db_session.add(joined)

        decline = ProgressMaster(
            title="辞退",
            changer=1,
        )
        db_session.add(decline)

        checking = ProgressResult(
            title="選考中",
            changer=1,
        )
        db_session.add(checking)

        adjustment = ProgressResult(
            title="日程調整中",
            changer=1,
        )
        db_session.add(adjustment)

        schedule = ProgressResult(
            title="予定",
            changer=1,
        )
        db_session.add(schedule)

        done = ProgressResult(
            title="実施",
            changer=1,
        )
        db_session.add(done)

        cancel = ProgressResult(
            title="キャンセル",
            changer=1,
        )
        db_session.add(cancel)

        passing = ProgressResult(
            title="通過",
            changer=1,
        )
        db_session.add(passing)

        failure = ProgressResult(
            title="不合格",
            changer=1,
        )
        db_session.add(failure)

        job_master = JobMaster(
            job_offer_name="テスト求人",
            subscription_cost=100000,
            changer=1,
        )
        db_session.add(job_master)

        db_session.commit()

        job_ads = JobAds(
            job_master_id=1,
            publication_start="2022-04-01",
            publication_end="2022-09-01",
            title="未経験可",
            contents="エンジニア募集中",
            views=200,
            cost=200,
            changer=1,
        )
        db_session.add(job_ads)

        db_session.commit()

        job_seeker = JobSeeker(
            name="テスト太郎",
            gender="m",
            birthday="1993-02-18",
            career="2021年テスト株式会社入社",
            ads_id=1,
            changer=1,
        )
        db_session.add(job_seeker)

        progress_info = ProgressInfo(
            user_id=1,
            job_seeker_id=1,
            progress_master_id=1,
            progress_info="応募がありました",
            schedule=dt.now(),
            result="1",
            changer=1,
        )
        db_session.add(progress_info)

        progress_info = ProgressInfo(
            user_id=1,
            job_seeker_id=1,
            progress_info="",
            progress_master_id=2,
            result=2,
            changer=1,
        )
        db_session.add(progress_info)

        memo = Memo(
            job_seeker_id=1,
            memo="ちゃんと勉強してそう",
            changer=1,
        )
        db_session.add(memo)
        db_session.commit()


if __name__ == "__main__":
    create_table()

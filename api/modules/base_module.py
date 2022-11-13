import hashlib
from contextlib import contextmanager

from models.base_model import session
from models.user_master import UserMaster


class BaseModule:
    @contextmanager
    def session_scope() -> object:
        db_session = session()
        try:
            yield db_session
            db_session.commit()
        except Exception:
            db_session.rollback()
            raise
        finally:
            db_session.close()

    @classmethod
    def password_hash(cls, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @classmethod
    def get_user(cls, **user_info: dict) -> object:
        with cls.session_scope() as db_session:
            user = (
                db_session.query(UserMaster)
                .filter_by(**user_info, delete_flag="0")
                .one_or_none()
            )
            if user:
                user = user.__dict__
        return user

    @classmethod
    def date_to_string(cls, date: object) -> str:
        try:
            return_date = date.strftime("%Y/%m/%d")
        except Exception:
            return_date = None
        return return_date

    class Constant:
        DELETE_FLAG_OFF = "0"
        DELETE_FLAG_ON = "1"
        GENDER_DICT = {"m": "男性", "f": "女性"}

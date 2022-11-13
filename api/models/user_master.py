import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import BigInteger, Boolean, Column, Integer, String


class UserMaster(BaseModel):
    """ユーザーテーブル"""

    __tablename__ = "user_master"
    user_id = Column("user_id", Integer, nullable=False, primary_key=True)
    name = Column("name", String(200), nullable=False)
    email = Column("email", String(256), nullable=False, unique=True)
    password = Column("password", String(100), nullable=False)
    is_locked = Column("is_locked", Boolean, default=False, nullable=False)
    miss_count = Column("miss_count", BigInteger, server_default="0", nullable=False)
    is_init = Column("init_flag", Boolean, default=False, nullable=False)
    auth_id = Column("auth_id", String(200), nullable=False)


def create_user(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_user(sys.argv)

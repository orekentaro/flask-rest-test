from sqlalchemy import BigInteger, Boolean, Column, Integer, String

from models.base_model import BaseModel


class UserMaster(BaseModel):
    """ユーザーテーブル"""

    __tablename__ = "user_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    name = Column("name", String(200), nullable=False)
    email = Column("email", String(256), nullable=False, unique=True)
    password = Column("password", String(100), nullable=False)
    is_locked = Column("is_locked", Boolean, default=False, nullable=False)
    miss_count = Column("miss_count", BigInteger, server_default="0", nullable=False)
    is_init = Column("init_flag", Boolean, default=False, nullable=False)
    auth_id = Column("auth_id", Integer, nullable=False)

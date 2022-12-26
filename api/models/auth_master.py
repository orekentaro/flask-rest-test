from sqlalchemy import Column, Integer, String

from models.base_model import BaseModel


class AuthMaster(BaseModel):
    """権限マスタ"""

    __tablename__ = "auth_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    auth = Column("auth", String(200), nullable=False)

import sys

from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String


class AuthMaster(BaseModel):
    """権限マスタ"""

    __tablename__ = "auth_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    auth = Column("auth", String(200), nullable=False)

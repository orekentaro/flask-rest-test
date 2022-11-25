import sys
from typing import Any

from models.base_model import ENGINE, BaseModel, session
from sqlalchemy import Column, Integer, String


class AuthMaster(BaseModel):
    """権限マスタ"""

    __tablename__ = "auth_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    auth = Column("auth", String(200), nullable=False)


def get_auth(id: int) -> dict[str, Any]:
    return session().get(AuthMaster, id).__dict__


def create_auth(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_auth(sys.argv)

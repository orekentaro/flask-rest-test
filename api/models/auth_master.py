import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import Column, String


class AuthMaster(BaseModel):
    """権限マスタ"""

    __tablename__ = "auth_master"
    id = Column("id", String(200), nullable=False, primary_key=True)
    auth = Column("auth", String(200), nullable=False)


def create_auth(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_auth(sys.argv)

import sys

from sqlalchemy import Column, Integer, String

from models.base_model import ENGINE, BaseModel


class AuthMaster(BaseModel):
    """権限マスタ"""

    __tablename__ = "auth_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    auth = Column("auth", String(200), nullable=False)


def create_auth(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_auth(sys.argv)

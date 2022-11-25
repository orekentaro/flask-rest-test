import sys
from typing import Any

from models.base_model import ENGINE, BaseModel, session
from sqlalchemy import Column, Integer, Text


class ProgressMaster(BaseModel):
    """進捗マスタ"""

    __tablename__ = "progress_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    title = Column("title", Text, nullable=False)


def get_progress_master(id: int) -> dict[str, Any]:
    data = session().get(ProgressMaster, id).__dict__
    data.pop("_sa_instance_state")
    return data


def create_progress_master(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_master(sys.argv)

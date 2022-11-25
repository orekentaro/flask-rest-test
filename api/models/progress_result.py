import sys
from typing import Any

from models.base_model import ENGINE, BaseModel, session
from sqlalchemy import Column, Integer, Text


class ProgressResult(BaseModel):
    """進捗結果マスタ"""

    __tablename__ = "progress_result"
    id = Column("id", Integer, nullable=False, primary_key=True)
    title = Column("title", Text, nullable=False)


def get_progress_result(id: int) -> dict[str, Any]:
    return session().get(ProgressResult, id)


def create_progress_result(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_result(sys.argv)

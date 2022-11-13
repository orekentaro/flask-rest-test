import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import Column, Integer, Text


class ProgressResult(BaseModel):
    """進捗結果マスタ"""

    __tablename__ = "progress_result"
    progress_result_id = Column(
        "progress_result_id", Integer, nullable=False, primary_key=True
    )
    title = Column("title", Text, nullable=False)


def create_progress_result(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_result(sys.argv)

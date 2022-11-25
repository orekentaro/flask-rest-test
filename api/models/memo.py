import sys
from typing import Any

from models.base_model import ENGINE, BaseModel, session
from sqlalchemy import Column, ForeignKey, Integer, Text


class Memo(BaseModel):
    """求職者情報"""

    __tablename__ = "memo"
    id = Column("id", Integer, nullable=False, primary_key=True)
    job_id = Column(
        "job_id",
        Integer,
        ForeignKey("job_seeker.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    memo = Column("memo", Text, nullable=False)


def get_memo(id: int) -> dict[str, Any]:
    return session().get(Memo, id)


def create_memo(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_memo(sys.argv)

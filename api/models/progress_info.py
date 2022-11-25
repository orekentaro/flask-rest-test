import sys
from typing import Any

from models.base_model import ENGINE, BaseModel, session
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text


class ProgressInfo(BaseModel):
    """進捗情報"""

    __tablename__ = "progress_info"
    id = Column("id", Integer, nullable=False, primary_key=True)
    progress_id = Column(
        "progress_id",
        Integer,
        ForeignKey("progress_master.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    user_id = Column(
        "user_id",
        Integer,
        ForeignKey("user_master.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    job_id = Column(
        "job_id",
        Integer,
        ForeignKey("job_seeker.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    progress_info = Column("progress_info", Text, nullable=False)
    schedule = Column("schedule", DateTime)
    result = Column(
        "result",
        Integer,
        ForeignKey("progress_result.id", onupdate="CASCADE", ondelete="CASCADE"),
    )


def get_progress_info(id: int) -> dict[str, Any]:
    return session().get(ProgressInfo, id)


def create_progress_info(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_info(sys.argv)

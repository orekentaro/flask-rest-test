import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text


class ProgressInfo(BaseModel):
    """進捗情報"""

    __tablename__ = "progress_info"
    progress_info_id = Column(
        "progress_info_id", Integer, nullable=False, primary_key=True
    )
    progress_id = Column(
        "progress_id",
        Integer,
        ForeignKey(
            "progress_master.progress_id", onupdate="CASCADE", ondelete="CASCADE"
        ),
    )
    user_id = Column(
        "user_id",
        Integer,
        ForeignKey("user_master.user_id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    job_id = Column(
        "job_id",
        Integer,
        ForeignKey("job_seeker.job_id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    progress_info = Column("progress_info", Text, nullable=False)
    schedule = Column("schedule", DateTime)
    result = Column(
        "result",
        Integer,
        ForeignKey(
            "progress_result.progress_result_id", onupdate="CASCADE", ondelete="CASCADE"
        ),
    )


def create_progress_info(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_info(sys.argv)

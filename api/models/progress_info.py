import sys

from models.base_model import BaseModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text


class ProgressInfo(BaseModel):
    """進捗情報"""

    __tablename__ = "progress_info"
    id = Column("id", Integer, nullable=False, primary_key=True)
    progress_master_id = Column(
        "progress_master_id",
        Integer,
        ForeignKey("progress_master.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    user_id = Column(
        "user_id",
        Integer,
        ForeignKey("user_master.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    job_seeker_id = Column(
        "job_seeker_id",
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

import sys

from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, Text


class Memo(BaseModel):
    """求職者情報"""

    __tablename__ = "memo"
    id = Column("id", Integer, nullable=False, primary_key=True)
    job_seeker_id = Column(
        "job_seeker_id",
        Integer,
        ForeignKey("job_seeker.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    memo = Column("memo", Text, nullable=False)

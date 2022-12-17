from models.base_model import BaseModel
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Text


class JobAds(BaseModel):
    """求人広告"""

    __tablename__ = "job_ads"
    id = Column("id", Integer, nullable=False, primary_key=True)
    job_master_id = Column(
        "job_master_id",
        Integer,
        ForeignKey("job_master.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    publication_start = Column("publication_start", String(10))
    publication_end = Column("publication_end", String(10))
    title = Column("title", Text)
    contents = Column("contents", Text)
    views = Column("views", BigInteger)
    cost = Column("cost", BigInteger)

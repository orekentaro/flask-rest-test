import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, Text


class JobAds(BaseModel):
    """求人広告"""

    __tablename__ = "job_ads"
    ads_id = Column("ads_id", Integer, nullable=False, primary_key=True)
    job_master_id = Column(
        "job_master_id",
        Integer,
        ForeignKey("job_master.job_master_id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    publication_start = Column("publication_start", String(10))
    publication_end = Column("publication_end", String(10))
    title = Column("title", Text)
    contents = Column("contents", Text)
    views = Column("views", BigInteger)
    cost = Column("cost", BigInteger)


def create_job_ads(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_job_ads(sys.argv)

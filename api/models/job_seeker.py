import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text


class JobSeeker(BaseModel):
    """求職者情報"""

    __tablename__ = "job_seeker"
    id = Column("id", Integer, nullable=False, primary_key=True)
    name = Column("name", String(200), nullable=False)
    gender = Column("gender", String(1))
    birthday = Column("birthday", String(10))
    career = Column("career", Text)
    ads_id = Column(
        "ads_id",
        Integer,
        ForeignKey("job_ads.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    is_active = Column("is_active", Boolean, default=True, nullable=False)


def create_job_seeker(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_job_seeker(sys.argv)

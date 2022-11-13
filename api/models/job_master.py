import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import BigInteger, Column, Integer, String


class JobMaster(BaseModel):
    """求人マスタ"""

    __tablename__ = "job_master"
    job_master_id = Column("job_master_id", Integer, nullable=False, primary_key=True)
    job_offer_name = Column("job_offer_name", String(200), nullable=False)
    subscription_cost = Column("subscription_cost", BigInteger)


def create_job_master(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_job_master(sys.argv)

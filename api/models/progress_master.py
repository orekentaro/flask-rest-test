from models.base_model import BaseModel
from sqlalchemy import Column, Integer, Text


class ProgressMaster(BaseModel):
    """進捗マスタ"""

    __tablename__ = "progress_master"
    id = Column("id", Integer, nullable=False, primary_key=True)
    title = Column("title", Text, nullable=False)

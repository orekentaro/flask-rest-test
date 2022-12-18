from sqlalchemy import Column, Integer, Text

from models.base_model import BaseModel


class ProgressResult(BaseModel):
    """進捗結果マスタ"""

    __tablename__ = "progress_result"
    id = Column("id", Integer, nullable=False, primary_key=True)
    title = Column("title", Text, nullable=False)

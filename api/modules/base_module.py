from models.base_model import BaseModel, session
from sqlalchemy import select


class BaseModule:

    model: BaseModel = ""

    def all(self, *args, **kwargs):
        with session() as db_session:
            stm = select(self.model).filter_by(**kwargs)
            print(db_session.execute(stm).scalars().all())

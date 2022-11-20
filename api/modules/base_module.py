from typing import Optional, TypeAlias

from models.base_model import BaseModel, session
from serializer.base_serializer import BaseSerializer
from sqlalchemy import select


class BaseModule:

    model: Optional[BaseModel] = None
    serializer: TypeAlias = Optional[BaseSerializer]

    def all(self, *args, **kwargs):
        with session() as db_session:
            stmt = select(self.model).filter_by(**kwargs)
            return db_session.execute(stmt).scalars().all()

    def one_or_none(self, *args, **kwargs):
        with session() as db_session:
            stmt = select(self.model).filter_by(**kwargs)
            return db_session.execute(stmt).scalars().one_or_none()

    def first(self, *args, **kwargs):
        with session() as db_session:
            stmt = select(self.model).filter_by(**kwargs)
            return db_session.execute(stmt).scalars().first()

    def save(self, *args, **kwargs):
        with session() as db_session, db_session.begin():
            stmt = self.serializer.save(self.model, **kwargs)
            db_session.execute(stmt)

    def update(self, fillter, *args, **kwargs):
        with session() as db_session, db_session.begin():
            stmt = self.serializer.update(self.model, fillter, **kwargs)
            db_session.execute(stmt)

    def delete(self, fillter):
        with session() as db_session, db_session.begin():
            stmt = self.serializer.update(self.model, fillter)
            db_session.execute(stmt)

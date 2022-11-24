from typing import Any, Optional, TypeAlias

from models.base_model import BaseModel, session
from serializer.base_serializer import BaseSerializer
from sqlalchemy import delete, insert, select, update


class BaseModule:

    model: TypeAlias = BaseModel
    serializer: TypeAlias = BaseSerializer
    data: Optional[model] = None

    def all(self, *args, **kwargs) -> Optional[model]:
        with session() as db_session:
            stmt = select(self.model).filter_by(**kwargs)
            self.data = db_session.execute(stmt).scalars().all()
            return self.data

    def one_or_none(self, *args, **kwargs) -> Optional[model]:
        with session() as db_session:
            stmt = select(self.model).filter_by(**kwargs)
            self.data = db_session.execute(stmt).scalars().one_or_none()
            return self.data

    def first(self, *args, **kwargs) -> Optional[model]:
        with session() as db_session:
            stmt = select(self.model).filter_by(**kwargs)
            self.data = db_session.execute(stmt).scalars().first()
            return self.data

    def save(self, *args, **kwargs) -> None:
        with session() as db_session, db_session.begin():
            stmt = insert(self.model).values(**kwargs)
            db_session.execute(stmt)

    def path(self, fillter: dict[str, Any], *args, **kwargs) -> None:
        with session() as db_session, db_session.begin():
            stmt = update(self.model).values(**kwargs).filter_by(fillter)
            db_session.execute(stmt)

    def destroy(self, fillter: dict[str, Any]) -> None:
        with session() as db_session, db_session.begin():
            stmt = delete(self.model).filter_by(fillter)
            db_session.execute(stmt)

    def serialize(self) -> dict[str, Any]:
        return {"data": self.serializer.serialize(self.data)}

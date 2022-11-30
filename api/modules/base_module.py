from typing import Any, Optional, TypeAlias

import utils.constans as const
from flask import Response, json, request
from models.base_model import BaseModel, session
from serializer.base_serializer import BaseSerializer
from sqlalchemy import delete, insert, select, update


class BaseModule:

    model: TypeAlias = BaseModel
    serializer: TypeAlias = BaseSerializer
    data: Optional[model] = None

    def get(self, id: Optional[int] = None) -> Response:
        condition = dict(request.args)
        if id is not None:
            condition.update({"id": str(id)})
            self.one_or_none(**condition)
            if self.data is None:
                raise Exception("データが存在しません。")
        else:
            self.all(**condition)
        res = self.serialize()
        return Response(status=const.RESPONSE_OK, response=json.dumps(res))

    def post(self):
        r = request.json
        self.save(**r)
        return Response(status=const.RESPONSE_OK, response=json.dumps(r))

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

    def patch(self, fillter: dict[str, Any], *args, **kwargs) -> None:
        with session() as db_session, db_session.begin():
            stmt = update(self.model).values(**kwargs).filter_by(fillter)
            db_session.execute(stmt)

    def destroy(self, fillter: dict[str, Any]) -> None:
        with session() as db_session, db_session.begin():
            stmt = delete(self.model).filter_by(fillter)
            db_session.execute(stmt)

    def serialize(self) -> dict[str, Any]:
        return {"data": self.serializer().data(self.data)}

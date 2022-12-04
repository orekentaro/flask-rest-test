from typing import Any, Optional, TypeAlias, Union

from flask import Response, json, request
from sqlalchemy import insert, select, update

import utils.constans as const
from models.base_model import BaseModel, session
from serializer.base_serializer import BaseSerializer


class BaseModule:

    model: TypeAlias = BaseModel
    serializer: TypeAlias = BaseSerializer
    data: Optional[model] = None

    def get(self, id: Optional[int] = None, all_data: bool = False) -> Response:
        condition: dict[str, Union[str, bool]] = dict(request.args)
        if not all_data:
            condition.update({"is_delete": False})
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
        self.serializer().is_valid(**r)
        self.save(**r)
        return Response(status=const.RESPONSE_OK)

    def patch(self, id: int):
        if id is None:
            return Response(status=const.RESPONSE_BAD_REQUEST)

        r = request.json
        if r is None:
            return Response(status=const.RESPONSE_BAD_REQUEST)

        self.serializer().is_valid(to_update=True, **r)
        self.update({"id": id}, **r)
        return Response(status=const.RESPONSE_OK)

    def delete(self, id: int):
        if id is None:
            return Response(status=const.RESPONSE_BAD_REQUEST)

        self.destroy({"id": id})
        return Response(status=const.RESPONSE_OK)

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

    def update(self, fillter: dict[str, Any], *args, **kwargs) -> None:
        with session() as db_session, db_session.begin():
            stmt = update(self.model).values(**kwargs).filter_by(**fillter)
            db_session.execute(stmt)

    def destroy(self, fillter: dict[str, Any]) -> None:
        with session() as db_session, db_session.begin():
            stmt = update(self.model).values(is_delete=True).filter_by(**fillter)
            db_session.execute(stmt)

    def serialize(self) -> dict[str, Any]:
        return {"data": self.serializer().data(self.data)}

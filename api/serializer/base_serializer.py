from models.base_model import BaseModel
from sqlalchemy import delete as dl
from sqlalchemy import insert
from sqlalchemy import update as ud


class BaseSerializer:
    @classmethod
    def save(cls, model: BaseModel, *args, **values):
        stmt = insert(model).values(**values)
        return stmt

    @classmethod
    def update(
        cls,
        model: BaseModel,
        fillter,
        **values,
    ):
        stmt = ud(model).values(**values).filter_by(fillter)
        return stmt

    @classmethod
    def delete(
        cls,
        model: BaseModel,
        fillter,
    ):
        stmt = dl(model).filter_by(fillter)
        return stmt

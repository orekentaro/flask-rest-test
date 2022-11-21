from typing import Union

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

    @classmethod
    def serialize(clas, model: Union[BaseModel, list[BaseModel]]):
        if type(model) != list:
            raw_data = model.__dict__
            raw_data.pop("_sa_instance_state")
            return raw_data

        raw_data_list = []
        for data in BaseModel:
            rd: dict = data.__dict__
            rd.pop("_sa_instance_state")
            raw_data_list.append(rd)
        return raw_data_list

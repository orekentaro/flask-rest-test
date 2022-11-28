from typing import Any

from models.base_model import BaseModel, session
from sqlalchemy import select


def get_one(model: BaseModel, id) -> dict[str, Any]:
    return model_to_dict(session().get(model, id))


def get_relation(model: BaseModel, *args, **kwargs) -> list[dict[str, Any]]:
    with session() as db_session:
        stmt = select(model).filter_by(**kwargs)
        datas = db_session.execute(stmt).scalars().all()
        return [model_to_dict(data) for data in datas]


def model_to_dict(data: BaseModel) -> dict[str, Any]:
    data = data.__dict__
    data.pop("_sa_instance_state")
    return data

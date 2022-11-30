from typing import Any, Optional, Union

from models.base_model import BaseModel, session
from sqlalchemy import select


class BaseSerializer:
    def data(
        self, model: Optional[Union[BaseModel, list[BaseModel]]]
    ) -> Union[dict[str, Any], list[dict[str, Any]]]:
        if type(model) != list:
            raw_data = self._model_to_dict(model)
            return raw_data

        raw_data_list = []
        for data in model:
            rd = self._model_to_dict(data)
            raw_data_list.append(rd)
        return raw_data_list

    def _get_one(
        self, model: BaseModel, id: int, to_model: bool = False
    ) -> dict[str, Any]:
        if to_model:
            return session().get(model, id)
        return self._model_to_dict(session().get(model, id))

    def _get_relation(
        self,
        model: BaseModel,
        to_model: bool = False,
        is_delete: bool = False,
        *args,
        **kwargs
    ) -> Union[list[dict[str, Any]], list[BaseModel]]:
        with session() as db_session:
            stmt = select(model).filter_by(is_delete=is_delete, **kwargs)
            datas = db_session.execute(stmt).scalars().all()
            if to_model:
                return [data for data in datas]
            return [self._model_to_dict(data) for data in datas]

    def _model_to_dict(self, data: BaseModel) -> dict[str, Any]:
        data = data.__dict__
        data.pop("_sa_instance_state")
        return data

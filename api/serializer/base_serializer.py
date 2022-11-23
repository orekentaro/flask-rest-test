from typing import Any, Union

from models.base_model import BaseModel


class BaseSerializer:
    @classmethod
    def serialize(
        clas, model: Union[BaseModel, list[BaseModel]]
    ) -> Union[dict[str, Any], list[dict[str, Any]]]:
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

from typing import Any, Union

from models.progress_info import ProgressInfo
from models.progress_master import ProgressMaster
from models.progress_result import ProgressResult
from models.user_master import UserMaster
from serializer.base_serializer import BaseSerializer


class ProgressInfoSerializer(BaseSerializer):
    def data(self, progress_info: Union[ProgressInfo, list[ProgressInfo]]) -> Union[dict[str, Any], list]:  # type: ignore[override]
        if type(progress_info) == list:
            return_list = []
            for pi in progress_info:
                progress_info_data = self._make_data(pi)
                return_list.append(progress_info_data)
            return return_list
        else:
            return self._make_data(progress_info)  # type: ignore[arg-type]

    def _make_data(self, progress_info: ProgressInfo) -> dict[str, Any]:
        pi = self._model_to_dict(progress_info)
        pi["result"] = self._get_one(ProgressResult, pi["result"])
        pi["progress"] = self._get_one(ProgressMaster, pi["progress_master_id"])[
            "title"
        ]
        pi["interviewer"] = self._get_one(UserMaster, pi["user_id"])["name"]
        del pi["job_seeker_id"]
        del pi["progress_master_id"]
        del pi["user_id"]
        return pi

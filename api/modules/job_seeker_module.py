from typing import Optional

import utils.constans as const
from flask import Response, json, request
from models.job_seeker import JobSeeker
from modules.base_module import BaseModule
from serializer.job_seeker_serializer import JobSeekerSerializer


class JobSeekerModule(BaseModule):
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    model = JobSeeker
    serializer = JobSeekerSerializer

    def get(self, id: Optional[int] = None) -> Response:
        condition = dict(request.args)
        if type(id) == int:
            condition.update({"id": str(id)})

        self.all(**condition)
        res = self.serialize()
        return Response(status=const.RESPONSE_OK, response=json.dumps(res))

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

    def get(self, job_id: Optional[int] = None) -> Response:
        try:
            condition = dict(request.args)
            if type(job_id) == int:
                condition.update({"job_id": str(job_id)})

            self.all(**condition)
            res = self.serialize()
            return Response(status=const.RESPONSE_OK, response=json.dumps(res))
        except Exception as e:
            return Response(
                status=const.RESPONSE_ERROR,
                response=json.dumps({"msg": f"予期せぬエラーが発生しました:[{e}]"}),
            )

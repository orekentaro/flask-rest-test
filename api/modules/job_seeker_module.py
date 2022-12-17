from models.job_seeker import JobSeeker
from modules.base_module import BaseModule
from serializer.job_seeker_serializer import JobSeekerSerializer


class JobSeekerModule(BaseModule):
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    model = JobSeeker
    serializer = JobSeekerSerializer

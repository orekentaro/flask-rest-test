from models.base_model import session
from models.user_master import UserMaster
from modules.base_module import BaseModule
from sqlalchemy import select


class UserModule(BaseModule):
    """
    ユーザー認証やログイン、権限、ユーザー管理用のモジュールクラス
    """

    model = UserMaster

    def login(self, email, password):
        """
        ログイン認証API
        """
        self.all()

from typing import Any

from models.auth_master import AuthMaster
from models.base_model import session
from models.user_master import UserMaster
from serializer.base_serializer import BaseSerializer


class AuthSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, user: UserMaster) -> dict[str, Any]:  # type: ignore[override]
        auth: AuthMaster = session().get(AuthMaster, user.auth_id)
        user_data = user.__dict__
        user_data.update(auth_name=auth.auth)
        return user_data

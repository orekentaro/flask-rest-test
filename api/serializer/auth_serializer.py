from typing import Any, Optional

from models.auth_master import get_auth
from models.user_master import UserMaster
from serializer.base_serializer import BaseSerializer


class AuthSerializer(BaseSerializer):
    @classmethod
    def serialize(cls, user: Optional[UserMaster]) -> dict[str, Any]:  # type: ignore[override]
        if user is None:
            return {}
        auth = get_auth(user.auth_id)
        user_data = user.__dict__
        user_data.pop("_sa_instance_state")
        user_data.update(auth_name=auth.get("auth", ""))
        return user_data

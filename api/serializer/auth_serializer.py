from typing import Any, Optional

from models.auth_master import AuthMaster
from models.user_master import UserMaster
from serializer.base_serializer import BaseSerializer


class AuthSerializer(BaseSerializer):
    def data(self, user: Optional[UserMaster]) -> dict[str, Any]:  # type: ignore[override]
        if user is None:
            return {}
        auth = self._get_one(AuthMaster, user.auth_id)
        user_data = user.__dict__
        user_data.pop("_sa_instance_state")
        user_data.update(auth_name=auth.get("auth", ""))
        return user_data

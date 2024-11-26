from typing import Union, Any, Optional

from app.base.service import BaseService
from app.models.user import User

UserOrItsID = Union[int, User]

class UserService(BaseService):
    async def get_user(self, user_id: int) -> Optional[User]:
        """
        Get user by id
        """

    async def update_user(self, user: UserOrItsID, new_data: dict[str, Any]) -> User:
        """
        Update user with new data
        """

    async def delete_user(self, user: UserOrItsID) -> None:
        pass

    async def create_user(self, data: dict[str, Any]) -> User:
        pass

from app.base.service import BaseService
from app.repositories.user import UserRepository


class UserService(BaseService):
    __repository_class__ = UserRepository

    async def get_user(self, user_id):
        async with self.get_repo(UserRepository) as user_repo:
            user = await user_repo.get_user(user_id)
            return user

    async def update_user(self, user, new_data):
        pass

    async def delete_user(self, user):
        pass

    async def create_user(self, data):
        pass

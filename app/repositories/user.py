from sqlalchemy import select

from app.base.repository import BaseRepository
from app.models import User


class UserRepository(BaseRepository):
    async def get_user(self, user_id):
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        return result.scalar()

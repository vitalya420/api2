from typing import Optional

from app.base.repository import BaseRepository
from app.models import User

class UserRepository(BaseRepository):
    async def get_user(self, user_id: int) -> Optional[User]:
        pass

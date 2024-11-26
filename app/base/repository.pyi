# repository.pyi

from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository:
    """
    A base repository class for managing database operations.

    This class serves as a foundation for repository classes that interact
    with the database, typically using SQLAlchemy's `AsyncSession` for asynchronous
    database operations. It provides common functionality for executing database
    queries and managing the lifecycle of a database session.

    Args:
        running_session (AsyncSession): An instance of `AsyncSession` that will
                                         be used for executing database operations.
    """

    def __init__(self, running_session: AsyncSession) -> None:
        """
        Initialize the BaseRepository with a database session.

        Args:
            running_session (AsyncSession): An instance of AsyncSession that will be
                                    used for executing database operations.
        """
        self.session: AsyncSession

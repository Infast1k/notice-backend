"""Base MongoDB repository abstraction with basic attrs and methods"""

__author__ = 'infast1k'


from abc import ABC

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection


class BaseMongoDBRepository(ABC):
    """Base MongoDB repository"""

    def __init__(self, client: AsyncIOMotorClient, db_name: str, collection_name: str) -> None:
        """Initialize mongo db repository"""
        self._client: AsyncIOMotorClient = client
        self._db_name: str = db_name
        self._collection_name: str = collection_name

    @property
    def _collection(self) -> AsyncIOMotorCollection:
        """Get collection for data"""
        return self._client[self._db_name][self._collection_name]

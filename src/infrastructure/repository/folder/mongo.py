"""Репозиторий для папок, работающий на основе MongoDB"""

__author__ = 'infast1k'

from typing import override

from domain.folder.entity import Folder

from domain.folder.repository import BaseFolderRepository

from infrastructure.repository.base.mongo import BaseMongoDBRepository


class MongoDBFolderRepository(BaseMongoDBRepository, BaseFolderRepository):
    """Folder repository abstraction"""

    @override
    async def folder_already_exists(self, folder: Folder) -> bool:
        """Check if folder already exists"""
        return bool(
            await self._collection.find_one(
                filter={
                    'title': folder.title,
                }
            )
        )

    @override
    async def create_folder(self, folder: Folder) -> None:
        """Add new folder to storage"""
        await self._collection.insert_one(document=self._convert_entity_to_document(folder))

    @staticmethod
    def _convert_entity_to_document(folder: Folder) -> dict:
        """Convert folder entity to dict"""
        return {
            'oid': str(folder.oid),
            'title': folder.title,
            'parentId': str(folder.parent_oid) if folder.parent_oid else None,
            'createdAt': folder.created_at,
            'updatedAt': folder.updated_at,
        }

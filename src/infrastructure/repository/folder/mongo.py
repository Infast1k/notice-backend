"""Репозиторий для папок, работающий на основе MongoDB"""

__author__ = 'infast1k'

from typing import override
from uuid import UUID

from domain.folder.entity import Folder

from domain.folder.repository import BaseFolderRepository

from infrastructure.repository.base.mongo import BaseMongoDBRepository


class MongoDBFolderRepository(BaseMongoDBRepository, BaseFolderRepository):
    """Реализация репозитория для работы с папками"""

    @override
    async def get_folder_by_id(self, folder_id: UUID) -> Folder | None:
        """Получить папку по её идентификатору"""
        return await self._collection.find_one(filter={
            'oid': str(folder_id),
        })

    @override
    async def is_unique_folder(self, folder: Folder) -> bool:
        """Проверить папку на уникальность"""
        existing_folder = await self._collection.find_one(filter={
            'title': folder.title,
            'parent_oid': str(folder.parent_oid) if folder.parent_oid else None,
        })

        return bool(existing_folder)

    @override
    async def create_folder(self, folder: Folder) -> None:
        """Создать новую папку"""
        await self._collection.insert_one(document=self._convert_entity_to_document(folder))

    @staticmethod
    def _convert_entity_to_document(folder: Folder) -> dict:
        """Преобразовать сущность в документ"""
        return {
            'oid': str(folder.oid),
            'title': folder.title,
            'parentId': str(folder.parent_oid) if folder.parent_oid else None,
            'createdAt': folder.created_at,
            'updatedAt': folder.updated_at,
        }

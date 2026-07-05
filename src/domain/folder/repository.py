"""Репозиторий для работы с папками"""

__author__ = 'infast1k'


from abc import ABC, abstractmethod
from uuid import UUID

from domain.folder.entity import Folder


class BaseFolderRepository(ABC):
    """Описание репозитория для работы с папками"""

    @abstractmethod
    async def is_unique_folder(self, folder: Folder) -> bool:
        """Проверить папку на уникальность"""
        raise NotImplementedError

    @abstractmethod
    async def get_folder_by_id(self, folder_id: UUID) -> Folder | None:
        """Получить модель папки по её идентификатору"""
        raise NotImplementedError

    @abstractmethod
    async def create_folder(self, folder: Folder) -> None:
        """Создать новую папку по переданной модели"""
        raise NotImplementedError

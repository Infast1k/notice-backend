"""Репозиторий для работы с папками"""

__author__ = 'infast1k'


from abc import ABC, abstractmethod

from domain.folder.entity import Folder


class BaseFolderRepository(ABC):
    """Описание репозитория для работы с папками"""

    @abstractmethod
    async def folder_already_exists(self, folder: Folder) -> bool:
        """Проверить, существует ли уже такая папка"""
        raise NotImplementedError

    @abstractmethod
    async def create_folder(self, folder: Folder) -> None:
        """Создать новую папку по переданной модели"""
        raise NotImplementedError

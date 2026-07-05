"""Обработка создания папки"""

__author__ = 'infast1k'


from dataclasses import dataclass
from typing import override
from uuid import UUID

from application.base.command import BaseCommand, BaseCommandHandler
from application.command.folder.exception import FolderAlreadyExistsException, FolderDoesNotExistsException

from domain.folder.entity import Folder
from domain.folder.repository import BaseFolderRepository
from domain.folder.value_object import Title


@dataclass(frozen=True, eq=False)
class CreateFolderCommand(BaseCommand):
    """Команда создания новой папки"""

    title: str
    """Название папки"""
    parent_oid: UUID | None
    """Идентификатор родительской папки"""


class CreateFolderCommandHandler(BaseCommandHandler[CreateFolderCommand, Folder]):
    """Обработчик создания новой папки"""

    def __init__(self, folder_repository: BaseFolderRepository) -> None:
        """Инициализация"""
        self._folder_repository: BaseFolderRepository = folder_repository

    @override
    async def execute(self, command: CreateFolderCommand) -> Folder:
        """Обработать полученную команду"""
        title = Title(command.title)
        folder = Folder(title=title, parent_oid=command.parent_oid)

        if command.parent_oid:
            parent_folder = await self._folder_repository.get_folder_by_id(command.parent_oid)
            if not parent_folder:
                raise FolderDoesNotExistsException(folder)

        is_unique_folder = await self._folder_repository.is_unique_folder(folder)
        if not is_unique_folder:
            raise FolderAlreadyExistsException(folder)

        await self._folder_repository.create_folder(folder)

        return folder

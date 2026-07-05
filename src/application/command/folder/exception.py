"""Исключения при работе с БП правил"""

__author__ = 'infast1k'


from dataclasses import dataclass
from typing import override

from application.base.exception import ApplicationException

from domain.folder.entity import Folder


@dataclass(frozen=True, eq=False)
class FolderDoesNotExistsException(ApplicationException):
    """Исключение, возникающее при отсутвии папки"""

    folder: Folder

    @property
    @override
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'Папки с идентификатором {self.folder.oid} не существует'


@dataclass(frozen=True, eq=False)
class FolderAlreadyExistsException(ApplicationException):
    """Исключение, возникающее при попытке создать папку, которая уже существует"""

    folder: Folder

    @property
    @override
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'Папка с названием "{self.folder.title}" на данном уровне вложенности уже существует'

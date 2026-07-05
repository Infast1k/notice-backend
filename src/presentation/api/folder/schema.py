"""Схемы данных для работы с хендлерами"""

__author__ = 'infast1k'


from typing import Self
from uuid import UUID

from pydantic import BaseModel

from domain.folder.entity import Folder


class CreateFolderRequestSchema(BaseModel):
    """Модель входных данных для создания новой папки"""

    title: str
    """Название папки"""
    parent_oid: UUID | None
    """Идентификатор родительской папки"""


class CreateFolderResponseSchema(BaseModel):
    """Модель выходных данных при создании новой папки"""

    oid: UUID
    """Идентификатор созданной папки"""
    title: str
    """Название созданной папки"""
    parent_oid: UUID | None
    """Идентификатор родительской папки"""

    @classmethod
    def from_entity(cls, folder: Folder) -> Self:
        """Преобразовать сущность в модель ответа"""
        return cls(
            oid=folder.oid,
            title=folder.title,
            parent_oid=folder.parent_oid,
        )

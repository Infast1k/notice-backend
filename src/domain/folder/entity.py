"""Сущность папки"""

__author__ = 'infast1k'


from datetime import datetime
from uuid import UUID

from domain.base.entity import BaseEntity
from domain.folder.value_object import Title


class Folder(BaseEntity):
    """Реализация сущности папки"""

    def __init__(
        self,
        *,
        title: Title,
        parent_oid: UUID | None = None,
        oid: UUID | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        """Инициализация"""
        self._title: Title = title
        self._parent_oid: UUID | None = parent_oid
        super().__init__(oid=oid, created_at=created_at, updated_at=updated_at)

    @property
    def title(self) -> str:
        """Получить название папки"""
        return self._title.value

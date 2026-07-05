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
    def oid(self) -> UUID:
        """Получить идентификатор папки"""
        return self._oid

    @property
    def title(self) -> str:
        """Получить название папки"""
        return self._title.value

    @property
    def parent_oid(self) -> UUID | None:
        """Получить идентификатор родительской папки (если есть)"""
        return self._parent_oid

    @property
    def created_at(self) -> datetime:
        """Получить дату и время создания папки"""
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        """Получить дату и время последнего обновления папки"""
        return self._updated_at

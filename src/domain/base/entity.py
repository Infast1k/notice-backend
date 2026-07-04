"""Базовая сущность"""

__author__ = 'infast1k'


from abc import ABC
from datetime import datetime
from uuid import UUID, uuid4


class BaseEntity(ABC):
    """Реализация базовой сущности"""

    def __init__(
        self,
        *,
        oid: UUID | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        """
        Инициализация

        :param oid: уникальный идентификатор сущности
        :param created_at: дата и время создания сущности
        :param updated_at: дата и время обновления сущности
        """
        self._oid: UUID = oid or uuid4()
        self._created_at: datetime = created_at or datetime.now()
        self._updated_at: datetime = updated_at or datetime.now()

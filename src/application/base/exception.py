"""Базовое исключение уровня БЛ"""

__author__ = 'infast1k'


from dataclasses import dataclass
from typing import override

from domain.base.exception import DomainException


@dataclass(frozen=True, eq=False)
class ApplicationException(DomainException):
    """Реализация базового исключения уроня БЛ"""

    @property
    @override
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'Произошла ошибка бизнес-логики'

"""Исключения для папок"""

__author__ = 'infast1k'


from dataclasses import dataclass
from typing import override

from domain.base.exception import DomainException


@dataclass(frozen=True, eq=False)
class EmptyFolderTitleException(DomainException):
    """Ошибка, возникающая при попытке создать объект названия папки с пустым значением"""

    @property
    @override
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'Название папки не может быть пустым'


@dataclass(frozen=True, eq=False)
class TooLongFolderTitleException(DomainException):
    """Ошибка, возникающая при попытке создать объект названия папки со слишком длинным кол-вом символов"""

    max_length: int

    @property
    @override
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'Длина названия папки не может превышать {self.max_length} символов'

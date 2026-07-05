"""Реализация объектов-значений для папок"""

__author__ = 'infast1k'


from dataclasses import dataclass
from typing import Final, override

from domain.base.value_object import BaseValueObject
from domain.folder.exception import EmptyFolderTitleException, TooLongFolderTitleException


_MAX_TITLE_LENGTH: Final[int] = 220
"""Максимальная длина названия папки"""


@dataclass(frozen=True, slots=True)
class Title(BaseValueObject[str]):
    """Реализаця объекта-значения для хранения названия папки"""

    @override
    def _validate(self) -> None:
        """Валидация названия папки"""
        if not self.value:
            raise EmptyFolderTitleException

        if len(self.value) > _MAX_TITLE_LENGTH:
            raise TooLongFolderTitleException(_MAX_TITLE_LENGTH)

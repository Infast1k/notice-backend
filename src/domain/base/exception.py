"""Реализация базовых исключений для доменного уровня"""

__author__ = 'infast1k'


from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class DomainException(Exception):
    """Реализация базового исключения доменного уровня"""

    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return 'Произошла ошибка доменного уровня'

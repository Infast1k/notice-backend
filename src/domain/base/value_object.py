"""Абстракция объекта-значения"""

__author__ = 'infast1k'


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BaseValueObject[T](ABC):
    """Реализация базового объекта-значения"""

    value: T
    """Значение объекта"""

    def __post_init__(self) -> None:
        """Метод, вызывающийся после инициализации объекта"""
        self._validate()

    @abstractmethod
    def _validate(self) -> None:
        """
        Валидация значения (вызывается в методе `post_init` после инициализации)
        Необходимо реализовать в каждом дочернем элементе
        """
        raise NotImplementedError

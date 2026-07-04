"""Абстракции для реализации команд и их обработчиков"""

__author__ = 'infast1k'


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class BaseCommand:
    """Базовая команда"""


class BaseCommandHandler[CT, CR](ABC):
    """Базовый обработчик команды"""

    @abstractmethod
    async def execute(self, command: CT) -> CR:
        """Обработать команду"""
        raise NotImplementedError

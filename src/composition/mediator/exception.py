"""Исключения при работе с медиаторами"""

__author__ = 'infast1k'


from dataclasses import dataclass

from application.base.command import BaseCommand
from application.base.exception import ApplicationException


@dataclass(frozen=True, eq=False)
class CommandHandlerNotRegisteredException(ApplicationException):
    """Исключение, возникающее при попытке обработать команду, на которую не был зарегистрирован обработчик"""

    command_type: type[BaseCommand]

    @property
    def message(self) -> str:
        """Сообщение об ошибке"""
        return f'Для указанной команды не указан обработчик: "{self.command_type}"'

"""Абстракция медиатора для работы с командами и их обработчиками"""

__author__ = 'infast1k'


from typing import Any

from application.base.command import BaseCommand, BaseCommandHandler

from composition.mediator.exception import CommandHandlerNotRegisteredException


class CommandMediator:
    """Абстракция медиатора для работы с командами и их обработчиками"""

    def __init__(self) -> None:
        """Инициализация"""
        self._command_handler_map: dict[type[BaseCommand], BaseCommandHandler] = {}

    def register_command(self, command: type[BaseCommand], handler: BaseCommandHandler) -> None:
        """Регистрация команды и её обработчика"""
        self._command_handler_map[command] = handler

    async def handle_command(self, command: BaseCommand) -> Any:
        """Обработать полученную команду"""
        command_type = command.__class__

        command_handler = self._command_handler_map[command_type]
        if not command_handler:
            raise CommandHandlerNotRegisteredException(command_type)

        return await command_handler.execute(command)

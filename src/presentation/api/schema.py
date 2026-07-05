"""Базовые схемы для работы с хендлерами"""

__author__ = 'infast1k'

from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """Базовая схема для ответа с ошибкой"""

    error: str
    """Сообщение об ошибке"""

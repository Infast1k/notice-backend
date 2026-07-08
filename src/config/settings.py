"""Конфигурация приложения"""

__author__ = 'infast1k'


from pydantic import Field

from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSettings(BaseSettings):
    """Класс конфигурации приложения"""

    model_config = SettingsConfigDict(env_file='../.env', env_file_encoding='utf-8', extra='ignore')

    # Настройки для работы с MongoDB
    mongo_username: str = Field(alias='MONGO_USERNAME')
    mongo_password: str = Field(alias='MONGO_PASSWORD')
    mongo_host: str = Field(alias='MONGO_HOST')
    mongo_port: int = Field(alias='MONGO_PORT')

    # Настройки для работы с mongo express
    mongo_express_host: str = Field(alias='MONGO_EXPRESS_HOST')
    mongo_express_port: int = Field(alias='MONGO_EXPRESS_PORT')

    # Настройка коллекций для хранения данных
    mongo_folder_db_name: str = Field(alias='MONGO_FOLDER_DB_NAME')
    mongo_folder_collection: str = Field(alias='MONGO_FOLDER_COLLECTION')

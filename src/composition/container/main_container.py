"""Реализация основного контейнера зависимостей"""

__author__ = 'infast1k'


from functools import cache

from motor.motor_asyncio import AsyncIOMotorClient

from punq import Container, Scope

from application.command.folder.create_folder import CreateFolderCommand, CreateFolderCommandHandler

from composition.mediator.main_mediator import Mediator

from config.settings import ApplicationSettings

from domain.folder.repository import BaseFolderRepository

from infrastructure.repository.folder.mongo import MongoDBFolderRepository


@cache
def init_container() -> Container:
    """Инициализировать основной контейнера приложения"""
    container = Container()
    container.register(ApplicationSettings, instance=ApplicationSettings(), scope=Scope.singleton)

    def create_mongodb_client() -> AsyncIOMotorClient:
        print('init_folder_mongodb_repository before')
        config: ApplicationSettings = container.resolve(ApplicationSettings)
        print('init_folder_mongodb_repository after')
        return AsyncIOMotorClient(
            (
                f'mongodb://{config.mongo_username}:{config.mongo_password}'
                f'@{config.mongo_host}:{config.mongo_port}/?authSource=admin'
            ),
            serverSelectionTimeoutMS=3000,
        )

    container.register(AsyncIOMotorClient, factory=create_mongodb_client, scope=Scope.singleton)
    mongo_db_client = container.resolve(AsyncIOMotorClient)

    def init_folder_mongodb_repository() -> BaseFolderRepository:
        print('init_folder_mongodb_repository before')
        config: ApplicationSettings = container.resolve(ApplicationSettings)
        print('init_folder_mongodb_repository after')
        return MongoDBFolderRepository(
            client=mongo_db_client,
            db_name=config.mongo_folder_db_name,
            collection_name=config.mongo_folder_collection,
        )

    container.register(BaseFolderRepository, factory=init_folder_mongodb_repository, scope=Scope.singleton)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        create_folder_command_handler = CreateFolderCommandHandler(
            folder_repository=container.resolve(BaseFolderRepository),
        )

        mediator.register_command(CreateFolderCommand, create_folder_command_handler)

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container

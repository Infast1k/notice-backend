"""Хендлеры работы с папками"""

__author__ = 'infast1k'

from domain.base.exception import DomainException
from fastapi import (
    Depends,
    status,
)
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from punq import Container

from application.command.folder.create_folder import CreateFolderCommand

from composition.container.main_container import init_container
from composition.mediator.main_mediator import Mediator

from presentation.api.folder.schema import CreateFolderRequestSchema, CreateFolderResponseSchema
from presentation.api.schema import ErrorSchema


router = APIRouter(tags=['Folder'])


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    description='Создание новой папки',
    responses={
        status.HTTP_201_CREATED: {'model': CreateFolderResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def create_folder_handler(
    schema: CreateFolderRequestSchema,
    container: Container = Depends(init_container),
) -> CreateFolderResponseSchema:
    """Создать новую папку"""
    mediator: Mediator = container.resolve(Mediator)

    try:
        folder = await mediator.handle_command(CreateFolderCommand(title=schema.title, parent_oid=schema.parent_oid))
    except DomainException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})

    return CreateFolderResponseSchema.from_entity(folder)

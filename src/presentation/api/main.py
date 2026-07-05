"""Основная точка входа в приложение"""

__author__ = 'infast1k'


from fastapi import FastAPI

from presentation.api.folder.handler import router as folder_handler


def create_app() -> FastAPI:
    """Инициализация приложения"""
    app = FastAPI(
        title='Notice',
        docs_url='/api/docs',
        description='Markdown notes taking application',
        debug=True,
    )

    app.include_router(folder_handler, prefix='/folders')

    return app

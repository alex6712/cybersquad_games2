from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import get_settings
from app.api.routers import (
    auth_router,
    games_router,
    root_router,
    users_router,
)

settings = get_settings()

tags_metadata = [
    {
        "name": "root",
        "description": "Получение информации о **приложении**.",
    },
    {
        "name": "authorization",
        "description": "Операции **регистрации** и **аутентификации**.",
    },
    {
        "name": "users",
        "description": "Операции с **пользователями**. _Получение информации_ о них.",
    },
    {
        "name": "games",
        "description": "Операции с **комнатами игр**: _создание_, _удаление_, _получение информации_.",
    },
    {
        "name": "blackjack",
        "description": "API для работы с потоком игры **блек-джек**.",
    },
]

cybersquad_games = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    summary=settings.APP_SUMMARY,
    contact={
        "name": settings.ADMIN_NAME,
        "email": settings.ADMIN_EMAIL,
    },
    openapi_tags=tags_metadata,
)

cybersquad_games.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cybersquad_games.include_router(auth_router)
cybersquad_games.include_router(games_router)
cybersquad_games.include_router(root_router)
cybersquad_games.include_router(users_router)

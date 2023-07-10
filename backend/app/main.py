from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import get_settings
from app.routers import (
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
        "description": "Операции с **пользователями**. Получение _информации_ о них.",
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

origins = [
    "http://localhost:3000",
]

cybersquad_games.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cybersquad_games.include_router(auth_router)
cybersquad_games.include_router(games_router)
cybersquad_games.include_router(root_router)
cybersquad_games.include_router(users_router)

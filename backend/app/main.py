from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import get_settings
from app.routers import (
    auth_router,
    games_router,
    root_router,
    users_router,
)

origins = [
    "http://localhost:3000",
]

settings = get_settings()

cybersquad_games = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    contact={
        "name": settings.ADMIN_NAME,
        "email": settings.ADMIN_EMAIL,
    },
)

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

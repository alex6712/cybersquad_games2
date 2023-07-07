from fastapi import FastAPI

from app import get_settings
from app.routers import (
    authorization_router,
    root_router,
    users_router,
)

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
cybersquad_games.include_router(authorization_router)
cybersquad_games.include_router(root_router)
cybersquad_games.include_router(users_router)

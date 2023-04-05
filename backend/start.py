import uvicorn

from app import settings

if __name__ == "__main__":
    uvicorn.run(
        app="app.main:cybersquad_games",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEV_MODE,
    )

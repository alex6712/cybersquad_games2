import uvicorn

from app import settings

if __name__ == "__main__":
    uvicorn.run(
        app="app.main:app",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=True,
    )

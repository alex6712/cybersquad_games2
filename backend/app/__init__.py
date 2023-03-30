"""
Factory CRM

Source directory серверной части приложения.

Здесь присутствуют файлы API серверной части приложения.

Используются инструменты:
    FastAPI
    SQLAlchemy
    asyncio
    uvicorn
    asyncpg

Алексей Ванюков
vanyukov.alex@gmail.com
"""

__author__ = "Алексей Ванюков"

from .settings import settings

__version__ = settings.APP_VERSION

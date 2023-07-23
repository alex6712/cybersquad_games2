"""CYBERSQUAD Games

Source directory серверной части приложения.

Используются инструменты:
    FastAPI
    SQLAlchemy
    asyncio
    uvicorn
    asyncpg

Приложение создано командой CYBERSQUAD Games.
Лицензия отсутствует.
Приятной игры!
"""

__author__ = "Алексей Ванюков"

from config import get_settings

__version__ = get_settings().APP_VERSION

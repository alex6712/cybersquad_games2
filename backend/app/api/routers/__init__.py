"""
CYBERSQUAD Games API routers

Модуль с описанием роутеров API.

Алексей Ванюков
vanyukov.alex@gmail.com
"""

__author__ = "Алексей Ванюков"

from .auth import router as auth_router
from .games import router as games_router
from .root import router as root_router
from .users import router as users_router

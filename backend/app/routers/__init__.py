"""
Factory CRM API routers

Модуль с описанием роутеров API.

Алексей Ванюков
vanyukov.alex@gmail.com
"""

from .authorization import router as authorization_router
from .root import router as root_router
from .users import router as users_router

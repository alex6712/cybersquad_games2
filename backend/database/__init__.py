"""
Database Factory CRM

Модуль для работы с базой данных.

Здесь описаны модели используемой БД и интерфейсы взаимодействия с ними.

Используется фреймворк SQLAlchemy.

Алексей Ванюков
vanyukov.alex@gmail.com
"""

__author__ = "Алексей Ванюков"

from .session import (
    get_session,
    AsyncSessionMaker,
)

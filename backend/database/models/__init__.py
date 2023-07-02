"""
Database Factory CRM Models

Модуль с описаниями моделей базы данных.

Алексей Ванюков
vanyukov.alex@gmail.com
"""

__author__ = "Алексей Ванюков"

from .base import BaseModel as DBBaseModel
from .base import JoinBaseModel as DBJoinBaseModel
from .user import User as DBUserModel

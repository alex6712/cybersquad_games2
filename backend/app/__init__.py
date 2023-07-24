"""CYBERSQUAD Games

Source directory серверной части приложения.

Используются инструменты:
    * `FastAPI`_
    * `SQLAlchemy`_
    * `uvicorn`_
    * `asyncpg`_

Приложение создано командой CYBERSQUAD Games для игр на компанию по
локальной сети.
Приложение устанавливается на устройство, способное запустить Python,
React и PostgreSQL, после чего запускается доступный по локальной сети
frontend, а данное приложение, являющееся backend'ом, запускается
на localhost, не позволяя подключиться к нему извне.

.. _`FastAPI`:
    https://fastapi.tiangolo.com/
.. _`SQLAlchemy`:
    https://www.sqlalchemy.org
.. _`uvicorn`:
    https://www.uvicorn.org
.. _`asyncpg`:
    https://magicstack.github.io/asyncpg/current/
"""

from .config import get_settings

settings = get_settings()

__title__ = settings.APP_NAME
__summary__ = settings.APP_SUMMARY

__version__ = settings.APP_VERSION

__author__ = settings.ADMIN_NAME
__email__ = settings.ADMIN_EMAIL

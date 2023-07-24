"""CYBERSQUAD Games API routers

Пакет с описанием роутеров API.

В этом пакете собраны реализации роутеров API, содержащие набор
методов (``endpoints``) серверной части приложения.
Каждый из роутеров импортируется в корневой путь пакета, что позволяет
далее импортировать их без явного указания модуля.

Роутеры импортируются с заменой идентификатора, чтобы не происходило конфликтов,
т.к. для удобства [1]_ в отдельных модулях каждый роутер называется ``router``.

.. [1] Для единообразия кода и простоты чтения.
"""

from .auth import router as auth_router
from .games import router as games_router
from .root import router as root_router
from .users import router as users_router

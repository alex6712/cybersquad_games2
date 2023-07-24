"""API CYBERSQUAD Games Schemas

Пакет с описаниями схем объектов тела запросов.

Здесь содержатся описания схем объектов, необходимых для передачи
данных внутри приложения и приведения различных объектов к определённой
структуре.

Например, для приведения записи пользователя из базы данных, в которой будет
запись о пароле, к схеме без пароля.
Для создания схем используется ``pydantic`` (документация которого
может быть найдена `здесь`_).

.. _`здесь`:
    https://docs.pydantic.dev/
"""

from .user import (
    UserSchema,
    UserWithPasswordSchema,
)
from .room import (
    RoomSchema,
    RoomWithPasswordSchema,
    RoomCredentialsSchema,
)

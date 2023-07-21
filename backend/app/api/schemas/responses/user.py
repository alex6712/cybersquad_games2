from api.schemas import UserSchema
from api.schemas.responses import StandardResponse


class UserResponse(StandardResponse, UserSchema):
    """
    Модель ответа с данными о пользователе.

    Используется в качестве ответа от сервера на запрос о пользователе.
    """
    pass

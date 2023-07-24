from app.api.schemas import UserSchema
from .standard import StandardResponse


class UserResponse(StandardResponse, UserSchema):
    """Модель ответа с данными о пользователе.

    Используется в качестве ответа от сервера на запрос о пользователе.

    See also
    --------
    schemas.responses.standard.StandardResponse
    schemas.user.UserSchema
    """
    pass

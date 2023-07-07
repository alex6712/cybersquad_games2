from app.models import APIUserModel
from app.models.responses import StandardResponse


class UserResponse(StandardResponse, APIUserModel):
    """
    Модель ответа с данными о пользователе.

    Используется в качестве ответа от сервера на запрос о пользователе.
    """
    pass

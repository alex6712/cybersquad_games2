from pydantic import Field

from app.models.responses import StandardResponse


class TokenResponse(StandardResponse):
    """
    Модель ответа с вложенным JWT.

    Используется в качестве ответа от сервера на запрос об авторизации.

    .. seealso::

        :ref:`BaseModel` - базовая модель pydantic :class:`pydantic.BaseModel`.

    Attributes
    ----------
    access_token: str
        JSON Web Token
    token_type: str
        тип возвращаемого токена
    """
    access_token: str = Field(example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                                      ".eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
                                      ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    refresh_token: str = Field(example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                                       ".eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"
                                       ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    token_type: str = Field(example="bearer")

from fastapi import status
from pydantic import BaseModel, Field


class StandardResponse(BaseModel):
    """Модель стандартного ответа от сервера.

    Используется в качестве базовой модели ответа на любой запрос этого приложения.

    Это означает, что любой ответ от сервера будет содержать код ответа ``code``
    и сообщение от сервера ``message`` в теле ответа.

    See also
    --------
    pydantic.BaseModel

    Attributes
    ----------
    code : int
        Статусный код ответа от сервера.
    message : str
        Сообщение от сервера.
    """
    code: int = Field(default=status.HTTP_200_OK, example=status.HTTP_200_OK)
    message: str = Field(default="Success!", example="Success!")

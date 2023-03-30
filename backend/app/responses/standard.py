from fastapi import status
from pydantic import BaseModel, Field


class StandardResponse(BaseModel):
    """
    Модель стандартного ответа от сервера.

    Используется в качестве базовой модели ответа на любой запрос этого приложения.

    Это означает, что любой ответ от сервера будет содержать код ответа (:attr:`code`)
    и сообщение от сервера (:attr:`message`) в теле ответа.

    .. seealso::

        :ref:`BaseModel` - базовая модель pydantic :class:`pydantic.BaseModel`.

    Attributes
    ----------
    code: int
        статусный код ответа от сервера
    message: str
        сообщение от сервера
    """
    code: int = Field(default=status.HTTP_200_OK, example=status.HTTP_200_OK)
    message: str = Field(default="Success!", example="Success!")

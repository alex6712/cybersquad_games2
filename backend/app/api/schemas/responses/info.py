from pydantic import Field, EmailStr

from .standard import StandardResponse


class AppInfoResponse(StandardResponse):
    """Модель ответа на запрос информации о приложении.

    Для получения справки о наследуемых атрибутах см. ``StandardResponse``.

    See Also
    --------
    .standard.StandardResponse

    Attributes
    ----------
    app_name : str
        Наименование приложения.
    app_version : str
        Текущая версия приложения.
    app_description : str
        Полное описание приложения.
    app_summary : str
        Краткое описание приложения.
    admin_name : str
        ФИО ответственного.
    admin_email : str
        Адрес электронной почты для связи с ответственным.
    """
    app_name: str = Field(example="Fast API")
    app_version: str = Field(example="0.0.0")
    app_description: str = Field(example="RESTful API с использованием FastAPI Python 3.10")
    app_summary: str = Field(example="Лучшее веб-приложение.")
    admin_name: str = Field(example="Иванов Иван Иванович")
    admin_email: EmailStr = Field(example="ivanov.ivan@mail.ru")

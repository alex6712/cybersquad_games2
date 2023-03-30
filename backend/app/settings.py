from pydantic import (
    BaseSettings,
    EmailStr,
    IPvAnyAddress,
    PostgresDsn,
)


class Settings(BaseSettings):
    """
    Config класс проекта.

    Используется pydantic + python-dotenv для поиска настроек приложения, описанных в .env.

    .. seealso::

        :ref:`python-dotenv` - https://pypi.org/project/python-dotenv/

    Attributes
    ----------
    APP_NAME: str
        наименование приложения
    APP_VERSION: str
        текущая версия приложения
    APP_DESCRIPTION: str
        описание приложения
    ADMIN_NAME: str
        ФИО ответственного
    ADMIN_EMAIL: EmailStr
        адрес электронной почты для связи с ответственным
    DOMAIN: str | IPvAnyAddress
        IP домена, на котором расположено приложение
    BACKEND_PORT: int
        порт приложения
    DATABASE_USER: str
        пользователь базы данных для подключения
    DATABASE_PASSWORD: str
        пароль пользователя для подключения к базе данных
    DATABASE_PORT: int
        порт базы данных
    DATABASE_NAME: str
        имя базы данных
    DATABASE_URL: PostgresDsn
        строка подключения (ссылка) к базе данных
    """
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str

    ADMIN_NAME: str
    ADMIN_EMAIL: EmailStr

    DOMAIN: str | IPvAnyAddress

    BACKEND_PORT: int

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    DATABASE_URL: PostgresDsn

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

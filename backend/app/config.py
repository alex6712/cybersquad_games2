from functools import lru_cache
from typing import List

from pydantic import (
    EmailStr,
    IPvAnyAddress,
    AnyHttpUrl,
    field_validator,
)
from pydantic_settings import BaseSettings


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
    APP_SUMMARY: str
        краткое описание приложения
    ADMIN_NAME: str
        ФИО ответственного
    ADMIN_EMAIL: EmailStr
        адрес электронной почты для связи с ответственным
    DEV_MODE: bool
        режим разработки
    INITIALIZE_DB: bool
        пересоздать БД
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]
        список источников для CORS Middleware
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
    JWT_SECRET_KEY: str
        секретный ключ для кодирования JSON Web Token
    JWT_ALGORITHM: str
        алгоритм кодирования JWT
    ACCESS_TOKEN_LIFETIME_MINUTES: int
        срок жизни токена доступа в минутах
    REFRESH_TOKEN_LIFETIME_DAYS: int
        срок жизни токена обновления в днях
    """
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_SUMMARY: str

    ADMIN_NAME: str
    ADMIN_EMAIL: EmailStr

    DEV_MODE: bool

    INITIALIZE_DB: bool

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]

    @classmethod
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: List[str] | str) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]

        elif isinstance(v, (list, str)):
            return v

        raise ValueError(v)

    DOMAIN: str | IPvAnyAddress

    BACKEND_PORT: int

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_LIFETIME_MINUTES: int
    REFRESH_TOKEN_LIFETIME_DAYS: int

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()

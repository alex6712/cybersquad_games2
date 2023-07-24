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
    """Config класс проекта.

    Используется `pydantic`_ + `python-dotenv`_ для поиска настроек приложения, описанных в .env.

    .. _`pydantic`:
        https://docs.pydantic.dev/
    .. _`python-dotenv`:
        https://pypi.org/project/python-dotenv/

    See also
    --------
    pydantic
    python-dotenv

    Attributes
    ----------
    APP_NAME : str
        Наименование приложения.
    APP_VERSION : str
        Текущая версия приложения.
    APP_DESCRIPTION : str
        Полное описание приложения.
    APP_SUMMARY : str
        Краткое описание приложения.
    ADMIN_NAME : str
        ФИО ответственного.
    ADMIN_EMAIL : EmailStr
        Адрес электронной почты для связи с ответственным.
    DEV_MODE : bool
        Режим разработки.
    INITIALIZE_DB : bool
        Пересоздать БД.
    BACKEND_CORS_ORIGINS : List[AnyHttpUrl]
        Список источников для CORS Middleware.
    DOMAIN : str` | `IPvAnyAddress
        IP домена, на котором расположено приложение.
    BACKEND_PORT : int
        Порт приложения.
    DATABASE_USER : str
        Пользователь базы данных для подключения.
    DATABASE_PASSWORD : str
        Пароль пользователя для подключения к базе данных.
    DATABASE_PORT : int
        Порт базы данных.
    DATABASE_NAME : str
        Имя базы данных.
    DATABASE_URL : PostgresDsn
        Строка подключения (ссылка) к базе данных.
    JWT_SECRET_KEY : str
        Секретный ключ для кодирования JSON Web Token.
    JWT_ALGORITHM : str
        Алгоритм кодирования JWT.
    ACCESS_TOKEN_LIFETIME_MINUTES : int
        Срок жизни токена доступа в минутах.
    REFRESH_TOKEN_LIFETIME_DAYS : int
        Срок жизни токена обновления в днях.
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

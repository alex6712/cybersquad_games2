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
    APP_NAME: str = "CYBERSQUAD Games"
    APP_VERSION: str = "2.0.0"
    APP_DESCRIPTION: str = "API серверной части локальной игровой платформы от команды CYBERSQUAD."

    ADMIN_NAME: str = "Ванюков Алексей Игоревич"
    ADMIN_EMAIL: EmailStr = "vanyukov.alex@gmail.com"

    DOMAIN: str | IPvAnyAddress = "127.0.0.1"

    BACKEND_PORT: int = 8080

    DATABASE_USER: str = "root"
    DATABASE_PASSWORD: str = "toor"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "cybersquad_games"

    DATABASE_URL: PostgresDsn = f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DOMAIN}:" \
                                f"{DATABASE_PORT}/{DATABASE_NAME}"

    class Config:
        case_sensitive = True


settings = Settings()

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from app import get_settings

engine: AsyncEngine = create_async_engine(
    url=get_settings().DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)
AsyncSessionMaker: async_sessionmaker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """Создаёт объект асинхронной сесии уникального запроса.

    Используется для добавления сессии БД в маршрут запроса с помощью системы зависимостей FastAPI.

    Returns
    -------
    session : AsyncSession
        Объект асинхронной сессии для уникального запроса.
    """
    async with AsyncSessionMaker() as session:
        yield session

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from app import settings

engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)
AsyncSessionMaker: async_sessionmaker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """
    Создаёт объект асинхронной сесии уникального запроса.

    Используется для добавления сессии БД в маршрут запроса с помощью системы зависимостей FastAPI.

    :return: AsyncSession, объект асинхронной сессии для уникального запроса
    """
    async with AsyncSessionMaker() as session:
        yield session

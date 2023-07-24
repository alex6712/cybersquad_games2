from typing import AnyStr

from sqlalchemy import select
from sqlalchemy.engine.result import ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import RoomWithPasswordSchema
from app.database.models import RoomModel


async def get_room_by_id(session: AsyncSession, id_: int) -> RoomModel:
    """Возвращает модель записи игровой комнаты по идентификатору для дальнейшей работы.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    id_ : int
        Идентификатор игровой комнаты.

    Returns
    -------
    room : RoomModel
        Модель записи игровой комнаты в базе данных.
    """
    return await session.scalar(select(RoomModel).where(RoomModel.id == id_))


async def get_room_by_title(session: AsyncSession, title: AnyStr) -> ScalarResult[RoomModel]:
    """Возвращает модели записей игровых комнат по их названию для дальнейшей работы.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    title : AnyStr
        Название комнаты (комнат).

    Returns
    -------
    rooms : ScalarResult[RoomModel]
        Модели записей игровых комнат в базе данных.
    """
    return await session.scalars(select(RoomModel).where(RoomModel.title == title))


def add_room(session: AsyncSession, room: RoomWithPasswordSchema):
    """Добавляет новую запись об игровой комнате в базу данных.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    room : RoomWithPasswordSchema
        Схема объекта комнаты с паролем.
    """
    session.add(RoomModel(title=room.title, password=room.password, game_type=room.game_type))

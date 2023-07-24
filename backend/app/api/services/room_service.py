from typing import AnyStr

from sqlalchemy import select, delete
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


async def get_rooms_by_title(session: AsyncSession, title: AnyStr) -> ScalarResult[RoomModel]:
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


async def get_rooms_by_game_type(session: AsyncSession, game_type: AnyStr) -> ScalarResult[RoomModel]:
    """Возвращает модели записей игровых комнат по их названию для дальнейшей работы.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    game_type : AnyStr
        Тип игры в комнате (комнатах).

    Returns
    -------
    rooms : ScalarResult[RoomModel]
        Модели записей игровых комнат в базе данных.
    """
    return await session.scalars(select(RoomModel).where(RoomModel.game_type == game_type))


async def get_rooms_by_title_and_game_type(
        session: AsyncSession,
        title: AnyStr,
        game_type: list[AnyStr],
) -> ScalarResult[RoomModel]:
    """Возвращает модели записей игровых комнат по их названию для дальнейшей работы.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    title : AnyStr
        Название комнаты (комнат).
    game_type : AnyStr
        Тип игры в комнате (комнатах).

    Returns
    -------
    rooms : ScalarResult[RoomModel]
        Модели записей игровых комнат в базе данных.
    """
    where_clauses = []

    if title is not None:
        where_clauses.append(RoomModel.title == title)

    if game_type is not None:
        where_clauses.append(RoomModel.game_type.in_(game_type))

    return await session.scalars(select(RoomModel).where(*where_clauses))


async def delete_room_by_id(session: AsyncSession, id_: int):
    """Удаляет запись об игровой комнате по идентификатору.

    Parameters
    ----------
    session : AsyncSession
        Объект сессии запроса.
    id_ : int
        Идентификатор игровой комнаты, запись которой необходимо удалить.
    """
    await session.execute(delete(RoomModel).where(RoomModel.id == id_))


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

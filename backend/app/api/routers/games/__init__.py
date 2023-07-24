"""CYBERSQUAD Games API games routers

Пакет с описанием роутеров игр.

В данном файле описаны методы оперирования комнатами: их создание,
удаление, модификация, взаимодействие пользователя с комнатами.

Т.к. интерфейс взаимодействия комнаты и пользователя не зависит от типа комнаты,
реализация вынесена на уровень иерархии выше, чем сами игры.
"""

from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException,
    Query,
    Body,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.security import hash_, verify
from app.api.schemas import (
    UserSchema,
    RoomWithPasswordSchema,
    RoomCredentialsSchema,
)
from app.api.schemas.responses import (
    StandardResponse,
    RoomsResponse,
)
from app.api.services import room_service
from app.database.session import get_session
from .blackjack import router as _blackjack_router

router = APIRouter(
    prefix="/games",
)
router.include_router(_blackjack_router)


@router.post(
    "/room",
    response_model=StandardResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["games"],
    summary="Создаёт комнату.",
)
async def create_room(
        user: Annotated[UserSchema, Depends(validate_access_token)],
        room: Annotated[RoomWithPasswordSchema, Body(title="Данные для создания новой комнаты.")],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """Метод создания комнаты.

    Создаёт комнату для игры по сети.
    Комната может быть нескольких типов, в зависимости от типа игры, для которой она создаётся.
    Однако интерфейс взаимодействия пользователя и комнаты общий.

    Parameters
    ----------
    user : UserSchema
        Пользователь получен из зависимости на авторизацию.
    room : RoomWithPasswordSchema
        Информация о комнате, которая будет занесена в базу данных.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    response : StandardResponse
        Положительная обратная связь о создании комнаты.
    """
    room.password = hash_(room.password)

    room_service.add_room(session, room)

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough information in request.",
        )

    return {"code": status.HTTP_201_CREATED, "message": f"Room created by {user.username} successfully."}


@router.delete(
    "/room",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    tags=["games"],
    summary="Удаляет комнату.",
)
async def delete_room(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """Метод удаления комнаты.

    Проверяет возможность удаления комнаты, выполняет удаление каскада зависимостей.

    Parameters
    ----------
    user : UserSchema
        Пользователь получен из зависимости на авторизацию.

    Returns
    -------
    response : StandardResponse
        Положительная обратная связь об удалении комнаты.
    """
    return {"message": f"Room deleted by {user.username} successfully."}


@router.get(
    "/room",
    response_model=RoomsResponse,
    status_code=status.HTTP_200_OK,
    tags=["games"],
    summary="Возвращает список комнат."
)
async def get_room(query: Annotated[str | None, Query(title="параметры фильтрации выборки игровых комнат.")]):
    return {"message": "Hello, World!", "rooms": []}


@router.post(
    "/join",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    tags=["games"],
    summary="Привязывает пользователя к комнате.",
)
async def join_room(
        user: Annotated[UserSchema, Depends(validate_access_token)],
        room_credentials: Annotated[RoomCredentialsSchema, Body(title="Данные для присоединения к комнате.")],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """Метод присоединения пользователя к комнате.

    Привязывает пользователя к определённой комнате, что позволяет во время
    исполнения потока игры утверждать, что он в игре.

    Parameters
    ----------
    user : UserSchema
        Пользователь получен из зависимости на авторизацию.
    room_credentials : RoomCredentialsSchema
        Схема представления формы игровой комнаты для привязки пользователя.
    session : AsyncSession
        Объект сессии запроса.

    Returns
    -------
    response : StandardResponse
        Положительная обратная связь о присоединении пользователя.
    """
    room = await room_service.get_room_by_id(session, room_credentials.id)

    if not room:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_404_UNAUTHORIZED,
            detail=f"Cannot find room with id={room_credentials.id}",
        )

    if not verify(room_credentials.password, room.password):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password."
        )

    return {"message": f"User {user.username} successfully joined room."}

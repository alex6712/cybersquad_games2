"""CYBERSQUAD Games API games routers

Пакет с описанием роутеров игр.

В данном файле описаны методы оперирования комнатами: их создание,
удаление, модификация, взаимодействие пользователя с комнатами.

Т.к. интерфейс взаимодействия комнаты и пользователя не зависит от типа комнаты,
реализация вынесена на уровень иерархии выше, чем сами игры.
"""

__author__ = "Алексей Ванюков"

from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.api.dependencies import validate_access_token
from app.api.schemas import UserSchema
from app.api.schemas.responses import StandardResponse
from .blackjack import router as _blackjack_router

router = APIRouter(
    prefix="/games",
)
router.include_router(_blackjack_router)


@router.post("/room", status_code=status.HTTP_201_CREATED, response_model=StandardResponse, tags=["games"])
def create_room(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """Метод создания комнаты.

    Создаёт комнату для игры по сети.
    Комната может быть нескольких типов, в зависимости от типа игры, для которой она создаётся.
    Однако интерфейс взаимодействия пользователя и комнаты общий.

    Parameters
    ----------
    user : `UserSchema`
        Пользователь получен из зависимости на авторизацию

    Returns
    -------
    response : `StandardResponse`
        Положительная обратная связь о создании комнаты
    """
    return {"code": status.HTTP_201_CREATED, "message": f"Room created by {user.username} successfully."}


@router.delete("/room", status_code=status.HTTP_200_OK, response_model=StandardResponse, tags=["games"])
def delete_room(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """Метод удаления комнаты.

    Проверяет возможность удаления комнаты, выполняет удаление каскада зависимостей.

    Parameters
    ----------
    user : `UserSchema`
        Пользователь получен из зависимости на авторизацию

    Returns
    -------
    response : `StandardResponse`
        Положительная обратная связь об удалении комнаты
    """
    return {"message": f"Room deleted by {user.username} successfully."}


@router.post("/join", status_code=status.HTTP_200_OK, response_model=StandardResponse, tags=["games"])
def join_room(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """Метод присоединения пользователя к комнате.

    Привязывает пользователя к определённой комнате, что позволяет во время
    исполнения потока игры утверждать, что он в игре.

    Parameters
    ----------
    user : `UserSchema`
        Пользователь получен из зависимости на авторизацию

    Returns
    -------
    response : `StandardResponse`
        Положительная обратная связь о присоединении пользователя
    """
    return {"message": f"User {user.username} successfully joined room."}

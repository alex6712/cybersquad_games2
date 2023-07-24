from pydantic import BaseModel, Field


class RoomSchema(BaseModel):
    """Схема объекта комнаты.

    Используется в качестве представления информации о комнате.

    Attributes
    ----------
    id : int
        Идентификатор игровой комнаты.
    title : str
        Наименование комнаты.
    game_type : str
        Тип игры, которая воспроизводится в комнате.
    """
    id: int = Field(example=0)
    title: str = Field(default="Новая комната", example="Новая комната")
    game_type: str = Field(example="CG_BLACKJACK_GAME")

    class Config:
        frozen = True


class RoomWithPasswordSchema(BaseModel):
    """Схема объекта комнаты с паролем.

    Используется в качестве представления информации о комнате, включая пароль.

    Attributes
    ----------
    title : str
        Наименование комнаты.
    game_type : str
        Тип игры, которая воспроизводится в комнате.
    password : str
        Пароль игровой комнаты.
    """
    title: str = Field(default="Новая комната", example="Новая комната")
    game_type: str = Field(example="CG_BLACKJACK_GAME")
    password: str = Field(example="password")


class RoomCredentialsSchema(BaseModel):
    """Схема идентификационных данных игровой комнаты.

    Используется в качестве объекта представления формы для пользователя к комнате.

    Attributes
    ----------
    id : int
        Идентификатор игровой комнаты.
    password : str
        Пароль игровой комнаты.
    """
    id: int = Field(example=0)
    password: str = Field(example="password")

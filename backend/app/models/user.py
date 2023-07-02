from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """
    Модель объекта пользователя.

    Используется в качестве представления информации о пользователе.

    .. seealso::

        :ref:`BaseModel` - базовая модель pydantic :class:`pydantic.BaseModel`.

    Attributes
    ----------
    username: str
        логин пользователя
    email: EmailStr
        адрес электронной почты пользователя
    """
    username: str = Field(example="someone")
    email: EmailStr = Field(example="someone@post.domen")
    phone: str = Field(example="+7 900 000-00-00")


class UserWithPassword(User):
    """
    Модель объекта пользователя с паролем.

    Используется в качестве представления информации о пользователе, включая пароль.

    .. seealso::

        :ref:`User` - базовая модель pydantic :class:`app.models.User`.

    Attributes
    ----------
    password: str
        пароль пользователя
    """
    password: str = Field(example="password")

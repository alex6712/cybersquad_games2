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
    password: str
        пароль пользователя
    email: EmailStr
        адрес электронной почты пользователя
    """
    username: str = Field(example="someone")
    password: str = Field(example="password")
    email: EmailStr = Field(example="someone@post.domen")
    phone: str = Field(example="+7 900 000-00-00")

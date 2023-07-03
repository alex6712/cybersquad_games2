from pydantic import BaseModel, Field, EmailStr


class APIUserModel(BaseModel):
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


class APIUserWithPasswordModel(APIUserModel):
    """
    Модель объекта пользователя с паролем.

    Используется в качестве представления информации о пользователе, включая пароль.

    .. seealso::

        :ref:`APIUserModel` - модель объекта пользователя без пароля :class:`app.models.APIUserModel`.

    Attributes
    ----------
    password: str
        пароль пользователя
    """
    password: str = Field(example="password")

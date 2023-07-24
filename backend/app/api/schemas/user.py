from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Схема объекта пользователя.

    Используется в качестве представления информации о пользователе.

    Attributes
    ----------
    username : str
        Логин пользователя.
    email : EmailStr
        Адрес электронной почты пользователя.
    phone : str
        Номер мобильного телефона пользователя.
    """
    username: str = Field(example="someone")
    email: EmailStr = Field(default=None, example="someone@post.domen")
    phone: str = Field(default=None, example="+7 900 000-00-00")


class UserWithPasswordSchema(UserSchema):
    """Схема объекта пользователя с паролем.

    Используется в качестве представления информации о пользователе, включая пароль.

    Attributes
    ----------
    password : str
        Пароль пользователя.
    """
    password: str = Field(example="password")

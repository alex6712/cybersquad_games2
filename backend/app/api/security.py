from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_(secret: str | bytes, scheme: str = None, category: str = None, **kwargs) -> str:
    """Прокси для метода ``CriptContext.hash()``.

    Получает необходимые для выполнения хеширования параметры и возвращает результат.

    Parameters
    ----------
    secret : str or bytes
        Пароль, который подлежит хешированию.
    scheme : str or bytes, optional
        Схема, по которой будет производиться хеширование. Опциональный аргумент.
        Если не передана, что будет использоваться схема, заданная контексту.

        .. deprecated:: 1.7
            Поддержка этого ключевого слова устарела и будет удалена в Passlib 2.0.
    category : str, optional
        Если указана, то любые значения по умолчанию, относящиеся к категории,
        будут изменены на значения по умолчанию этой категории.

    Returns
    -------
    hashed : str or bytes
        Хешированный по установленным схеме и настройкам пароль.
    """
    return pwd_context.hash(secret, scheme, category, **kwargs)


def verify(secret: str | bytes, hashed: str | bytes, scheme: str = None, category: str = None, **kwargs) -> bool:
    """Прокси для метода ``CriptContext.verify()``.

    Проверяет переданный пароль на соответствие переданному хешу.

    Parameters
    ----------
    secret : str or bytes
        Проверяемый пароль.
    hashed : str or bytes
        Хешированный пароль.
    scheme : str or bytes, optional
        Схема, по которой будет производиться хеширование. Опциональный аргумент.
        Если не передана, что будет использоваться схема, заданная контексту.

        .. deprecated:: 1.7
            Поддержка этого ключевого слова устарела и будет удалена в Passlib 2.0.
    category : str, optional
        Если указана, то любые значения по умолчанию, относящиеся к категории,
        будут изменены на значения по умолчанию этой категории.

    Returns
    -------
    equality : bool
        ``True`` если хеш пароля совпадает с переданным, ``False`` в ином случае.
    """
    return pwd_context.verify(secret, hashed, scheme, category, **kwargs)

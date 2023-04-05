from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]) -> None:
    """
    Временный примерный материал для создания зависимости обработки JWT-токена.
    Если токен не совпадает, возвращается ошибка 400.

    :param x_token: Annotated[str, Header()], защитный токен
    """
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str) -> None:
    """
    Временный примерный материал для создания зависимости обработки JWT-токена.
    Если токен не совпадает, возвращается ошибка 400.

    :param token: str, защитный токен
    """
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
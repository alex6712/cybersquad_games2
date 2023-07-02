from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

SECRET_KEY = "79871f2dd656ab8e91a5f96142763f12aed8d6a4d6bc7cf9aaa9ebe597487323"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def jwt_encode(to_encode: dict):
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)


def jwt_decode(token: Annotated[str, Depends(oauth2_scheme)]):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def create_jwt(data: dict, expires_delta: timedelta = timedelta(minutes=5)):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})

    return jwt_encode(to_encode)

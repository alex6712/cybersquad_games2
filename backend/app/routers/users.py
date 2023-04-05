from typing import Annotated

from pydantic import EmailStr
from fastapi import APIRouter, Depends, Form

from app.dependencies import get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
)


@router.get("/me")
async def read_items():
    """
    """
    return


@router.post("/sign_up")
async def sign_up(login: Annotated[str, Form()], password: Annotated[str, Form()], email: Annotated[EmailStr, Form()]):
    """
    """
    return


@router.get("/sign_in")
async def sign_in(login: Annotated[str, Form()], password: Annotated[str, Form()]):
    """
    """
    return

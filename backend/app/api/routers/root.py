from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app import get_settings
from app.config import Settings
from app.api.schemas.responses import (
    StandardResponse,
    AppInfoResponse,
)

router = APIRouter(
    tags=["root"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=StandardResponse, tags=["root"])
async def root():
    """Корневой путь для проверки работоспособности API.

    Ничего не делает, кроме положительной обратной связи на запрос.

    Returns
    -------
    response : `StandardResponse`
        Ответ о корректной работе сервера
    """
    return {"message": "API works!"}


@router.get("/app_info", status_code=status.HTTP_200_OK, response_model=AppInfoResponse, tags=["root"])
async def app_info(settings: Annotated[Settings, Depends(get_settings)]):
    """Путь для получения информации о серверной части приложения.

    Получаемая информация:
        * app_name : `str`, имя приложения
        * app_version : `str`, версия приложения
        * app_description : `str`, полное описание приложения
        * app_summary : `str`, краткое описание приложения
        * admin_name : `str`, ФИО ответственного
        * admin_email : `str`, адрес электронной почты для связи с ответственным

    Parameters
    ----------
    settings : `Settings`
        Настройки приложения

    Returns
    -------
    response : `AppInfoResponse`
        Ответ, содержащий информацию о серверной части приложения
    """
    return {
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "app_description": settings.APP_DESCRIPTION,
        "app_summary": settings.APP_SUMMARY,
        "admin_name": settings.ADMIN_NAME,
        "admin_email": settings.ADMIN_EMAIL,
    }

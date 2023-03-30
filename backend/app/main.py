from fastapi import FastAPI, status

from app import settings
from app.responses import (
    StandardResponse,
    AppInfoResponse,
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    contact={
        "name": settings.ADMIN_NAME,
        "email": settings.ADMIN_EMAIL,
    },
)


@app.get("/", status_code=status.HTTP_200_OK, response_model=StandardResponse)
async def root():
    """
    Корневой путь для проверки работоспособности API.

    Ничего не делает, кроме положительной обратной связи на запрос.

    :return: StandardResponse, ответ о корректной работе сервера
    """
    return StandardResponse(message="API works!")


@app.get("/app_info", status_code=status.HTTP_200_OK, response_model=AppInfoResponse)
async def app_info():
    """
    Путь для получения информации о серверной части приложения.

    Получаемая информация:
        * app_name: str, имя приложения
        * app_version: str, версия приложения
        * app_description: str, описание приложения
        * admin_name: str, ФИО ответственного
        * admin_email: str, адрес электронной почты для связи с ответственным

    :return: InfoResponse, ответ, содержащий информацию о серверной части приложения
    """
    return AppInfoResponse(
        app_name=settings.APP_NAME,
        app_version=settings.APP_VERSION,
        app_description=settings.APP_DESCRIPTION,
        admin_name=settings.ADMIN_NAME,
        admin_email=settings.ADMIN_EMAIL,
    )

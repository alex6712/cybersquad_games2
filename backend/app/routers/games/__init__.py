"""
Factory CRM API games routers

Модуль с описанием роутеров игр.

Алексей Ванюков
vanyukov.alex@gmail.com
"""

from fastapi import APIRouter

from .blackjack import router as _blackjack_router

router = APIRouter(
    prefix="/games",
)
router.include_router(_blackjack_router)

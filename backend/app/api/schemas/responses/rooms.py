from typing import Tuple

from pydantic import Field

from app.api.schemas import RoomSchema
from app.api.schemas.responses import StandardResponse


class RoomsResponse(StandardResponse):
    """Модель ответа с данными об игровой комнате.

    Используется в качестве ответа от сервера на запрос об игровой комнате.

    See also
    --------
    schemas.responses.standard.StandardResponse
    schemas.room.RoomSchema
    """
    rooms: Tuple[RoomSchema, ...] = Field(
        example=(
            RoomSchema(id="0", game_type="CG_BLACKJACK_GAME"),
            RoomSchema(id="12", title="Я создал. Заходите.", game_type="CG_POKER_GAME"),
        )
    )

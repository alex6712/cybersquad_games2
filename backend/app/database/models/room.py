from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import BaseModel


class RoomModel(BaseModel):
    __tablename__ = "room"

    title: Mapped[str] = mapped_column(String(256), nullable=False, default="Новая комната")
    password: Mapped[str] = mapped_column(String(256))
    game_type: Mapped[str] = mapped_column(String(256))

    def __repr__(self):
        return f"<{self.__class__.__name__}(title={self.title}, password={self.password}, game_type={self.game_type})>"

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.models import DBBaseModel


class DBUserModel(DBBaseModel):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(256), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(String(256))
    phone: Mapped[str] = mapped_column(String(256))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"username={self.username!r}, " \
               f"password={self.password!r}, " \
               f"email={self.email!r}, " \
               f"phone={self.phone!r}" \
               f")>"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

Base = declarative_base()


class DBBaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id!r})>"


class DBJoinBaseModel(Base):
    __abstract__ = True

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

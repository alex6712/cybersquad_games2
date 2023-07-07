from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base

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

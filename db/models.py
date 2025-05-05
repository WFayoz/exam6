from sqlalchemy import BIGINT, DATE, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, db
from db.utils import CreatedModel


class User(CreatedModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)


metadata = Base.metadata

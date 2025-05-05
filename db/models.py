from sqlalchemy import BIGINT, DATE, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, db
from db.utils import CreatedModel


class User(CreatedModel):
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)


class Category(CreatedModel):
    __tablename__ = "categories"
    name: Mapped[str]
    todos: Mapped[list['ToDo']] = relationship(back_populates="category", lazy='joined')
    metadata = Base.metadata


class ToDo(CreatedModel):
    dead_line: Mapped[str] = mapped_column(DATE)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id', ondelete='CASCADE'))
    category: Mapped['Category'] = relationship(back_populates="todos", lazy='joined')


metadata = Base.metadata

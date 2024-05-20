from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, ARRAY, INTEGER
from typing import List
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey, CheckConstraint, DateTime
from app.database import Base


class User(Base):
    __tablename__ = 'users' 

    id              : Mapped[str] = mapped_column(String(72), primary_key=True)
    username        : Mapped[str] = mapped_column(String(72), unique=True)
    firstname       : Mapped[str] = mapped_column(String(72))
    name            : Mapped[str] = mapped_column(String(72))
    email           : Mapped[str] = mapped_column(String(72), unique=True)
    password        : Mapped[str] = mapped_column(String(72))
    interests       : Mapped[str] = mapped_column(String(72))
    admin            : Mapped[bool] = mapped_column(Boolean(), default=False)
    articles: Mapped[List["Article"]] = relationship()

class Article(Base):
    __tablename__ = 'articles' 

    id = Column(Integer, primary_key=True)
    author_id : Mapped[str] = mapped_column(ForeignKey("users.id"))  # Clé étrangère vers la table users
    title = mapped_column(String, nullable=False)
    date = mapped_column(DateTime)
    content = mapped_column(String(1024))
    theme = mapped_column(String(64))
    note = mapped_column(Integer)
    author : Mapped["User"] = relationship()
    __table_args__ = (
        CheckConstraint('theme IN ("sport", "culture", "politics", "economics", "health", "environment", "social", "technology", "international")', name='check_theme'),
        CheckConstraint('note >= 0 AND note <= 5', name='check_note_range'),
    )
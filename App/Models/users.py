from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, ARRAY, INTEGER
from typing import List
from App.Models.articles import Article

from App.database import Base


class User(Base):
    __tablename__ = 'users' 

    id              : Mapped[str] = mapped_column(String(72), primary_key=True)
    username        : Mapped[str] = mapped_column(String(72), unique=True)
    firstname       : Mapped[str] = mapped_column(String(72))
    name            : Mapped[str] = mapped_column(String(72))
    email           : Mapped[str] = mapped_column(String(72), unique=True)
    password        : Mapped[str] = mapped_column(String(72))
    interests       = Column(ARRAY(String(72)))
    admin            : Mapped[bool] = mapped_column(Boolean(), default=False)
    articles: Mapped[List["Article"]] = relationship()

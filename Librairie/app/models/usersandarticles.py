from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, ARRAY, INTEGER
from typing import List
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey, CheckConstraint, Date, UniqueConstraint
from app.database import Base


class User(Base):
    __tablename__ = 'users' 

    id : Mapped[str] = mapped_column(String(72), primary_key=True)
    username : Mapped[str] = mapped_column(String(72), unique=True)
    firstname : Mapped[str] = mapped_column(String(72))
    name : Mapped[str] = mapped_column(String(72))
    email : Mapped[str] = mapped_column(String(72), unique=True)
    password : Mapped[str] = mapped_column(String(72))
    interests : Mapped[List[str]] = mapped_column((String(64)), nullable=True)
    admin : Mapped[bool] = mapped_column(Boolean, default=False)
    articles: Mapped[List["Article"]] = relationship("Article", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    
class Article(Base):
    __tablename__ = 'articles' 

    id              : Mapped[str] = mapped_column(String(72), primary_key=True)
    author_username : Mapped[str] = mapped_column(String(72), ForeignKey("users.username"), nullable=False)
    title           : Mapped[str] = mapped_column(String(72))
    date                          = Column(Date)
    content         : Mapped[str] = mapped_column(String(2048))
    theme           : Mapped[str] = mapped_column(String(72))
    likes           : Mapped[int] = mapped_column(Integer, default=0)
    dislikes        : Mapped[int] = mapped_column(Integer, default=0)
    #author = relationship("User", foreign_keys=[author_id, author_username])
    author = relationship("User", back_populates="articles")
    comments: Mapped[List["Comment"]] = relationship( "Comment", back_populates="article")
    __table_args__ = (
        CheckConstraint('theme IN ("sport", "music", "cinema", "politics", "economics", "health", "environment", "social", "technology", "international")', name='check_theme'),
        CheckConstraint('likes >= 0' , name='check_like_range'),
        CheckConstraint('dislikes >= 0' , name='check_dislike_range'),
    )

class Comment(Base):
    __tablename__ = 'comments'
    author_id      : Mapped[str] = mapped_column(String(72), ForeignKey("users.id"), primary_key = True)
    article_id     : Mapped[str] = mapped_column(String(72), ForeignKey("articles.id"), primary_key = True)
    content        : Mapped[str] = mapped_column(String(1024))
    article = relationship("Article", back_populates="comments")
    author = relationship("User", back_populates="comments")
    __table_args__ = (
        UniqueConstraint('author_id', 'article_id', name='uq_author_article'),)
    


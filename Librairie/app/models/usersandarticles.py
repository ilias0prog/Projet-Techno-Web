from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, ARRAY, INTEGER
from typing import List
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey, CheckConstraint, DateTime, UniqueConstraint
from app.database import Base


class User(Base):
    __tablename__ = 'users' 

    id = Column(String(72), primary_key=True)
    username = Column(String(72), unique=True)
    firstname = Column(String(72))
    name = Column(String(72))
    email = Column(String(72), unique=True)
    password = Column(String(72))
    interests = Column(String(72), nullable=True)
    admin = Column(Boolean(), default=False)
    articles: Mapped[List["Article"]] = relationship()
    comments = relationship("Comment", back_populates="author")
    
class Article(Base):
    __tablename__ = 'articles' 

    id = Column(Integer, primary_key=True)
    author_id = Column(String(72), ForeignKey("users.id"))  # Clé étrangère vers la table users
    title = Column(String, nullable=False)
    date = Column(DateTime)
    content = Column(String(1024))
    theme = Column(String(64))
    likes = Column(Integer)
    dislikes = Column(Integer)
    author = relationship("User", back_populates="articles")
    comments: Mapped[List["Comment"]] = relationship( "Comment", back_populates="article")
    __table_args__ = (
        CheckConstraint('theme IN ("sport", "culture", "politics", "economics", "health", "environment", "social", "technology", "international")', name='check_theme'),
        CheckConstraint('like >= 0 AND dislike >= 0', name='check_note_range'),
    )

class Comment(Base):
    __tablename__ = 'comments'
    author_id = Column(String(72), ForeignKey("users.id"), primary_key = True ) 
    article_id = Column(Integer, ForeignKey("articles.id"), primary_key = True )
    content = Column(String(1024))
    article = relationship("Article", back_populates="comments")
    author = relationship("User", back_populates="comments")
    __table_args__ = (
        UniqueConstraint('author_id', 'article_id', name='uq_author_article'),)
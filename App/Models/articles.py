from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey, CheckConstraint, DateTime
#from App.Models.users import User
from App.database import Base


class Article(Base):
    __tablename__ = 'articles' 

    id = Column(Integer, primary_key=True)
    author_id : Mapped[str] = mapped_column(ForeignKey("users.id"))  # Clé étrangère vers la table users
    user : Mapped["User"] = relationship()  # Relation avec la table users
    title = mapped_column(String, nullable=False)
    date = mapped_column(DateTime)
    content = mapped_column(String(1024))
    theme = mapped_column(String(64))
    note = mapped_column(Integer)

    __table_args__ = (
        CheckConstraint('theme IN ("sport", "culture", "politics", "economics", "health", "environment", "social", "technology", "international")', name='check_theme'),
        CheckConstraint('note >= 0 AND note <= 5', name='check_note_range'),
    )
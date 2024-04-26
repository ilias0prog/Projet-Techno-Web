from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey, CheckConstraint
from App.Models.users import User
from App.database import Base


class Article(Base):
    __tablename__ = 'articles' 

    id = Column(Integer, primary_key=True)
    author_id : Mapped[str] = mapped_column(ForeignKey("users.id"))  # Clé étrangère vers la table users
    user : Mapped["User"] = relationship()  # Relation avec la table users
    title = mapped_column(String, constraints=[CheckConstraint('LENGTH(titre) > 0', name='check_titre_length')])
    date = mapped_column(Column(String), "date", "datetime")
    content = mapped_column(String(1024))
    theme = mapped_column(String(64), constraints=[CheckConstraint(
        'theme IN ("sport", "culture", "politics", "economics", "health", "environment", "social", "technology", "international")',
        name='check_theme')])
    note = mapped_column(Integer, constraints=[CheckConstraint('mon_entier >= 0 AND mon_entier <= 5', name='check_entier_range')])

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Column, Integer, ForeignKey

from App.database import Base


class Aricle(Base):
    __tablename__ = 'articles' 

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))  # Clé étrangère vers la table users
    user = relationship("User", back_populates="articles")
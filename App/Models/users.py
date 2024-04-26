from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Column, ARRAY, Integer, CheckConstraint

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
    note = mapped_column(Integer, constraints=[
        CheckConstraint('mon_entier >= 0 AND mon_entier <= 5', name='check_entier_range')])
    
    # Si on utilise MongoDB pour les articles, on peut faire en parallèle :
        # Une DB mySQL contenant :
            # - une table avec tous les users
            # - soit une table avec tous les id des articles (en lien avec leur id dans la db MongoDB) et l'id de son auteur, du coup tous les id d'articles sont dans une table
            # - soit une table par thème d'articles, ex : dans la table "sport" on met tous les articles de sport, etc
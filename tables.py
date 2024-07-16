import hashlib
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class Livre(Base):
    __tablename__ = 'livres'

    id = Column(Integer, primary_key=True)
    titre = Column(String(100))
    auteur = Column(String(100))
    annee = Column(Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'titre': self.titre,
            'auteur': self.auteur,
            'annee': self.annee
        }

class Personne(Base):
    __tablename__ = 'personnes'

    def hash_password(self, password):
        # Fonction de hachage pour le mot de passe
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    id = Column(Integer, primary_key=True)
    nom = Column(String(100))
    prenom = Column(String(100))
    abonne = Column(String(100))
    password = Column(String(150))

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'abonne': self.abonne,
        }

    @classmethod
    def get_by_username(cls, db_session, username):
        return db_session.query(cls).filter_by(nom=username).first()

    def verify_password(self, password):
        hashed_password = self.hash_password(password)
        return self.password == hashed_password


class Emprunt(Base):
    __tablename__ = 'emprunts'

    id = Column(Integer, primary_key=True)
    livre_id = Column(Integer, ForeignKey('livres.id'))
    personne_id = Column(Integer, ForeignKey('personnes.id'))
    heure_emprunt = Column(DateTime)

    livre = relationship("Livre", backref="emprunts")
    personne = relationship("Personne", backref="emprunts")

    def to_dict(self):
        return {
            'id': self.id,
            'livre_id': self.livre_id,
            'personne_id': self.personne_id,
            'heure_emprunt': self.heure_emprunt
        }

class Remise(Base):
    __tablename__ = 'remises'

    id = Column(Integer, primary_key=True)
    emprunt_id = Column(Integer, ForeignKey('emprunts.id'))
    heure_remise = Column(DateTime)

    emprunt = relationship("Emprunt", backref="remises")

    def to_dict(self):
        return {
            'id': self.id,
            'emprunt_id': self.emprunt_id,
            'heure_remise': self.heure_remise
        }

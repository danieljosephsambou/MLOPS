from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Chemin absolu vers le fichier SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "m2dsia_etudiants.db")
DATABASE_URL = f"sqlite:///{db_path}"

# Création de l'engine SQLite avec les bons arguments
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # obligatoire avec SQLite
)

# Session locale pour accéder à la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles SQLAlchemy
Base = declarative_base()
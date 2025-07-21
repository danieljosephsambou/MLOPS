import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from schemas.schemas import User
from db.connexion import SessionLocal
from db.crud import create_user

db = SessionLocal()

data = {
    "email": "lipson.soume@isi.com",
    "nom": "lipson",
    "prenom": "soume",
    "classe": "MLOps 2025"
}

user = User(**data)
result = create_user(db, user)
print(User.from_orm(result).dict())
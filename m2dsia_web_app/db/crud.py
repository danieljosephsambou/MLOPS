from sqlalchemy.orm import Session
from db.connexion import engine
from models.models import User as UserModel
from schemas.schemas import User
from db.connexion import Base

# Crée les tables
Base.metadata.create_all(bind=engine)

def create_user(db: Session, user: User):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def get_all_users(db: Session):
    return db.query(UserModel).all()

def update_user(db: Session, email: str, user_update: User):
    db_user = get_user(db, email)
    if not db_user:
        return None
    for field, value in user_update.dict().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    db_user = get_user(db, email)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

if __name__ == "__main__":
    print("Hello")
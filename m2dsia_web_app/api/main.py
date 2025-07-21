from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.connexion import SessionLocal
from db import crud
from schemas.schemas import User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/{email}")
def read_user(email: str, db: Session = Depends(get_db)):
    return crud.get_user(db, email)

@app.get("/users/")
def read_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

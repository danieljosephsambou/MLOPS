from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connexion import SessionLocal
from schemas.schemas import User
from db.crud import (
    create_user, get_user, get_all_users,
    update_user, delete_user
)

app = FastAPI()

# Dépendance à injecter dans chaque route
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def add_user(user: User, db: Session = Depends(get_db)):
    db_user = get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db, user)

@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@app.get("/users/{email}")
def read_user(email: str, db: Session = Depends(get_db)):
    user = get_user(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{email}")
def update_user_endpoint(email: str, user: User, db: Session = Depends(get_db)):
    updated_user = update_user(db, email, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{email}")
def delete_user_endpoint(email: str, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, email)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": f"User {email} deleted"}

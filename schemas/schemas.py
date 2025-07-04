from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    nom: str
    prenom: str
    classe: str

    class Config:
        from_attributes = True

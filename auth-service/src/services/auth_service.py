from passlib.context import CryptContext
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models import User
from src.schemas import UserCreate, UserLogin
from src.database import get_db
import jwt, os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "secret")


def register_user(user: UserCreate, db: Session = next(get_db())):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = pwd_context.hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "email": new_user.email}


def login_user(user: UserLogin, db: Session = next(get_db())):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = jwt.encode({"user_id": db_user.id}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}
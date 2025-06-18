from fastapi import APIRouter, HTTPException, Depends
from src.schemas import UserCreate, UserLogin
from src.services import auth_service

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    return auth_service.register_user(user)

@router.post("/login")
def login(user: UserLogin):
    return auth_service.login_user(user)
from fastapi import FastAPI
from src.routers import auth

app = FastAPI(title="Auth Service")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

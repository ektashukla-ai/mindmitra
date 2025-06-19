from fastapi import APIRouter
from src.schemas import UserQuery, BotResponse
from src.services.llm_service import generate_response

router = APIRouter()

@router.post("/", response_model=BotResponse)
def chat_with_bot(query: UserQuery):
    response = generate_response(query.message)
    return {"response": response}
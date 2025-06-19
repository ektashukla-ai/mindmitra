from fastapi import APIRouter
from src.services.vector_store import load_documents_to_vector_db

router = APIRouter()

@router.post("/load")
def load_documents():
    count = load_documents_to_vector_db()
    return {"message": f"{count} documents embedded successfully."}
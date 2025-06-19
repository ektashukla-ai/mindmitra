import uvicorn
from fastapi import FastAPI
from src.routers import chatbot, embed
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Chatbot Core Service")

app.include_router(chatbot.router, prefix="/chat", tags=["Chatbot"])
app.include_router(embed.router, prefix="/embed", tags=["Embedding"])

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
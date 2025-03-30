from fastapi import APIRouter
from app.schemas.chatbot import ChatRequest, ChatResponse

# Create an API router for chatbot-related routes
router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/message", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_message = request.message
    return {"response": f"Echo: {user_message}"}

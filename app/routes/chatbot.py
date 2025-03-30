from fastapi import APIRouter
from app.schemas.chatbot import ChatRequest, ChatResponse
from app.services.ai_service import get_ai_response

# Create an API router for chatbot-related routes
router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/message", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_message = request.message
    ai_response = get_ai_response(user_message)
    return {"response": ai_response}

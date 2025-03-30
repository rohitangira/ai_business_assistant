from fastapi import APIRouter
from app.services.ai_service import get_faq_response
from app.schemas.faq import FAQRequest, FAQResponse  # ✅ Import from faq.py

router = APIRouter()

@router.post("/faq", response_model=FAQResponse)
async def handle_faq(request: FAQRequest):
    """Handles FAQ queries using AI."""
    answer = get_faq_response(request.question)
    return FAQResponse(response=answer)

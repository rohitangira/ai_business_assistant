from fastapi import APIRouter
from app.services.order_service import get_order_status  # Import AI/order service
from app.schemas.order import OrderStatusRequest, OrderStatusResponse

router = APIRouter()

@router.post("/status", response_model=OrderStatusResponse)
async def check_order_status(request: OrderStatusRequest):
    """Fetch order status from AI or Database."""
    status, delivery_date = get_order_status(request.order_id)
    return OrderStatusResponse(status=status, estimated_delivery=delivery_date)

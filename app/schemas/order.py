from pydantic import BaseModel

class OrderStatusRequest(BaseModel):
    order_id: str

class OrderStatusResponse(BaseModel):
    status: str
    estimated_delivery: str

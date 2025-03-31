import random
from datetime import datetime, timedelta

def get_order_status(order_id: str):
    """Simulates checking order status."""
    statuses = ["Processing", "Shipped", "Out for Delivery", "Delivered"]
    status = random.choice(statuses)

    estimated_days = random.randint(1, 7)
    estimated_delivery = (datetime.now() + timedelta(days=estimated_days)).strftime("%Y-%m-%d")

    return status, estimated_delivery

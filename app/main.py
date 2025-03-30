from fastapi import FastAPI
from app.routes import chatbot,customer


app = FastAPI(title="AI Business Workflow Assistant")

# Include chatbot routes
app.include_router(chatbot.router)
app.include_router(customer.router, prefix="/customer", tags=["Customer Support"])

@app.get("/")
def root():
    return {"message": "AI Business Workflow Assistant is running!"}

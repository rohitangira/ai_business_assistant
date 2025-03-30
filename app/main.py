from fastapi import FastAPI
from app.routes import chatbot

app = FastAPI(title="AI Business Workflow Assistant")

# Include chatbot routes
app.include_router(chatbot.router)

@app.get("/")
def root():
    return {"message": "AI Business Workflow Assistant is running!"}

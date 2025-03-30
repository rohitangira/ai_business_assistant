from pydantic import BaseModel

class FAQRequest(BaseModel):
    question: str

class FAQResponse(BaseModel):
    response: str

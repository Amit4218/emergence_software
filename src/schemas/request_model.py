from pydantic import BaseModel


class ChatBotRequestBody(BaseModel):
    question: str


class MessageRequestBody(BaseModel):
    name: str
    email: str
    message: str

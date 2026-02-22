from pydantic import BaseModel


class ChatBotRequestBody(BaseModel):
    question: str

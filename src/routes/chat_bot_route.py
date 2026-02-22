from fastapi.routing import APIRouter

from src.schemas.request_model import ChatBotRequestBody
from src.schemas.response_models import (
    ChatBotResponseModel,
    ErrorResponseModel,
    SuccessResponseModel,
)
from src.services.open_router import send_chat_request
from src.utils.extract_resume import extract_resume_text

chabotroute = APIRouter(prefix="/api/chatbot", tags=["chatbot"])


@chabotroute.post("/", response_model=SuccessResponseModel | ErrorResponseModel)
def return_chatbot_response(requiter_question: ChatBotRequestBody):
    """extract resume text and send request to openrouter"""
    try:
        resume = extract_resume_text()
        response = send_chat_request(resume_data=resume, question=requiter_question)
        return SuccessResponseModel(data=ChatBotResponseModel(response=response))
    except Exception:
        return ErrorResponseModel()

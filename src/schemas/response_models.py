from typing import Any, Dict, List

from pydantic import BaseModel, ConfigDict


class ProjectsResponseModel(BaseModel):
    project_name: str
    project_description: str
    learnings: List[str]
    languages: List[str]
    frameworks: Dict
    links: List[dict]
    preview_image: str

    model_config = ConfigDict(from_attributes=True)


class ProjectsListSuccessResponse(BaseModel):
    status: int = 200
    message: str = "successful"
    data: List[ProjectsResponseModel]


class ChatBotResponseModel(BaseModel):
    response: str


class ErrorResponseModel(BaseModel):
    status: int = 500
    message: str = "unsuccessful"
    data: Any = None


class SuccessResponseModel(BaseModel):
    status: int = 200
    message: str = "successful"
    data: Any = None

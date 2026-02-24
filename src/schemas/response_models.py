from typing import Any, List

from pydantic import BaseModel, ConfigDict


class ProjectsResponseModel(BaseModel):
    project_name: str
    project_description: str
    learnings: List[str]
    languages: List[str]
    frameworks: List[str]
    tools: List[str]
    github: str
    link: str | None
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

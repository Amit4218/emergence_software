from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session

from config.db import get_db
from src.models.project_model import Message, Project
from src.schemas.request_model import MessageRequestBody
from src.schemas.response_models import (
    ErrorResponseModel,
    MessagesListSuccessResponse,
    ProjectsListSuccessResponse,
    ProjectsResponseModel,
    SuccessResponseModel,
)

siteRouter = APIRouter(prefix="/api/projects", tags=["projects"])


@siteRouter.get("/", response_model=ProjectsListSuccessResponse)
def get_projects(db: Session = Depends(get_db)):
    """retrive the projects data"""
    try:
        projects = db.execute(select(Project)).scalars().all()
        return {
            "status": 200,
            "message": "successful",
            "data": projects,
        }
    except Exception:
        return ErrorResponseModel()


@siteRouter.post("/project", response_model=SuccessResponseModel)
def save_project_data(data: ProjectsResponseModel, db: Session = Depends(get_db)):
    """retrive the projects data"""
    try:
        project = Project(**data.model_dump())
        db.add(project)
        db.commit()
        db.refresh(project)
        return SuccessResponseModel()
    except Exception:
        return ErrorResponseModel()


@siteRouter.post("/message", response_model=SuccessResponseModel)
def save_message(data: MessageRequestBody, db: Session = Depends(get_db)):
    message = Message(**data.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)
    return SuccessResponseModel()


@siteRouter.get("/messages", response_model=MessagesListSuccessResponse)
def get_messages(db: Session = Depends(get_db)):
    messages = db.execute(select(Message)).scalars().all()
    return {
        "status": 200,
        "message": "successful",
        "data": messages,
    }

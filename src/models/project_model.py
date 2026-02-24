from datetime import datetime
from typing import List

from sqlalchemy import JSON, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from config.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    project_description: Mapped[str] = mapped_column(Text, nullable=False)
    learnings: Mapped[List[str]] = mapped_column(JSON, nullable=True)
    languages: Mapped[List[str]] = mapped_column(JSON, nullable=True)
    frameworks: Mapped[List[str]] = mapped_column(JSON, nullable=True)
    tools: Mapped[List[str]] = mapped_column(JSON, nullable=True)
    github: Mapped[str] = mapped_column(String, nullable=True)
    link: Mapped[str] = mapped_column(String, nullable=True)
    preview_image: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

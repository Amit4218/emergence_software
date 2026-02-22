from datetime import datetime
from typing import Any, Dict, List

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
    frameworks: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable=True)
    links: Mapped[List[Dict[str, Any]]] = mapped_column(JSON, nullable=True)
    preview_image: Mapped[str] = mapped_column(String(500), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

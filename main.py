from fastapi import FastAPI

import src.models  # noqa: F401 ignoring ruff unused-import
from config.base import Base
from config.db import engine
from src.routes.chat_bot_route import chabotroute
from src.routes.site_data_routes import siteRouter

app = FastAPI()
app.include_router(siteRouter)
app.include_router(chabotroute)
Base.metadata.create_all(bind=engine)


@app.get("/")
async def read_root():
    return {"Application running"}

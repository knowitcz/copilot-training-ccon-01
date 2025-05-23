from fastapi import FastAPI
from app.db import SQLModel, engine
from app.api.account_routes import router as account_router
from app.startup import create_default_accounts

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(account_router, prefix="/api/v1", tags=["v1"])

create_default_accounts()
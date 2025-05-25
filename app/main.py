from fastapi import FastAPI
from app.db import SQLModel, engine
from app.api.account_routes import router as account_router
from app.api.bank_routes import router as bank_router
from app.startup import create_default_accounts

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(account_router, prefix="/api/v1", tags=["v1"])
app.include_router(bank_router, prefix="/api/v0", tags=["v0"])

create_default_accounts()
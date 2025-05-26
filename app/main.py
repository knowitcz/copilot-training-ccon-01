from fastapi import FastAPI
from app.db import SQLModel, engine
from app.api.account_routes import router as account_router
from app.api.bank_routes import router as bank_router
from app.api.client_routes import router as client_router
from app.startup import create_default_accounts

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(account_router, prefix="/api/v1", tags=["accounts"])
app.include_router(bank_router, prefix="/api/v1", tags=["transfers"])
app.include_router(client_router, prefix="/api/v1", tags=["client"])

create_default_accounts()
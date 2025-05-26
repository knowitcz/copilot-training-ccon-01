from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.dependencies import get_client_service
from app.models.client import Client
from app.services.client_service import ClientService
from typing import List

router = APIRouter()

@router.get("/clients", response_model=List[Client])
def list_clients(client_service: ClientService = Depends(get_client_service)):
    return client_service.get_all_clients()

@router.post("/clients", response_model=Client)
def add_client(client: Client, client_service: ClientService = Depends(get_client_service)):
    try:
        client_service.add_client(client)
        return client
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

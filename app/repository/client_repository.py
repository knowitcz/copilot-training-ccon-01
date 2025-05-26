from sqlmodel import Session, select
from app.models.client import Client

class ClientRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Client]:
        statement = select(Client)
        return list(self.session.exec(statement))

    def add(self, client: Client) -> None:
        self.session.add(client)
        self.session.commit()

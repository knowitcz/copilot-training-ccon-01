from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def get_session():
    return Session(engine)
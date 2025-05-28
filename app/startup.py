from sqlmodel import select, func
from app.db import get_session
from app.models.account import Account
from sqlalchemy.sql import text

import os

def read_sql_file(sql_file_path):
    with open(sql_file_path, "r") as sql_file:
        return sql_file.read()

def create_default_accounts():
    sql_file_path = os.path.join(os.path.dirname(__file__), "../resources/data/default_accounts.sql")
    with get_session() as session:
        statement = select(func.count()).select_from(Account)
        account_count = session.exec(statement).one()
        if account_count > 0:
            return

        sql_script = read_sql_file(sql_file_path)
        session.exec(text(sql_script))
        session.commit()

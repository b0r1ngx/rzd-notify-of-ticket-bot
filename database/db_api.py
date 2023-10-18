from sqlalchemy import Executable

from sqlalchemy.dialects.sqlite import insert

from database.db_session import Session
from database.tables.User import User


def commit_user_to_db(chat_id: int) -> None:
    insert_stmt = insert(User).values({
        'chat_id': chat_id
    })

    on_conflict_stmt = insert_stmt.on_conflict_do_nothing()
    execute_stmt(on_conflict_stmt)


def execute_stmt(stmt: Executable) -> bool:
    with Session() as s:
        s.execute(stmt)
        s.commit()
    return True
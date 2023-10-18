from database.db_api import commit_user_to_db
from database.tables import User


def prepare_user_data_for_commit(from_user: User) -> None:
    user = {
        'chat_id': from_user.id,
        'username': from_user.username,
        'first_name': from_user.first_name
    }
    commit_user_to_db(user)
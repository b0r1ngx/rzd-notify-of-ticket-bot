from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as S, sessionmaker
from sqlalchemy import create_engine
import logging

# Declaration 2 basic objects, that was used for:
# Tables realisation (all tables extends from this base class)
Base = declarative_base()
# Interaction with DB
Session: S = sessionmaker()

path = 'database/cryptobot.db'
sqlite_path = 'sqlite:///' + path + '?check_same_thread=False'


def init_database_session() -> None:
    """Initialize global Session for interacting with DB.
    Method must be called firstly, if Application want to interact with DB, when calling Session().
    :return: None
    """
    engine = create_engine(url=sqlite_path, echo=False)

    logging.info('Подключение к базе данных')
    Session.configure(bind=engine)

    if not database_exists(engine.url):
        logging.info('Создание базы данных')
        create_database(engine.url)

    logging.info('Инициализация таблиц')
    Base.metadata.create_all(engine)

    logging.info('Объект Session, для доступа к базе данных, доступен')

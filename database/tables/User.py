from database.db_session import Base
from datetime import datetime as dt
from sqlalchemy import Column, Integer, BigInteger, DateTime, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    chat_id = Column(BigInteger, unique=True)
    # referred_by = Column(String)

    created_at = Column(DateTime, default=dt.now())
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import SQLALCHEMY_DATABASE_URI


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

Session = sessionmaker(bind=engine)
db = Session()


class Site(Base):
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True)
    phrase = Column(String, nullable=False)
    url = Column(String, nullable=False)
    query = Column(String, nullable=False)
    is_interested = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())

    def __init__(self, phrase, url, query, is_interested=None):
        self.phrase = phrase
        self.url = url
        self.query = query
        self.is_interested = is_interested

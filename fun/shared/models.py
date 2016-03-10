import logging
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from shared.settings import SQLALCHEMY_DATABASE_URI
from shared.settings import INTERESTING_ROBOT_PHRASES


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base = declarative_base()

Session = sessionmaker(bind=engine)
db = Session()


class Site(Base):
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True)
    phrase = Column(String, nullable=False)
    url = Column(String, nullable=False)
    operator = Column(String, nullable=False)
    content = Column(String, nullable=False)
    is_interested = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())

    def __init__(self, phrase, url, operator, content, is_interested=None):
        self.phrase = phrase
        self.url = url
        self.operator = operator
        self.content = content
        self.is_interested = is_interested

    def save(self):
        db.add(self)
        db.commit()

    @classmethod
    def get_sites(cls, is_interested=False, _all=False):
        if _all:
            return db.query(cls).all()
        return db.query(cls).filter_by(is_interested=is_interested).all()

    @classmethod
    def dump_all_to_file(cls, filename):
        sites = cls.get_sites(_all=True)
        with open(filename, 'w') as _file:
            for site in sites:
                _file.write('Phrase: {} Operator: {}\n'.format(site.phrase,
                                                               site.operator))
                _file.write('Content: {}\n'.format(
                    site.content.encode('utf-8')))
                _file.write('Url: {} \n\n'.format(site.url))

    def pretty_print(self):
        print 'Phrase: {} Operator: {}'.format(self.phrase, self.operator)
        print 'Content: {}'.format(self.content.encode('utf-8'))
        print 'Url: {} \n'.format(self.url)


class Link(Base):
    __tablename__ = 'link'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    robot_file = Column(Text)

    def __init__(self, url, robot_file=None):
        self.url = url

    @classmethod
    def save_many(cls, urls):
        for url in urls:
            cls(url=url.lower()).save()

    @classmethod
    def dump_to_file(cls, filename='links.txt'):
        links = db.query(cls).all()
        with open(filename, 'w') as _file:
            for link in links:
                _file.write(link.url + '\n')

    @classmethod
    def get_by_url(cls, url):
        return db.query(cls).filter_by(url=url).first()

    @classmethod
    def get_all(cls):
        return db.query(cls).all()

    @classmethod
    def find_interesting(cls, phrases=INTERESTING_ROBOT_PHRASES):
        links = cls.get_all()
        results = {phrase: [] for phrase in phrases}
        for link in links:
            for phrase in phrases:
                if link.robot_file:
                    if phrase in link.robot_file:
                        results[phrase].append(link.url)
                else:
                    logging.info('Phrase: %s not found in %s',
                                 phrase,
                                 link.url)

        return results

    def save(self):
        if not Link.get_by_url(url=self.url):
            db.add(self)
            db.commit()

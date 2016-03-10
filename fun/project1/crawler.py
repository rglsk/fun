from googlesearch import GoogleSearch
from sqlalchemy.orm import sessionmaker

from shared.models import Base
from shared.models import engine
from shared.models import Site


GOOGLE_OPERATORS = ['inurl', 'allintext', 'intext', 'allinanchor', 'intitle']

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def google_crawler(phrase):
    """Searching in google for given phrase using operators such us:
        - inurl
        - allintext
        - intext
        - allinanchor
        - intitle

    Results are saved in database.
    """

    for operator in GOOGLE_OPERATORS:
        query = '{}:{}'.format(operator, phrase)
        gs = GoogleSearch(query)
        google_results = gs.top_results()
        for google_result in google_results:
            site = Site(phrase=phrase,
                        operator=operator,
                        content=google_result['content'],
                        url=google_result['url'])
            site.save()

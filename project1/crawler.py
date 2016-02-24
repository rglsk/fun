from googlesearch import GoogleSearch
from sqlalchemy.orm import sessionmaker

from models import Base
from models import engine


GOOGLE_OPERATORS = ['inurl', 'allintext']  #, 'intext', 'allinanchor']

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def google_crawler(phrase):
    important_keys = ['url', 'content']
    results = {operator: [] for operator in GOOGLE_OPERATORS}

    for operator in GOOGLE_OPERATORS:
        query = '{}:{}'.format(operator, phrase)
        gs = GoogleSearch(query)
        google_results = gs.top_results()
        for google_result in google_results:
            results[operator].append({key: google_result[key]
                                      for key in important_keys})
    return {phrase: results}




if __name__ == '__main__':
    # phrases = raw_input('Please type phrases separate by space: ').split(' ')
    phrases = ['bla', 'foo']
    google_results = [google_crawler(phrase) for phrase in phrases]
    import ipdb; ipdb.set_trace()

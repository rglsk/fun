from googlesearch import GoogleSearch

from shared.models import Site


GOOGLE_OPERATORS = ['inurl', ] #'allintext', 'intext', 'allinanchor', 'intitle']

VULGAR_WORDS = ['dupa', 'kupa', 'kurwa', 'pierdolenie']


def google_crawler(phrase, vulgar_words=None):
    """Searching in google for given phrase using operators such us:
        - inurl
        - allintext
        - intext
        - allinanchor
        - intitle

    Results are saved in database.

    Returns total count of saved results.
    """
    total_count = 0
    for operator in GOOGLE_OPERATORS:
        query = '{}:{}'.format(operator, phrase)
        gs = GoogleSearch(query)
        google_results = gs.top_results()
        total_count += len(google_results)
        for google_result in google_results:
            site = Site(phrase=phrase,
                        operator=operator,
                        content=google_result['content'],
                        url=google_result['url'])
            site.save()

    return total_count

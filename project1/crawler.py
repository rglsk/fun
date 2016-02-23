from googlesearch import GoogleSearch

GOOGLE_OPERATORS = ['inurl', 'allintext', 'intext', 'site', 'allinanchor']


def google_crawler(operator, phrases):
    query = 'inurl:bla'
    gs = GoogleSearch(query)
    for url in gs.top_urls():
        print url


if __name__ == '__main__':
    google_crawler('', '')

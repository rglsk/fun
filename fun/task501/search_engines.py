import duckduckgo
from googlesearch import GoogleSearch
from py_bing_search import PyBingSearch

from shared.settings import BING_API_KEY


def google_search(query, limit=1):
    gs = GoogleSearch(query)
    top = gs.top_result()
    if not top:
        return {'content': '', 'url': ''}
    return {'content': top['content'], 'url': top['url']}


def duckduckgo_search(query, limit=1):
    duck = duckduckgo.query(query)
    if not duck.related:
        return {'content': '', 'url': ''}
    return {'content': duck.related[0].text, 'url': duck.related[0].url}


def bing_search(query, limit=1):
    bing = PyBingSearch(BING_API_KEY)
    result_list, next_uri = bing.search(query, limit=limit, format='json')
    if not result_list:
        return {'content': '', 'url': ''}
    return {'content': result_list[0].description, 'url': result_list[0].url}

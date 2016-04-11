import duckduckgo
from googlesearch import GoogleSearch
from py_bing_search import PyBingSearch

from shared.settings import BING_API_KEY


def google_search(query, limit=1):
    gs = GoogleSearch(query)
    tops = gs.top_results()
    if not tops:
        return [{'content': '', 'url': ''}]
    results = [{'content': top['content'], 'url': top['url']} for top in tops]
    return results[:limit]


def duckduckgo_search(query, limit=1):
    duck = duckduckgo.query(query)
    if not duck.related:
        return {'content': '', 'url': ''}
    results = [{'content': top.text, 'url': top.url}
               for top in duck.related]
    return results[:limit]


def bing_search(query, limit=1):
    bing = PyBingSearch(BING_API_KEY)
    result_list, next_uri = bing.search(query, limit=limit, format='json')
    if not result_list:
        return [{'content': '', 'url': ''}]
    results = [{'content': top.description, 'url': top.url}
               for top in result_list]
    return results[:limit]

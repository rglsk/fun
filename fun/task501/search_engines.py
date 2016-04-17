import duckduckgo
from googlesearch import GoogleSearch
from py_bing_search import PyBingSearch

from shared.settings import BING_API_KEY

limit = 5


def google_search(query, limit=limit):
    gs = GoogleSearch(query)
    tops = gs.top_results()
    if not tops:
        return [{'content': '', 'url': ''}] * limit
    results = [{'content': top['content'], 'url': top['url']} for top in tops]
    while len(results) < limit:
        results.append({'content': '', 'url': ''})
    return results[:limit]


def duckduckgo_search(query, limit=limit):
    duck = duckduckgo.query(query)
    if not duck.related:
        return [{'content': '', 'url': ''}] * limit
    results = [{'content': top.text, 'url': top.url}
               for top in duck.related]
    while len(results) < limit:
        results.append({'content': '', 'url': ''})
    return results[:limit]


def bing_search(query, limit=limit):
    bing = PyBingSearch(BING_API_KEY)
    result_list, next_uri = bing.search(query, limit=limit, format='json')
    if not result_list:
        return [{'content': '', 'url': ''}] * limit
    results = [{'content': top.description, 'url': top.url}
               for top in result_list]
    while len(results) < limit:
        results.append({'content': '', 'url': ''})

    return results[:limit]

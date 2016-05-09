import datetime
import os
import uuid
from itertools import islice

import bz2
from gensim.corpora.wikicorpus import extract_pages
from gensim.corpora.wikicorpus import filter_wiki

from elasticsearch import Elasticsearch


EXCLUDED_LIST = ['.git', 'fun', 'include', 'bin', 'lib', 'node_modules',
                 'backend_lib', '.eggs', 'google', 'ki-buildout']
INDEX_PATTERN = 'file_indexer-{nr}'


def index_py_files(es, dir_path):
    if os.path.isfile(dir_path) and dir_path.endswith('.py'):
        print dir_path
        try:
            _, _, _, _, uid, gid, size, atime, mtime, ctime = os.stat(dir_path)
            with open(dir_path, 'r') as _file:
                print dir_path
                doc = {'filename': dir_path,
                       'create_time': datetime.datetime.fromtimestamp(ctime),
                       'modified_time': datetime.datetime.fromtimestamp(mtime),
                       'size': size,
                       'content': _file.read()}
                index_nr = INDEX_PATTERN.format(nr=str(uuid.uuid4()))
                res = es.index(index=index_nr,
                               doc_type='python_file',
                               body=doc)
                print(res)
        except:
            pass
    elif os.path.isdir(dir_path):
        dir_list = os.listdir(dir_path)
        for folder in dir_list:
            path = os.path.join(dir_path, folder)
            if folder not in EXCLUDED_LIST:
                index_py_files(es, path)


def wiki_indexer(dir_path):
    es = Elasticsearch()
    wiki_index = 'wiki_index'
    pages = extract_pages(bz2.BZ2File(dir_path), filter_namespaces=('0',))
    _id = 0
    for title, text, pageid in islice(pages, 0, 50000001):
        doc = {'title': filter_wiki(title),
               'text': filter_wiki(title),
               'pageid': pageid}
        _id += 1
        es.index(index=wiki_index,
                 doc_type='wiki',
                 body=doc,
                 id=_id)


def wiki_search(query):
    es = Elasticsearch()
    return es.search(index='wiki_index',
                     doc_type='wiki',
                     q=query)['hits']['hits'][:20]


if '__main__' == __name__:
    wiki_file = ('/Users/rivinek/Downloads/'
                 'enwiki-latest-pages-articles.xml.bz2')
    # wiki_indexer(wiki_file)
    es = Elasticsearch()
    print es.count(index='wiki_index', doc_type='wiki')
    # es.indices.delete(index='_all')
    # print wiki_search()

    # indexer(es, '/Users/rivinek/Documents/Projects/')

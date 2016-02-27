import requests
import requesocks


def create_connection():
    session = requesocks.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    print session.get("http://httpbin.org/ip").text
    print requests.get("http://httpbin.org/ip").text


if __name__ == '__main__':
    create_connection()

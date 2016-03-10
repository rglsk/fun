import requests

from shared.models import Link


def crawl_robots():
    links = Link.get_all()[:10]
    for link in links:
        _link = link.url if link.url.endswith('/') else link.url + '/'
        try:
            response = requests.get(_link + 'robots.txt')
        except requests.exceptions.SSLError:
            continue
        if response.status_code == 200:
            link.robot_file = response.text
            link.save()


def find_interesting():
    print Link.find_interesting()

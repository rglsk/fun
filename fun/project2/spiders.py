from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider

from shared.models import Link


class LinkSpider(CrawlSpider):
    name = "link_spider"
    allowed_domains = ['*']
    start_urls = ["http://www.alexa.com/topsites/countries;{}/PL".format(nr)
                  for nr in xrange(0, 20)] + [
                    "http://polskiestrony.top-100.pl/",
                  ]

    def parse(self, response):
        #odp, common_crowl, slownik i doklejam .pl
        links = []
        # next_page = response.xpath('//a[@class="next"]/@href').extract()
        # if next_page and next_page[0]:
        #     domain = urlparse.urljoin(response.url, '/')
        #     next_page = domain + next_page[0][1:]
        # else:
        #     next_page = None

        for sel in response.xpath('//div'):
            link = sel.xpath('a/@href').extract()
            if link and link[0].startswith('http'):
                links.append(link[0])

        for sel in response.xpath('//a'):
            title = sel.xpath('text()').extract()
            if title and len(title[0].split('.')) == 2:
                link = 'http://' + title[0]
                links.append(link)

        Link.save_many(links)


def crawl_links(save_to_file=True):
    process = CrawlerProcess({
        'USER_AGENT': 'I like Dragon Ball.'
    })

    process.crawl(LinkSpider)
    process.start()

    if save_to_file:
        Link.dump_to_file()

    for x in Link.get_all():
        print x.url

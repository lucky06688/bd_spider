import os
import uuid
import scrapy
from scrapy.http import HtmlResponse, TextResponse
from bd_spider import settings

DEFAULT_DD = os.path.join(settings.PROJECT_ROOT, 'result')


class BdSpider(scrapy.Spider):
    name = "bd"

    def __init__(self, wd='bilibili', pn=3, dd=DEFAULT_DD, **kwargs):
        super().__init__(**kwargs)
        self.wd = wd
        self.dd = dd
        self.start_urls = ['https://www.baidu.com/s?wd={}&pn={}'.format(wd, pn)
                           for pn in [x * 10 for x in range(int(pn))]]
        self.logger.info(self.start_urls)

    def parse(self, response):
        urls = response.xpath('//h3/a[1]/@href')
        for url in urls:
            yield response.follow(url, callback=self.save)

    def save(self, response):
        """Save the response(only html/text) as local file"""
        body = response.body
        if isinstance(response, HtmlResponse):
            ext = '.html'
        elif isinstance(response, TextResponse):
            ext = '.txt'
        else:
            self.logger.info('Unsupported response type: {}'
                             .format(response.__class__.__name__))
        fname = self.wd + '_' + uuid.uuid4().hex + ext
        dd = getattr(self, 'dd', DEFAULT_DD)
        if not os.path.isdir(dd):
            os.mkdir(dd)
        fd = os.open(os.path.join(dd, fname), os.O_RDWR | os.O_CREAT)
        os.write(fd, body)
        os.close(fd)






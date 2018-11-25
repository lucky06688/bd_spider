import os
import uuid
import scrapy
from scrapy.http import HtmlResponse, TextResponse
from bd_spider import settings

default_dd = os.path.join(settings.PROJECT_ROOT, 'result')

class BdSpider(scrapy.Spider):
    name = "bd"

    def __init__(self, wd='bilibili', pn=3, **kwargs):
        super().__init__(**kwargs)
        self.wd = wd
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
        dd = getattr(self, 'dd', default_dd)
        if not os.path.isdir(dd):
            os.mkdir(dd)
        fd = os.open(os.path.join(dd, fname), os.O_RDWR | os.O_CREAT)
        os.write(fd, body)
        os.close(fd)






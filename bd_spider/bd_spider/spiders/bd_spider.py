import os
import uuid
import scrapy
from scrapy.http import HtmlResponse, TextResponse
from bd_spider import settings

DEFAULT_DD = os.path.join(settings.PROJECT_ROOT, 'result')


class BdSpider(scrapy.Spider):
    name = "bd"
    type_dict = {
        'webpage': {
            'subdomain': 'www',
            'path': 's',
            'parameters': {
                'keyword': 'wd',
                'pageNumber': 'pn'
            }
        },
        'news': {
            'subdomain': 'news',
            'path': 'ns',
            'parameters': {
                'keyword': 'word',
                'pageNumber': 'pn'
            }
        }
    }

    def __init__(self, wd='bilibili', pn=3, dd=DEFAULT_DD, tp='webpage', **kwargs):
        super().__init__(**kwargs)
        self.wd = wd
        self.dd = dd
        self.tp = tp
        type_dict = __class__.type_dict
        type_obj = type_dict.get(tp, type_dict['webpage'])
        subdomain = type_obj['subdomain']
        path = type_obj['path']
        param_keyword = type_obj['parameters']['keyword']
        param_page_number = type_obj['parameters']['pageNumber']
        self.start_urls = ['https://{}.baidu.com/{}?{}={}&{}={}'.
                               format(subdomain, path, param_keyword, wd, param_page_number, pn)
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
            return
        fname = self.tp + '_' + self.wd + '_' + uuid.uuid4().hex + ext
        dd = self.dd
        if not os.path.isdir(dd):
            os.mkdir(dd)
        fd = os.open(os.path.join(dd, fname), os.O_RDWR | os.O_CREAT)
        os.write(fd, body)
        os.close(fd)

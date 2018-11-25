from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from bd_spider.spiders.bd_spider import BdSpider
from bd_spider.spiders.bd_spider import DEFAULT_DD

runner = CrawlerRunner(get_project_settings())

d = runner.crawl(BdSpider, wd='pornhub', pn=3, dd=DEFAULT_DD)
d.addBoth(lambda _: reactor.stop())
reactor.run()

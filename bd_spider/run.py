from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from bd_spider.spiders.bd_spider import BdSpider

# configure_logging()
runner = CrawlerRunner(get_project_settings())

d = runner.crawl(BdSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()
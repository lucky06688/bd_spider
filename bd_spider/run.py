import argparse
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from bd_spider.spiders.bd_spider import BdSpider
from bd_spider.spiders.bd_spider import DEFAULT_DD

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download Baidu search results given Keyword and page number.')
    parser.add_argument('-w', '--word', type=str, help='Keyword', default='bilibili')
    parser.add_argument('-p', '--page', type=int, help='Page number', default=3)
    parser.add_argument('-d', '--des', type=str, help='Destination directory', default=DEFAULT_DD)
    parser.add_argument('-t', '--type', type=str, help='Type', default='webpage')
    args = parser.parse_args()
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(BdSpider, wd=args.word, pn=args.page, dd=args.des, tp=args.type)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

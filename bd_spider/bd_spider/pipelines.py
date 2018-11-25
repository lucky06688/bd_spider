# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline

class BdSpiderPipeline(FilesPipeline):
    # def handle_redirect(self, file_url):
    #     response = requests

    def process_item(self, item, spider):
        return item

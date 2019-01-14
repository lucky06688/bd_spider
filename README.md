# 爬取百度搜索结果
指定关键词和页数，将百度搜索到的网页的源码下载并保存为HTML/text文件

## Requirements ##
- Python3.6
- Scrapy

Installation 
------
    pip install -r requirements.txt
    
Getting Started
------
三个参数:
- wd:  关键词 (默认为 bilibili)
- pn:  页数 (默认为 3)
- dd:  结果的保存路径 (默认为 ./bd_spider/result/)
- ty:  搜索类型 (目前只支持*网页*和*新闻*)
    1. webpage: 网页 (默认)
    2. news: 新闻

Example:

    cd bd_spider      
    scrapy crawl bd -a wd="文法解析器" -a pn=1000 -a dd="/path/to/store/files/" -a tp="webpage"
    
Or:
 
    cd bd_spider
    python run.py -w "文法解析器" -p 1000 -d "/path/to/store/files/" -t "news"
            
------
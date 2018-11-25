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
- wd:  关键词
- pn:  页数
- dd:  结果的保存路径

Example:

    cd bd_spider      
    scrapy crawl bd -a wd="文法解析器" pn=1000 dd="/path/to/store/files/"
    
Or:
 
    cd bd_spider
    python run.py -w "文法解析器" -p 1000 -d "/path/to/store/files/"
            
------
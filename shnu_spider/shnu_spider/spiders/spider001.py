import scrapy
from shnu_spider.items import ShnuSpiderItem

class Spider001Spider(scrapy.Spider):
    name = "spider001"
    allowed_domains = ["www.shnu.edu.cn"]
    start_urls = ["https://www.shnu.edu.cn/tzggsy/"]

    def parse(self, response):
        item=ShnuSpiderItem()
        titles = [each.extract() for each in response.xpath('//*[@id="wp_news_w6"]/ul/li/span[1]/a/text()')]  # 提取新闻标题
        item['title'] = titles  # 保存提取到的数据

        return item


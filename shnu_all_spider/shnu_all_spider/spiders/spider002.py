import scrapy
from scrapy.http import Request
from shnu_all_spider.items import  ShnuAllSpiderItem
from requests_html import HTML
class Spider002Spider(scrapy.Spider):
    name = "spider002"
    allowed_domains = ["xxjd.shnu.edu.cn"]
    start_urls = ["http://xxjd.shnu.edu.cn/27065/list.htm"]
    # 设置下载延迟时间
    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # 在发出每个请求之前等待1秒
    }

    def parse(self, response):
        #number = int(response.xpath('//*[@id="wp_paging_w6"]/ul/li[3]/span[1]/em[2]').extract()[0])             # 页面数量
        number =3
        url_all1 = [f'http://xxjd.shnu.edu.cn/27065/list{i}.htm' for i in range(1, number+1)]    # 所有页面url


        for url in url_all1:
            yield Request(url, callback=self.parse_url, dont_filter=True)     # 访问各页面url


    def parse_url(self, response):
        urls = response.xpath('//*[@id="wp_news_w6"]/ul/li/span[1]/a/@href').extract()    # 各新闻页面中的所有新闻标题的二次页面url

        urls=map(lambda x: 'http://xxjd.shnu.edu.cn'+x if '.cn' not in x else 'http://'+x,urls)
        for url_sub in urls:
            yield Request(url_sub, callback=self.parse_text, dont_filter=True)      # 访问各新闻的二级页面url

    def parse_text(self, response):
        item = ShnuAllSpiderItem()

        item['title'] = response.xpath('//*[@id="d-container"]/div/div/div/h1/text()').extract()  # 新闻标题
        item['author'] = response.xpath('//*[@id="d-container"]/div/div/div/p/span[1]/text()').extract()   # 新闻人
        item['times'] = response.xpath('//*[@id="d-container"]/div/div/div/p/span[2]/text()').extract()      # 新闻发布时间
        item['view_count'] = response.xpath('///*[@id="d-container"]/div/div/div/p/span[3]/span/text()').extract()   # 新闻浏览次数
        #item['text'] = '\n'.join(response.xpath('//*[@id="d-container"]/div/div/div/div/div/div/p/text()').extract())    # 新闻文本
        #print('Prof.Li',item)
        return item
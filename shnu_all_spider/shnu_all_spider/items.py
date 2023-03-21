# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShnuAllSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author= scrapy.Field()
    times = scrapy.Field()
    view_count = scrapy.Field()
    #text = scrapy.Field()

import pandas as pd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ShnuAllSpiderPipeline:
    def process_item(self, item, spider):
        data = pd.DataFrame(dict(item))  # 将数据转为DataFrame结构
        data.to_csv('d:/new_all.csv', mode='a+', index=None, encoding='utf-8-sig', header=None)

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class TestdemoPipeline(object):
    #会在爬虫开启的时候执行
    def open_spider(self,spider):
        self.f = open('Movies.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        #转换成字符串
        data = json.dumps(dict(item))+'\n'
        self.write(data)
        return item

        
    #会在爬虫结束的时候执行
    def close_spider(self,spider):
        self.f.close()

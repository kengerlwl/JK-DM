import os

import requests
import scrapy
# from TestDemo.items import TestdemoItem
import re
import numpy
import fake_useragent
from fake_useragent import UserAgent

class paJs:

    def __init__(self):
        

        self.url = "http://www.imomoe.io/playdata/2/7426.js?1393.1"

        self.r = ''
        self.list = []


    def start(self):
        self.r = requests.get(self.url)

        txt = ''+self.r.text
        arr = txt.split('\'')
        count =0
        for index,val in enumerate(arr):
            ans = re.match('.u.*flv$',val)

            if ans!=None:
                count = count +1
                # print(index)
                # print(val)
                arr1 = val.split('$')
                s = ''.join(arr1[0])
                print(s)
                s=s.encode('utf-8')
                s = s.decode('unicode_escape')
                self.list.append([s,arr1[1]])

        print(self.list)
        print(count)
    
    def save(self, path):
            numpy.save("filename.npy",self.list)
    
    def load(self, path):
        a = numpy.load("filename.npy")

        self.list = []

        for item in a:
            self.list.append([item[0], item[1]])

        print(self.list)



class Minimp4Spider(scrapy.Spider):

    def __init__(self, category='', **kwargs):
        super().__init__(**kwargs)  # python3
        self.start_urls = [self.url]



    name = 'yh'
    allowed_domains = ['imomoe.io/']
    


    def parse(self, response):
        #返回的是一个列表
        print(response.request.headers)
        urls=response.css('.movurl').css('a[href]').css('a::attr(href)')
        url1 ='http://www.imomoe.io'+ urls[0].extract()
        print(url1)

        yield scrapy.Request(url1, callback=self.getContent,dont_filter=True)
        print('over/nover')

        
    #主要用于获取播放地址的js
    def getContent(self,response):
        #实例化
        print('asdfkhaksdjfhksjdhfkjsahdkfhaskdjfhkasjdhfksajdhfkjahsdkfjhaksjhdfksjhdfkjshdkfhkasjdhfksdjhfkjahsdfkjhaskdhfksdhfkhsdkfjhsd')
        print(response.request.headers)

        scripts = response.css('script')
        for script in scripts:
            ans = re.match('<script type="text/javascript" src="/playdata.*',script.extract())
            if ans!=None:
                url ='http://www.imomoe.io'+ script.css('script::attr(src)').extract()[0]
                print(url)

               # 开始爬 测试时用本地数据
                pa = paJs()
                pa.url = url
                pa.start()
                pa.save('adf')

                
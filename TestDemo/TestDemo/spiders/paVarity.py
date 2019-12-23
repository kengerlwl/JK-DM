# # -*- coding: utf-8 -*-
# import os

# import requests
# import scrapy
# # from TestDemo.items import TestdemoItem
# import re
# import numpy
# import fake_useragent
# from fake_useragent import UserAgent

# class paJs:

#     def __init__(self):
        

#         self.url = "http://www.imomoe.io/playdata/2/7426.js?1393.1"

#         self.r = ''
#         self.list = []


#     def start(self):
#         self.r = requests.get(self.url)

#         txt = ''+self.r.text
#         arr = txt.split('\'')
#         count =0
#         for index,val in enumerate(arr):
#             ans = re.match('.u.*flv$',val)

#             if ans!=None:
#                 count = count +1
#                 # print(index)
#                 # print(val)
#                 arr1 = val.split('$')
#                 self.list.append([arr1[0],arr1[1]])

#         print(self.list)
#         print(count)
    
#     def save(self, path):
#             numpy.save("filename.npy",self.list)
    
#     def load(self, path):
#         a = numpy.load("filename.npy")

#         self.list = []

#         for item in a:
#             self.list.append([item[0], item[1]])

#         print(self.list)




    
# def save(list, path, ):
#             numpy.save(path+".npy",list)
    
# def load(list, path):
#         a = numpy.load(path+".npy")

#         list = []

#         for item in a:
#             list.append([item[0], item[1]])

#         print(list)

# class Minimp4Spider(scrapy.Spider):

#     def __init__(self, category='', **kwargs):
#         super().__init__(**kwargs)  # python3
#         self.start_urls = [self.url]
#         self.list = []



#     name = 'paV'
#     allowed_domains = ['imomoe.io/']
    


#     def parse(self, response):
#         #返回的是一个列表
#         print(response.request.headers)
#         count= 0
#         urls=response.css('p').css("a[href^='/']")
#         for url in urls:
#             if (count ==10):
#                 u = url.css('a::attr(href)').extract()

#                 ans = u[0].encode('gbk')
#                 text = str(ans)
#                 text = text.replace('\\x','%' )
#                 text = text.replace('\'', '')
#                 t = list(text)
#                 t.pop(0)
#                 text = ''.join(t)
#                 u= text



                
#                 print('asdfkjhasdkfjhkasjdhfkasdhjfkjsahdfkjhsadjfhskajdhfksajdhfkajsdhfkjashkfjhskdhfkasjhdfkjhaksdjfhkasjhdfkasjhdfkjhsdfjhsakdfjhakslhjfkasjhdkfjsdh')
#                 u = 'http://www.imomoe.io'+u
#                 name = url.css('a::text')[0].extract()
#                 print(name)

#                 yield scrapy.Request(u,meta={'name': name}, callback=self.getContent,dont_filter=True)
            
#             # print(count)
#             # print(url)
#             count= count +1





#         # print(urls)
#         # url1 ='http://www.imomoe.io'+ urls[0].extract()
#         # print(url1)

#         print('over/nover')


#     def getContent(self, response):
#         item = response.meta['name']
#         print(item)

#         print(response.request.headers)
#         print('adhfkajshdfkjhasdkjfhksjhdfkahsdkfjhsdkjfhkasjhfkjshdfkjhasdjfhaksjhfksajdhkfjshdkfjsd')
#         ans = response.css('div.pics').css('a')
#         for temp1 in ans:
#             temp2 = temp1.css('img')
#             if temp2 != []:
#                 print(temp1.extract())

#                 print(temp1.css('a::attr(href)'))
#                 print(temp2.css('img::attr(src)'))
#                 print(temp2.css('img::attr(alt)'))
#                 u = temp1.css('a::attr(href)').extract()
#                 jpg = temp2.css('img::attr(src)').extract()
#                 na = temp2.css('img::attr(alt)').extract()
#                 if na !=[]:
#                     self.list.append([u, jpg, na])
#         print(self.list)
#         save(self.list, item)



            

    




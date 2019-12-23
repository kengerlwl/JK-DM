from django.shortcuts import render
from django.shortcuts import render
import numpy
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
import sys
import json
import os
from scrapy import cmdline
sys.path.append("/home/lwl/Study/code/Python/django/mysite-master/yh")
from payh import search
# Create your views here.
import load
import random

def loadU(request):
    f = open('/home/lwl/Study/code/Python/django/mysite-master/yh/url.txt')
    ans = f.read()
    f.close()
    return HttpResponse(ans)



def saveU(request):
    url =request.GET.get('url',default="")
    f = open('/home/lwl/Study/code/Python/django/mysite-master/yh/url.txt','w')
    f.write(url)
    f.close()
    return HttpResponse('ok')


def va(request):
    keyW = request.GET.get('varity',default='热血')

    list=[]
    list = load.load(list, keyW)
    random.shuffle(list)
    resp = {'data': list}
    return HttpResponse(json.dumps(resp), content_type="application/json")



def searchDm(request):
    keyW = request.GET.get('keyW',default='110')

    s = search()
    s.keyWord = keyW
    s.main()
    print(s.searchList)
    resp = {'data': s.searchList}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def viewDm(request):#不以mp4结尾的动漫，就使用https://api.xiaomingming.org/cloud/mp4.php?vid=相应网址的  这个api
    keyW = request.GET.get('keyW',default='110')
    url = keyW
    print(url)

    #爬虫
    os.system('cd /home/lwl/Study/code/Python/django/mysite-master/yh/yuanma-master/TestDemo/TestDemo/spiders&&scrapy crawl yh -a url=' + url)
    # os.system("scrapy crawl yh -a url="+url)

    # os.system("cd /home/lwl/Study/code/Python/scrapy/yuanma-master/TestDemo/TestDemo/spiders\n scrapy crawl yh -a url=" + url)

    a = numpy.load("/home/lwl/Study/code/Python/django/mysite-master/yh/yuanma-master/TestDemo/TestDemo/spiders/filename.npy")

    list = []

    for item in a:
            list.append([item[0], item[1]])


    resp = {'data':list}

    # cmdline.execute("scrapy crawl yh -a url=http://www.imomoe.io/view/7714.html".split())
    return HttpResponse(json.dumps(resp), content_type="application/json")




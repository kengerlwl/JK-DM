import requests#爬虫的请求库
import os#系统的一个库
#http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=52&marry=1&page=1
#http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=52&startheight=161&endheight=170&marry=1&education=10&salary=2&page=1
#查询条件  年龄  性别 城市  身高
def age():
    age=int(input("请输入期望寻找的对象的年龄(如20)"))
    if 21 <=age <=30:
        startage=21
        endage=30
    else :
         startage=31
         endage=40

    return startage,endage
def gender():
    gender=input("请输入期望寻找对象的性别(如:女)")
    if gender=='男':
        gender=1
    else:
        gender=2
    return gender
def city():
    city=input("请输入期望寻找对象的城市:(如北京)")
    if city=='北京':
        city=52
    elif city=='深圳':
        city=77
    else:
        print("抱歉没有找到，请重新输入")
        city()
def shengao():
    shengao=int(input("请输入期望寻找对象的身高(如160)"))
    if 0<=shengao<=150:
        startshengao=0
        endshenggao=150
    elif 160<=shengao<=170:
        startshengao=160
        endshenggao=170
    elif 171<=shengao<=180:
        startshengao=171
        endshenggao=180
    return startshengao,endshenggao
#综合函数
def start():
    print("请输入你的筛选条件,开始你的姻缘")
    startage,endage=age()
    xingbie=gender()
    chenshi=city()
    startshengao,endshenggao=shengao()
    #下载十页数据    range()包左不包右
    for i in range(1,11):

        json=get_one(i,startage,endage,xingbie,chenshi,startshengao,endshenggao)
        #要获取的信息在json['data']['list']中
        for item in json['data']['list']:
            save_image(item)
def get_one(page,startage,endage,xingbie,chenshi,startshengao,endshenggao):
    #反爬措施  让程序模拟浏览器  headers
    heads={
        "Referer":"http://www.lovewzly.com/jiaoyou.html",
        "User-Agent":"Mozilla/5.0(Windows NT 10.0;…)Gecko/20100101Firefox/56.0"
    }
    baseurl='http://www.lovewzly.com/api/user/pc/list/search?startage={}&endage={}&gender={}&cityid={}&startheight={}&endheight={}&marry=1&education=10&salary=2&page={}'.format(startage,endage,xingbie,chenshi,startshengao,endshenggao,page)
    while True:
        try:
            #得到页面的响应 200 为成功  返回一个json数据
            response=requests.get(url=baseurl)
            if response.status_code==200:
                print(response.json())
                return response.json()
        except:
            return None
    # print(url)
def save_image(item):
    #如果没有images这个文件夹的话  系统会自动创建
    if not os.path.exists('images'):
        os.mkdir('images')
    #获取图片的下载地址
    image_url=item['avatar']
    response=requests.get(image_url)
    if response.status_code==200:
        #下载的路径
        file_path='images/{}.jpg'.format(item['username'])
        if not os.path.exists(file_path):
            print("正在获取%s的信息"%item['username'])
            # "wb" 存储为一个二进制文件    保存图片用request.content
            with open(file_path,'wb') as f:
                f.write(response.content)
        else:
            print("已经保存过当前图片")

if __name__ == '__main__':
    start()
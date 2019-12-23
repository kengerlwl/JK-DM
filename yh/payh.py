import requests
from bs4 import BeautifulSoup
import sys
import io

import fake_useragent
from fake_useragent import UserAgent


sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
print(sys.getdefaultencoding())

class search:

    def __init__(self):
        self.searchList = []
        self.keyWord='东京'
    def main(self):



        #请求头

        headers = {
        'User-Agent': ''+UserAgent().random,
        'Accept-Encoding': 'gzip, deflate', 
        'Accept': 'zh-CN,zh;q=0.9', 
        'Connection': 'keep-alive', 
        'Cookie': 'ASPSESSIONIDQQATSSBA=MKMENFHBIOEFODLCFBIFELDF; security_session_verify=df7db2016d91fe97eff1fd14adec0c5e', 
        'Content-Length': '15', 
        'Content-Type': 'application/x-www-form-urlencoded',
        

    }



        resp = requests.get('http://www.imomoe.io/list/1.html')
        # 判断服务器返回的状态码是不是200（表示成功）
        if resp .status_code != 200:
            return
        # 获取返回对象里的cookies   
        cookies = resp.cookies.get_dict()
        soup = BeautifulSoup(resp.text,'lxml')
        # 得到csrf
        # 把提交表单的数据放在字典
        data = {
            'searchword': self.keyWord.encode('gb2312')#要注意这边的·编码不能直接复制chorme那的模式，就是这种最本质的解码才是
        }
        # 发出提交表单的post请求
        resp = requests.post('http://www.imomoe.io/search.asp', data=data,
                            cookies=cookies, headers = headers)
        print(resp.encoding)
        ans = resp.text
        ans = ans.encode('ISO-8859-1')
        ans = ans.decode('gb2312','ignore')
        html = BeautifulSoup(ans, 'html.parser')
        list1 = html.find_all(class_ ='pics')
        count =0
        for li in list1:
            temp = li.find_all(attrs={ 'target':"_blank"})
            if(temp!=[]):
                for result in temp:
                    t = result.find_all('img')
                    if (t!=[]):
                        # print(result)
                        # print(result['href'])
                        # print(t[0]['alt'])
                        self.searchList.append(['http://www.imomoe.io'+result['href'], t[0]['alt'], t[0]['src']])
                        count= count+1
        print(count)
        print(self.searchList)
        print(resp.request.headers)


if __name__ == '__main__':
    s= search()
    s.keyWord = '东京'

    s.main()
    print(s)


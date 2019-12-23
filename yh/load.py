#关于分类的load函数
import numpy
import sys
sys.path.append("/home/lwl/Study/code/Python/django/mysite-master/yh")

def save(list, path, ):
            numpy.save('/home/lwl/Study/code/Python/django/mysite-master/yh/npy/' +path+".npy",list)
    
def load(list, path):
        a = numpy.load('/home/lwl/Study/code/Python/django/mysite-master/yh/npy/' +path+".npy")
        a = a.tolist()
        list = []

        for item in a:
            list.append(['http://www.imomoe.io'+item[0][0],  item[1][0], item[2][0]])

        return(list)

# list=[]
# list =load(list, '热血')
# print(list)

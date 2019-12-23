from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django import forms
from cmdb import models
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request):
    if request.method=="POST":
        file_obj = request.FILES.get("file")
        test = request.FILES.get('type')
        print(test)
        print(file_obj)

        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)

        return HttpResponse("ok")
    return  HttpResponse("error")

# Create your views here.
def bili(request):
    url = request.GET.get('url',default='110')
    ans = '更改后'+url
    return  HttpResponse(ans)


def main(request):
    # num = num+1
    # print(num)
    return render(request, "main.html", )


def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        test = "test"
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password, test=test)

    # 从数据库读取数据
    user_list = models.UserInfo.objects.all()
    return render(request, "login.html", {"data": user_list})


def test(request):
    return HttpResponse("hello kjgjhjh world")




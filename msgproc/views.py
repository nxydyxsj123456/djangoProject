import re

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone

from msgproc import 工匠职聘短信登入, 工匠职聘发短信

from msgproc.models import gjzpCookie


def index(request):

    lists = gjzpCookie.objects.all()

    for xxx in lists:
        print(xxx)
    return HttpResponse('Hello World!')

def addMsg(request):
    phone = request.GET.get("phone")
    msg = request.GET.get("msg")
    print(phone)
    print(msg)
    accounts = [
        {
            "user": "9496626@qq.com",  # 账户
            "password": "nixinyu10010"  # 密码
        }
    ]
    if "工匠职聘" in msg:
        pattern = re.compile(r'您的验证码是(\d{6})')
        codes = pattern.findall(msg)
        ry = 工匠职聘短信登入.RainYun("user", "password")  # 实例
        ry.smsLogin(phone, codes[0])  # 登录
        if ry.signin_result :

            gjzp = gjzpCookie.objects.get(phone='15869171029')
            gjzp.content =ry.session_token
            gjzp.save()

    return HttpResponse("<p>数据添加成功！</p>")

def queryMsg(request):

    gjzps = gjzpCookie.objects.all()
    tmpstr=""
    for gjzp in gjzps:
        tmpstr+=gjzp.content+"&android\n"

    return HttpResponse(tmpstr)
def checktime(request):

    gjzps = gjzpCookie.objects.all()
    tmpstr=""
    for gjzp in gjzps:

        now = timezone.now()
        time_difference = now - gjzp.TimeStamp
        print(time_difference.days)
        if time_difference.days >= 3:
            print("相差3天或更多")
            ry = 工匠职聘发短信.RainYun("user", "password")  # 实例
            ry.sendSms(gjzp.phone)  # 登录
        else:
            print("没有相差3天")



    return HttpResponse(tmpstr)
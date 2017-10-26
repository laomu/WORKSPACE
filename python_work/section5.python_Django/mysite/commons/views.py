"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:公共视图处理函数模块
remark:web网站根网页视图处理定义
"""
from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from . import models

# -------------------------------
users_manage = models.Users.users_manage
# -------------------------------


# Create your views here.
def regist(request):
    """
    公共注册方法
    :param request:请求对象
    :return: 返回注册的结果页面[成功|失败]
    """
    if request.method == "GET":
        return render(request, "commons/regist.html", {})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            return render(request, "commons/regist.html", {"msg": "两次密码输入不一致"})

        try:
            users_manage.get(username=username)
            return render(request, "commons/regist.html", {"msg": "账号已经存在"})
        except:
            users_manage.create_obj(username=username, password=password, regist_time=datetime.now())
            return redirect(reverse("commons:login"), kwargs={"msg": "账号注册成功."})


def login(request):
    """
    公共用户登录方法
    :param request:请求对象
    :return: 返回登录的结果页面[成功|失败]
    """
    # 创建表单对象
    if request.method == "GET":
        return render(request, "commons/login.html", {})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = users_manage.find_single(username=username, password=password)
            request.session.set_expiry(0)
            request.session["login_user"] = user
            return redirect(reverse("commons:index"))
        except:
            return render(request, "commons/login.html", {"msg": "账号或者密码有误.."})


def index(request):
    """
    项目根首页
    :param request:请求对象
    :return: 返回首页页面渲染数据
    """
    if request.method == "GET":
        user = request.session.get("login_user")
        return render(request, "commons/index.html", {"user": user})


def logout(request):
    """
    安全退出：清除session和关联的cookie数据
    :param request:
    :return:
    """
    request.session.clear()
    return redirect(reverse("commons:index"))

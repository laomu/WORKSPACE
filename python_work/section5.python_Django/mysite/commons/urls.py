"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:公共模块路由配置
remark:涉及多个子模块公共使用的数据，处理方式定义在commons模块中
"""
from django.conf.urls import url

from . import views

app_name = "commons"

urlpatterns = [
    url(r'^regist/', views.regist, name='regist'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^.*$', views.index, name='index'),
]
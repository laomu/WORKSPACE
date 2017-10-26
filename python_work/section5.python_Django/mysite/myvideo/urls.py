"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:影视娱乐社区路由模块
remark:无
"""
from django.conf.urls import url

from . import views

app_name = "myvideo"

urlpatterns = [
    url("^(?P<vt_id>\d+)/vtlist/$", views.video_vtlist, name="vtlist"),
    url("^(?P<vdt_id>\d+)/vdtlist/$", views.video_vdtlist, name="vdtlist"),
    url("^(?P<v_id>\d+)/vdetail/$", views.video_detail, name="vdetail"),
    url("^(?P<v_id>\d+)/vplay/$", views.video_play, name="vplay"),
    url("^vsearch/$", views.video_search, name="vsearch"),
    url("^.*$", views.index, name="index"),
]
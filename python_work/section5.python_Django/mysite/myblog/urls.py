from django.conf.urls import url

from . import views

app_name = "myblog"

urlpatterns = [
    url(r'^alist/$', views.article_list, name="alist"),
    url(r'^(?P<a_id>\d+)/adetail/$', views.article_detail, name="adetail"),
    url(r'^.*$', views.index, name="index"),
]
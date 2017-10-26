"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:电商项目路由配置模块
remark:无
"""
from django.conf.urls import url

from . import views

app_name = "myshopping"

urlpatterns = [
    # 根据商品一级类型查看所有商品
    url(r"^(?P<type_id>\d+)/search_type/$", views.goods_search_type, name="search_type"),
    # 根据商品二级类型查看所有商品
    url(r"^(?P<type_id>\d+)/search_dtype/$", views.goods_search_dtype, name="search_dtype"),
    # 根据商品编号查询商品
    url(r"^(?P<goods_id>\d+)/detail/$", views.goods_detail, name="detail"),
    # 添加购物车
    url(r"^shopcart/$", views.shopcart, name="shopcart"),
    # 搜索商品
    url(r"^search_kw/$", views.goods_search_kw, name="search_kw"),
    # 首页展示
    url(r"^.*$", views.index, name="index"),
    # 结算
    # 查看所有订单
    # 查看单个订单详情
]

from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from . import models

# ---------------------
goodstype_manage = models.GoodsType.gt_manage
goodsdetailtype_manage = models.GoodsDetailType.gdt_manage
goodsimg_manage = models.GoodsImage.gi_manage
goods_manage = models.Goods.goods_manage
shopcart_manage = models.ShopCart.shopcart_manage


# Create your views here.
def index(request):
    """
    首页视图处理函数
    :param request:请求对象
    :return: 返回首页视图
    """
    # 查询所有键盘类型数据
    type_kb = goodstype_manage.find_single(id=1)# 一级类型
    type_detail_kb = goodsdetailtype_manage.find_multi(type=type_kb)# 二级类型
    goods_list_kb = goods_manage.find_multi(type__in = type_detail_kb)# 商品列表
    # 查询所有PC类型数据
    type_pc = goodstype_manage.find_single(id=3)
    type_detail_pc = goodsdetailtype_manage.find_multi(type=type_pc)
    goods_list_pc = goods_manage.find_multi(type__in = type_detail_pc)# 商品列表

    print(goods_list_kb)
    print(goods_list_pc)

    # 查询所有类型
    type_list = goodstype_manage.find_multi()

    # 返回首页页面，传递在页面中展示的数据
    return render(request, "myshopping/index.html", {"tl": type_list, "kb": goods_list_kb[0:2], "pc": goods_list_pc[0:2]})


def goods_search_kw(request):
    # 获取参数
    keyword = request.POST["search"]
    # 查询商品
    goods_list = goods_manage.find_multi(name__contains=keyword)
    return render(request, "myshopping/goods_list.html", {"gl": goods_list})


def goods_detail(request, goods_id):
    # 查询商品
    goods = goods_manage.find_single(id=goods_id)
    return render(request, "myshopping/goods_detail.html", {"goods": goods})


def goods_search_type(request, type_id):
    # 查询该类型对象
    type = goodstype_manage.find_single(id=type_id)
    # 查询所有二级类型
    dtype = goodsdetailtype_manage.find_multi(type=type)
    # 查询所有商品
    goods_list = goods_manage.find_multi(type__in = dtype)
    # 返回网页
    return render(request, "myshopping/goods_list.html", {"gl": goods_list})


def goods_search_dtype(request, type_id):
    # 查询所有商品
    goods_dtype = goodsdetailtype_manage.find_multi(id=type_id)
    goods_list = goods_manage.find_multi(type__in=goods_dtype)
    # 返回网页
    return render(request, "myshopping/goods_list.html", {"gl": goods_list})


def shopcart(request):
    if request.method == "GET":
        # 查询购物车中当前用户所有商品
        login_user = request.session.get("login_user")
        scgoods_list = shopcart_manage.find_multi(users=login_user)
        print(scgoods_list)
        return render(request, "myshopping/shopcart.html", {"gl": scgoods_list})

    elif request.method == "POST":
        # 获取购物车添加商品需要的参数[商品编号、购买数量]
        goods_id = request.POST["goods_id"]
        goods_count = request.POST["goods_count"]

        # 获取当前登录用户
        login_user = request.session.get("login_user")
        # 查询到具体商品
        goods = goods_manage.find_single(id=goods_id)

        # 创建购物车对象
        shopcart_manage.create_obj(deal_time=datetime.now(),\
                                   deal_price=goods.price,\
                                   deal_count=goods_count,\
                                   goods=goods,\
                                   users=login_user)
        # 返回路由
        return redirect(reverse("myshopping:shopcart"))

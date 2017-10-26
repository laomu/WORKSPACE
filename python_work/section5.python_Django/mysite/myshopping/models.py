"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:电商项目模型数据定义模块
remark:无
"""
from commons.models import Users
from django.db import models

from . import model_manage


# Create your models here.
class GoodsType(models.Model):
    """
    商品一级类型：键盘、鼠标、电脑....
    """
    id = models.AutoField(primary_key=True)  # 类型编号
    name = models.CharField(max_length=50)   # 类型名称
    desc = models.TextField()                # 类型描述

    gt_manage = model_manage.GoodsTypeManage()


class GoodsDetailType(models.Model):
    """
    商品二级类型：罗技、赛泰克...
    """
    id = models.AutoField(primary_key=True)     # 类型编号
    name = models.CharField(max_length=50)      # 类型名称
    desc = models.TextField()                   # 类型描述
    type = models.ForeignKey(GoodsType, on_delete=models.CASCADE) # 外键

    gdt_manage = model_manage.GoodsDetailManage()


class Goods(models.Model):
    """
    商品类型
    """
    id = models.AutoField(primary_key=True)# 商品编号
    name = models.CharField(max_length=50)# 商品名称
    price = models.FloatField()# 商品价格
    stock = models.IntegerField(default=0)# 商品库存
    type = models.ForeignKey(GoodsDetailType, on_delete=models.CASCADE)# 商品类型
    desc = models.TextField()# 商品描述

    # 管理器对象
    goods_manage = model_manage.GoodsManage()


class GoodsImage(models.Model):
    """
    商品对应展示图片
    """
    id = models.AutoField(primary_key=True)# 图片编号
    path = models.CharField(max_length=300)# 图片路径
    isdefault = models.BooleanField(default=False)# 是否默认
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)# 关联商品


    gi_manage = model_manage.GoodsImgManage()


class ShopCart(models.Model):
    """
    购物车类型
    """
    id = models.AutoField(primary_key=True)# 购物商品编号
    deal_time = models.DateTimeField()# 成交时间
    deal_price = models.FloatField()# 成交价格
    deal_count = models.IntegerField()# 成交数量
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

    shopcart_manage = model_manage.ShopcartManage()
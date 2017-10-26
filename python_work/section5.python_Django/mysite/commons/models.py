"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:公共模块应用，专门给其他模块提供基础服务
remark:公共类型类型
"""
from django.db import models

from . import model_manage


# Create your models here.
class Users(models.Model):
    """
    公共用户类型，其他所有子模块共同使用的基本用户信息
    """
    # 定义字段
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    regist_time = models.DateTimeField()
    remark = models.TextField()

    # 定义模型管理器
    users_manage = model_manage.UsersManage()
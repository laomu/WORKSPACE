"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:模型数据管理器类型模块
remark:提供公共类型对象的增伤改查操作管理器对象的定义
"""
from django.db import models


class BaseManage(models.Manager):
    """
    类型管理器对象基础类型，专门用于继承
    """
    def create_obj(self, **kw):
        """
        增加用户数据的方法
        :param kw: 增加用户的数据
        :return: 返回增加的用户对象
        """
        return self.create(**kw)

    def find_single(self, **kw):
        """
        根据条件查询单个对象数据
        :param kw: 查询条件
        :return: 返回查询到的用户
        """
        return self.get(**kw)

    def find_multi(self, **kw):
        """
        根据条件查询多个对象数据
        :param kw: 查询条件
        :return: 返回条件满足的多个用户
        """
        return self.filter(**kw)

    def update_obj(self, **kw):
        """
        根据传输的数据修改用户字段数据
        :param kw: 条件数据
        :return: 返回修改完成的用户
        """
        return self.update(**kw)

    def delete_obj(self):
        """
        删除用户对象数据
        :return: 返回删除的用户
        """
        return self.delete()


class UsersManage(BaseManage):
    """用户
    用户对象管理器类型
    """
    pass


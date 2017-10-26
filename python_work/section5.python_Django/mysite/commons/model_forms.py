"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:VO对象
remark:和网页中需要的数据一直的类型对象，主要进行数据验证、数据类型转换等操作
"""
from django import forms
from . import models


class UsersForm(forms.ModelForm):
    """
    定义一个由用户类型构建的表单对象：VO对象
    """
    class Meta:
        # 与models中的实体类建立关系
        model = models.Users
        fields = ['username', 'password']
        labels = {
            'username': '用户名',
            'password': '密码',
        },
        error_messages = {
            'username': {
                'required': '账号不能为空',
                'max_length': '账号长度不能超过18位',
                'min_length': '账号长度不能少于6位'
            }
        }

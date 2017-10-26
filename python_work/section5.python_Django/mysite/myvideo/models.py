"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:影视娱乐数据定义模块
remark:无
"""
from commons.models import Users
from django.db import models

from . import model_manage


# Create your models here.
class VideoType(models.Model):
    """
    视频一级类型
    """
    id = models.AutoField(primary_key=True)         # 视频类型编号
    name = models.CharField(max_length=50)          # 视频类型名称
    cover = models.ImageField(default="/static/myvideo/video/t_default.jpg")    # 封面
    remark = models.TextField()                     # 备注

    vt_manager = model_manage.VideoTypeManager()


class VideoDetailType(models.Model):
    """
    视频二级类型
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)  # 视频类型名称
    cover = models.ImageField(default="/static/myvideo/video/t_default.jpg")  # 封面
    remark = models.TextField()  # 备注

    type = models.ForeignKey(VideoType)# 所属一级类型

    vdt_manager = model_manage.VideoDetailTypeManager()


class Video(models.Model):
    """
    视频
    """
    id = models.AutoField(primary_key=True)         # 编号
    title = models.CharField(max_length=50)         # 标题
    path = models.CharField(max_length=200)         # 路径
    publish_time = models.DateTimeField()           # 上传时间
    cover = models.ImageField(default="/static/myvideo/video/v_default.jpg")    # 封面
    intro = models.TextField()                      # 视频介绍

    type = models.ForeignKey(VideoDetailType)        #详细二级类型
    user = models.ForeignKey(Users)                  # 所属用户

    v_manager = model_manage.VideoManager()

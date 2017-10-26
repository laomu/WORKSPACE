from django.db import models

from commons.models import Users

# Create your models here.
class Article(models.Model):
    """
    文章类型
    """
    id = models.AutoField(primary_key=True) # 编号
    title = models.CharField(max_length=50)  # 标题
    content = models.TextField()        # 内容
    publish_time = models.DateTimeField()   # 发布时间
    click_count = models.IntegerField() # 阅读次数

    users = models.ForeignKey(Users, on_delete=models.CASCADE)    # 外键


class Comment(models.Model):
    """
    文章评论
    """
    id = models.AutoField(primary_key=True) # 主键
    publish_time = models.DateTimeField()   # 发布时间
    content = models.TextField()    # 评论内容

    users = models.ForeignKey(Users, on_delete=models.CASCADE)    # 外键，发布人
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 评论文章
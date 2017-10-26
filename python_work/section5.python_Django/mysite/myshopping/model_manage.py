"""
author:牟文斌
version:V1.00
time:2017-10-20
desc:电商项目模型数据管理器定义模块
remark:无
"""
from commons.model_manage import BaseManage


class GoodsManage(BaseManage):
    """
    商品管理器对象
    """
    pass


class GoodsTypeManage(BaseManage):
    """
    商品一级类型管理器对象
    """
    pass


class GoodsDetailManage(BaseManage):
    """
    商品二级类型管理器对象
    """
    pass


class GoodsImgManage(BaseManage):
    """
    商品图片管理器对象
    """
    pass


class ShopcartManage(BaseManage):
    """
    购物车管理器对象
    """
    pass
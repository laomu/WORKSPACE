from django.shortcuts import render

from . import models

#---------------------------
v_manager = models.Video.v_manager
vt_manager = models.VideoType.vt_manager
vdt_manager = models.VideoDetailType.vdt_manager


# Create your views here.
def index(request):
    """
    首页视图处理函数
    :param request:
    :return:
    """
    # 加载首页视频展示
    # 所有视频类型
    vt = vt_manager.find_multi()

    # 动漫频道
    vt_dm = vt_manager.find_single(id=1)
    vdt_dm = vdt_manager.find_multi(type=vt_dm)
    video_dm = v_manager.find_multi(type__in = vdt_dm)
    # 游戏频道
    vt_game = vt_manager.find_single(id=3)
    vdt_game = vdt_manager.find_multi(type=vt_game)
    video_game = v_manager.find_multi(type__in=vdt_game)
    # 影视频道
    vt_ys = vt_manager.find_single(id=7)
    vdt_ys = vdt_manager.find_multi(type=vt_ys)
    video_ys = v_manager.find_multi(type__in=vdt_ys)

    # 返回首页
    return render(request, "myvideo/index.html", {"vt": vt,"v_dm": video_dm, "v_game": video_game, "v_ys": video_ys})


def video_vtlist(request, vt_id):
    """
    视频列表视图处理函数
    :param request:
    :return:
    """
    vt = vt_manager.find_single(id=vt_id)
    vdt = vdt_manager.find_multi(type=vt)
    video_list = v_manager.find_multi(type__in=vdt)
    return render(request, "myvideo/video_list.html", {"v_list": video_list})


def video_vdtlist(request, vdt_id):
    """
    视频列表视图处理函数
    :param request:
    :return:
    """
    vdt = vdt_manager.find_single(type=vdt_id)
    video_list = v_manager.find_multi(type=vdt)
    return render(request, "myvideo/video_list.html", {"v_list": video_list})


def video_search(request):
    """
    视频搜索视图处理函数
    :param request:
    :return:
    """
    kw = request.GET["keyword"]
    video_list = v_manager.find_multi(title__contains=kw)
    return render(request, "myvideo/video_list.html", {"v_list": video_list})


def video_detail(request, v_id):
    """
    视频详情视图处理函数
    :param request:
    :return:
    """
    video = v_manager.find_single(id=v_id)
    return render(request, "myvideo/video_detail.html", {"video": video})


def video_play(request,v_id):
    """
    视频播放处理函数
    :param request:
    :return:
    """
    video = v_manager.find_single(id=v_id)
    return render(request, "myvideo/video_play.html", {"video": video})


def video_upload(request):
    """
    上传视频
    :param request:请求对象
    :return: 返回上传结果
    """
    pass
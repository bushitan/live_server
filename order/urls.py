# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^check/member/$', CheckMember.as_view()), # 获取当前房间
    # url(r'^message/get_list/$', GetListCurrentMessage.as_view()), #获取当前房间的信息
]
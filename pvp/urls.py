# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^story/get_list/$', StoryGetList.as_view()), # 获取当前房间
    url(r'^room/create/$', RoomCreate.as_view()), # 获取当前房间
    url(r'^room/join/$', RoomJoin.as_view()), # 获取当前房间
    # url(r'^get/$', GetCurrentRoom.as_view()), # 获取当前房间
    # url(r'^get/cover/$', GetCurrentRoomCover.as_view()), # 获取当前房间
    # url(r'^get_list/app/$', GetListRoomByApp.as_view()), # 获取当前房间
    # url(r'^add/message/$', AddMessage.as_view()), # 获取当前房间
    # # url(r'^get/message/$', GetMessageByRoom.as_view()), # 获取当前房间
    # url(r'^check/teacher/$', CheckTeacher.as_view()), # 获取当前房间
    # # url(r'^message/get_list/$', GetListCurrentMessage.as_view()), #获取当前房间的信息
]
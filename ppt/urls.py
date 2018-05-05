# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^file/get_list/$', FileGetList.as_view()), # 获取当前房间


    url(r'^self/add/tag/$', SelfAddTag.as_view()), # 获取当前房间
    url(r'^self/get/tag/$', SelfGetTag.as_view()), # 获取当前房间
    url(r'^self/get/file/$', SelfGetFile.as_view()), # 获取当前房间

    url(r'^team/get/tag/$', TeamGetTag.as_view()), # 获取当前房间
    url(r'^team/check/$', TeamCheck.as_view()), # 获取当前房间
    url(r'^team/quit/$', TeamQuit.as_view()), # 获取当前房间
    url(r'^team/join/$', TeamJoin.as_view()), # 获取当前房间
    url(r'^team/get/roster_tag/$', TeamGetRosterTag.as_view()), # 获取当前房间
    url(r'^team/get/roster/$', TeamGetRoster.as_view()), # 获取当前房间


    # url(r'^room/create/$', RoomCreate.as_view()), # 获取当前房间
    # url(r'^room/join/$', RoomJoin.as_view()), # 获取当前房间
    # url(r'^member/check/$', MemberCheck.as_view()), # 获取当前房间
    # url(r'^get/$', GetCurrentRoom.as_view()), # 获取当前房间
    # url(r'^get/cover/$', GetCurrentRoomCover.as_view()), # 获取当前房间
    # url(r'^get_list/app/$', GetListRoomByApp.as_view()), # 获取当前房间
    # url(r'^add/message/$', AddMessage.as_view()), # 获取当前房间
    # # url(r'^get/message/$', GetMessageByRoom.as_view()), # 获取当前房间
    # url(r'^check/teacher/$', CheckTeacher.as_view()), # 获取当前房间
    # # url(r'^message/get_list/$', GetListCurrentMessage.as_view()), #获取当前房间的信息
]
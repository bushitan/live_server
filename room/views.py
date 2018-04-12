# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from lib.message import *
from action.live import *

# 获取当前房间
class GetCurrentRoom( ListView):
    def __init__(self):
        self.action_live = ActionLive()
        super(GetCurrentRoom,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _app_id = request.GET.get('app_id',"")
            _room = self.action_live.GetCurrentRoom(_app_id)
            _app = self.action_live.GetCurrentRoom(_app_id)
            _room_id = _room["room_id"]
            print _room
            # print self.action_live.GetMessageList(_room_id )
            # print self.action_live.CheckPusherUser(_app_id,_session)
            _dict = {
                'room_dict':_room,
                'app_dict':self.action_live.GetLiveUrlCurrentRoom(_app_id),
                'message_list':self.action_live.GetMessageList(_room_id ),
                "is_teacher":self.action_live.CheckPusherUser(_app_id,_session)
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 获取当前房间的封面，简介
class GetCurrentRoomCover( ListView):
    def __init__(self):
        self.action_live = ActionLive()
        super(GetCurrentRoomCover,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _app_id = request.GET.get('app_id',"")
            _room = self.action_live.GetCurrentRoom(_app_id)
            _dict = {
                'room_dict':_room,
                "is_teacher":self.action_live.CheckPusherUser(_app_id,_session)
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 获取APP下的房间列表
class GetListRoomByApp( ListView):
    def __init__(self):
        self.action_live = ActionLive()
        super(GetListRoomByApp,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _app_id = request.GET.get('app_id',"")
            _room_list = self.action_live.GetListRoomByApp(_app_id)
            _dict = {
                'room_list':_room_list
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 上传录制信息
class AddMessage( ListView):
    def __init__(self):
        self.action_live = ActionLive()
        super(AddMessage,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            print type( request.GET.get('is_teacher',"")), request.GET.get('is_teacher',"")
            _room_list = self.action_live.AddMessage(
                request.GET.get('session',""),
                room_id = request.GET.get('room_id',""),
                style = request.GET.get('style',""),
                # is_teacher = request.GET.get('is_teacher',""),
                text = request.GET.get('content',""),
                audio = request.GET.get('audio_url',""),
                image = request.GET.get('image_url',""),
            )
            _dict = {
                'msg':u"添加音频成功"
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )



#1v1房间，检测用户是否教师
class CheckTeacher( ListView):
    def __init__(self):
        self.action_live = ActionLive()
        super(CheckTeacher,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _dict = {
                'is_teacher':self.action_live.CheckTeacher(_session ),
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
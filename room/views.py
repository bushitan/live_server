# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from lib.message import *
from action.live import *

# 登陆
class GetCurrentRoom( ListView):
    def __init__(self):
        self.action_live = ActionLive()
        super(GetCurrentRoom,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            # _room_id = request.GET.get('room_id',"")
            _room = self.action_live.GetCurrentRoom()
            _room_id = _room["room_id"]
            _dict = {
                'dict_room':_room,
                'list_message':self.action_live.GetMessageList(_room_id )
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

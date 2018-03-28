# -*- coding: utf-8 -*-

from django.views.generic import ListView
from lib.message import *
from action.online import *
action_online = ActionOnline()
# 获取故事列表
class StoryGetList( ListView):
    def __init__(self):
        super(StoryGetList,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _app_id = request.GET.get('app_id',"")
            _stage_list = action_online.GetListStage()
            _dict = {
                'stage_list':_stage_list,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 创建房间
class RoomCreate( ListView):
    def __init__(self):
        super(RoomCreate,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            # _app_id = request.GET.get('app_id',"")
            _key , _room_config = action_online.CreatePvpRoom(_session)
            _dict = {
                'room_key':_key,
                'room_config':_room_config,
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 加入房间
class RoomJoin( ListView):
	def __init__(self):
		super(RoomJoin,self).__init__()
	def get(self, request, *args, **kwargs):

		_session = request.GET.get('session',"")
		_room_key = request.GET.get('room_key',"")
		_is_alive , _room_config = action_online.JoinPvpRoom(_room_key)
		_dict = {
			'is_alive':_is_alive,
			'room_config':_room_config,
		}
		return MESSAGE_RESPONSE_SUCCESS(_dict)
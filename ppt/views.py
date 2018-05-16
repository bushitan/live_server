# -*- coding: utf-8 -*-

from django.views.generic import ListView
from lib.message import *
from action.online import *
from action.tag import *
from action.file import *
from action.team import *
from action.room import *
action_online = ActionOnline()
action_news = ActionTag()
action_file = ActionFile()
action_team = ActionTeam()
action_room = ActionRoom()

import time
import datetime

# 获取故事列表
class FileGetList( ListView):
    def __init__(self):
        super(FileGetList,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _app_id = request.GET.get('app_id',"")
            _ppt_list = action_online.GetListPPTFile(_session)
            _dict = {
                'ppt_list':_ppt_list,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)



# 创建房间
class RoomAdd( ListView):
    def __init__(self):
        super(RoomAdd,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _config_dict = action_room.Add(_session)

            _dict = {
                'config_dict':_config_dict,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 注销房间
class RoomDelete( ListView):
    def __init__(self):
        super(RoomDelete,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            action_room.Delete(_session)
            _dict = {
                'msg':"删除成功",
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 检测房间是否存在
class RoomCheck (ListView):
    def __init__(self):
        super(RoomCheck,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
        #     _session = request.GET.get('session',"")
            _host_name = request.GET.get('host_name',"")
            _check_dict = action_room.Check(_host_name)
            _dict = {
                'check_dict':_check_dict,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)




## 我的SELF

## 我的SELF
# 根据标签获取图片
class SelfGetTag( ListView):
    def __init__(self):
        super(SelfGetTag,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _tag_list = action_news.GetListBySession(_session)
            _dict = {
                'tag_list':_tag_list,
                # 'tag_list':[],
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 添加标签
class SelfAddTag( ListView):
    def __init__(self):
        super(SelfAddTag,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _tag_name = request.GET.get('tag_name',"")
            _tag_list = action_news.AddBySession(_session,_tag_name)
            _dict = {
                'tag_list':_tag_list,
                # 'tag_list':[],
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 根据标签获取图片
class SelfGetFile( ListView):
    def __init__(self):
        super(SelfGetFile,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _tag_id = request.GET.get('tag_id',"")
            _file_list = action_file.GetListByTag(_tag_id)
            _dict = {
                'file_list':_file_list,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

FILE_KEY_HASH = {}
# 上传图片，获取token
class SelfUploadToken( ListView):
    def __init__(self):
        super(SelfUploadToken,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _tag_id = request.GET.get('tag_id',"")
            _suffix = request.GET.get('suffix',"")  #后缀
            _token,_key,_hash = action_file.UploadGetToken(_session,_tag_id,_suffix)
            FILE_KEY_HASH[_key] = _hash
            _dict = {
                "token":_token,
                "key":_key,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 上传图片，获取token
class SelfUploadCallback( ListView):
    def __init__(self):
        super(SelfUploadCallback,self).__init__()
    def post(self, request, *args, **kwargs):
        # try:
            key = request.POST['key']
            if FILE_KEY_HASH.has_key(key):
                _user_id = FILE_KEY_HASH[key]["user_id"]
                _url = FILE_KEY_HASH[key]["url"]
                _tag_id = FILE_KEY_HASH[key]["tag_id"]
                _image = action_file.UploadComplete(_user_id,_url,_tag_id)
                _dict = {
                    'image_dict':_image,
                }
            else :
                raise # name不存在如果没有，直接返回网络错误
            return MESSAGE_RESPONSE_SUCCESS(_dict)

            # _hash = request.POST['hash']
            # w = request.POST['w']
            # h = request.POST['h']
            # duration = request.POST['duration']
            # fsize = request.POST['fsize']
            # vw = request.POST['vw']
            # vh = request.POST['vh']


## 我的SELF
# 根据标签获取图片
class TeamGetTag( ListView):
    def __init__(self):
        super(TeamGetTag,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _team_id = request.GET.get('team_id',"")
            print 213,_team_id
            _tag_list = action_news.GetListByTeam(_team_id)
            print 2132423
            _dict = {
                'tag_list':_tag_list,
                # 'tag_list':[],
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 根据标签获取图片
class TeamCheck( ListView):
    def __init__(self):
        super(TeamCheck,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _team_id = action_team.CheckBySession(_session)
            _dict = {
                'team_id':_team_id,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 根据标签获取图片
class TeamQuit( ListView):
    def __init__(self):
        super(TeamQuit,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _msg = action_team.Quit(_session)
            _dict = {
                'msg':_msg,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 根据标签获取图片
class TeamJoin( ListView):
    def __init__(self):
        super(TeamJoin,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _session = request.GET.get('session',"")
            _team_id = request.GET.get('team_id',"")
            _team_id = action_team.JoinBySession(_session,_team_id)
            _dict = {
                'team_id':_team_id,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)


# 根据标签获取图片
class TeamGetRosterTag( ListView):
    def __init__(self):
        super(TeamGetRosterTag,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _team_id = request.GET.get('team_id',"")
            print _team_id
            _roster_tag_list = action_team.GetRosterTag(_team_id)
            _dict = {
                'roster_tag_list':_roster_tag_list,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
# 根据标签获取图片
class TeamGetRoster( ListView):
    def __init__(self):
        super(TeamGetRoster,self).__init__()
    def get(self, request, *args, **kwargs):
        # try:
            _roster_tag_id = request.GET.get('roster_tag_id',"")
            _roster_list = action_team.GetRoster(_roster_tag_id)
            _dict = {
                'roster_list':_roster_list,
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
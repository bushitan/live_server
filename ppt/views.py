# -*- coding: utf-8 -*-

from django.views.generic import ListView
from lib.message import *
from action.online import *
from action.tag import *
from action.file import *
from action.team import *
action_online = ActionOnline()
action_news = ActionTag()
action_file = ActionFile()
action_team = ActionTeam()


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
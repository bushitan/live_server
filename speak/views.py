# -*- coding: utf-8 -*-

from django.views.generic import ListView
from lib.message import *
from action.daily import *
action_daily = ActionDaily()


# 获取当前房间的封面，简介
class GetThemeList( ListView):
    def __init__(self):
        super(GetThemeList,self).__init__()
    def get(self, request, *args, **kwargs):
            _dict = {
                'theme_list': action_daily.getThemeList(),
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 获取当前房间的封面，简介
class GetTheme( ListView):
    def __init__(self):
        super(GetTheme,self).__init__()
    def get(self, request, *args, **kwargs):
            _theme_id = request.GET.get('theme_id',"")
            _dict = {
                'theme_dict': action_daily.getTheme(_theme_id),
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)


# 获取七牛上传的token
class GetToken( ListView):
    def __init__(self):
        super(GetToken,self).__init__()
    def get(self, request, *args, **kwargs):
            _session = request.GET.get('session',"")
            _suffix = request.GET.get('suffix',"")
            _token,_key = action_daily.getQiniuToken(_session,_suffix)
            _dict = {
                'token': _token,
                'key': _key,
                "voice_url":QINIU_HOST + _key
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 用户上传语音
class AddVoice( ListView):
    def __init__(self):
        super(AddVoice,self).__init__()
    def get(self, request, *args, **kwargs):
            _session = request.GET.get('session',"")
            _voice_url = request.GET.get('voice_url',"")
            _voice_key = request.GET.get('voice_key',"")
            _theme_id = request.GET.get('theme_id',"")

            _dict = {
                'msg': action_daily.addVoice(_session,_voice_url,_voice_key,_theme_id)
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)

# 用户删除语音
class DeleteVoice( ListView):
    def __init__(self):
        super(DeleteVoice,self).__init__()
    def get(self, request, *args, **kwargs):
            _session = request.GET.get('session',"")
            _theme_id = request.GET.get('theme_id',"")

            _dict = {
                'msg': action_daily.deleteVoice(_session,_theme_id)
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)


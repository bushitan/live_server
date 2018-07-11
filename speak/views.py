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

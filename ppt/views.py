# -*- coding: utf-8 -*-

from django.views.generic import ListView
from lib.message import *
from action.online import *
action_online = ActionOnline()


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

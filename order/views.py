# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from lib.message import *
from action.member import *

# 登陆
class CheckMember( ListView):
    def __init__(self):
        self.action_member = ActionMember()
        super(CheckMember,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _session = request.GET.get('session',"")
            _dict = {
                "is_member":self.action_member.check_member(_session)
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


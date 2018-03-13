# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from order.query.cost import *
from order.query.discount import *
from order.query.query_order import *
from order.query.member import *

class ActionMember():
    def __init__(self):
        self.query_member = QueryMember()
    #获取当前激活的房间
    def check_member(self,session):
        return self.query_member.IsExists(user__session = session)

    def GetMessageList(self,room_id):
        return self.query_member.Filter(room_id = room_id)

    def CheckPusherUser(self,room_id,session):
        return self.query_member.IsExists(
            room_id = room_id,
            user__session = session,
        )

if __name__ == "__main__":
    a = ActionMember()
    import os,django
    django.setup()
    print a.check_member("9GEUS5/0FMeW2hnRpBOBzg==")
















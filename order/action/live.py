# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from room.query.message import *
from room.query.query_room import *
from room.query.pusher_user import *

class ActionLive():
    def __init__(self):
        self.query_room = QueryRoom()
        self.query_message = QueryMessage()
        self.query_pusher_user = QueryPusherUser()
    #获取当前激活的房间
    def GetCurrentRoom(self):
        return self.query_room.Get(is_show = YES)

    def GetMessageList(self,room_id):
        return self.query_message.Filter(room_id = room_id)

    def CheckPusherUser(self,room_id,session):
        return self.query_pusher_user.IsExists(
            room_id = room_id,
            user__session = session,
        )

if __name__ == "__main__":
    a = ActionLive()
    import os,django
    django.setup()
    # print a.GetTagList()
    room = a.GetCurrentRoom()
    print room
    print a.GetMessageList( room['room_id'])
    # print login.CheckSession('2w321321' , "12321321")
















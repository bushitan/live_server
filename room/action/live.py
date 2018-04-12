# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from django.db import transaction
from room.query.message import *
from room.query.query_room import *
from room.query.pusher_user import *
from room.query.classroom import *
from lite.query.file_library import *
from lite.query.user import *
from lite.query.app import *

class ActionLive():
    def __init__(self):
        self.query_room = QueryRoom()
        self.query_message = QueryMessage()
        self.query_pusher_user = QueryPusherUser()
        # self.query_classroom = QueryClassroom()
        # self.query_file_library = QueryFileLibrary()
        self.query_app = QueryApp()
        self.query_user = QueryUser()
    #获取当前APP的推流信息，IM房间
    def GetLiveUrlCurrentRoom(self,app_id):
        return self.query_app.Get(app_id = app_id)
    def GetCurrentRoom(self,app_id):
        return self.query_room.Filter(is_show = YES, app__app_id = app_id)[0]

    # 获取聊天室内的信息列表
    def GetMessageList(self,room_id):
        return self.query_message.Filter(room_id = room_id)
    # 获取聊天室内的信息列表

    #上传文件的形式
    # def AddMessageByFile(self,session,audio_url,**kwargs):
    #     with transaction.atomic():
    #         _user = self.query_user.Get(session= session)
    #         _file = self.query_file_library.Add(
    #             user_id = _user["user_id"],
    #             url = audio_url,
    #             style=FILE_AUDIO,
    #         )
    #         return self.query_message.Add(
    #             user_id = _user["user_id"],
    #             audio_id = _file["file_id"],
    #             **kwargs
    #         )

    #上传纯文字
    def AddMessage(self,session,**kwargs):
        _user = self.query_user.Get(session= session)
        self.query_message.Add(user_id = _user["user_id"],**kwargs)

    # 检测是否推流用户
    def CheckPusherUser(self,app_id,session):
        _user = self.query_user.Get(session= session)
        return True if _user["is_teacher"] == 1 else False

    # 获取聊天室内的信息列表
    def GetListRoomByApp(self,app_id):
        return self.query_room.Filter(app__app_id = app_id)



    #1V1房间，是否教师
    def CheckTeacher(self,session):
        return self.query_classroom.IsExists(teacher__session = session)


if __name__ == "__main__":
    import os,django
    django.setup()

    a = ActionLive()
    # print a.GetCurrentRoom("wx76cc2152eea29e91")
    print a.GetLiveUrlCurrentRoom("wx76cc2152eea29e91")
    # print a.GetListRoomByApp("wx76cc2152eea29e91")
    # print a.CheckPusherUser(u'wx76cc2152eea29e91' , u'9GEUS5/0FMeW2hnRpBOBzg==')
    # print a.GetTagList()
    # room = a.GetCurrentRoom()
    # print room
    # print a.GetMessageList( room['room_id'])
    # # print login.CheckSession('2w321321' , "12321321")
















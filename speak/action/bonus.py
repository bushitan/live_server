# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from django.db import transaction
from lite.query.user import *
from lite.query.file_library import *
from speak.query.speak_theme import *
from speak.query.speak_user import *
from lib.qi_niu import *
class ActionBonus():
    def __init__(self):
        self.query_theme = QuerySpeakTheme()
        self.query_speak_user = QuerySpeakUser()
        self.query_user = QueryUser()
        self.query_file = QueryFileLibrary()
        self.qiniu = QiNiu()

    #打卡获取积分
    def addCheck(self,session,theme_id):
        # TODO
        # 1 查用户
        # 2 增加积分
        return

    #分享获取积分
    def addShare(self,session,other_id):
        # 1 查session是否存在bonus表中，
        # 2 已存在，不得积分
        # 3 未存在，加积分
        return

    #兑换积分
    def exchangeGift(self,session,other_session,score,app_id):
        # 1 app_id 下是，other_session是否为教师
        # 2 session剩余积分 大于0 ，扣除成功
        # 3 积分小于0 扣除失败
        return


if __name__ == "__main__":

    import django
    django.setup()
    a = ActionBonus()
    # print a.GetTagList()
    # print a.addVoice('9GEUS5/0FMeW2hnRpBOBzg==','httpwoiqewo',1)
    # print a.getThemeList()
    # print login.CheckSession('2w321321' , "12321321")
















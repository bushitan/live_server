# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from lite.query.company import *
from lite.query.user import *
from lite.query.file_library import *
from lite.query.file_tag import *


class ActionMy():
    def __init__(self):
        self.query_company = QueryCompany()
        self.query_user = QueryUser()
        self.query_file = QueryFileLibrary()
        self.query_file_tag = QueryFileTag()
    def GetCompanyInfo(self):
        return self.query_company.Get()

    #微信用户注册
    def WXRegisterUserInfo(self,session,*args,**kwargs):
        obj = self.query_user.FilterQuery(session = session)
        return self.query_user.Update(obj,*args,**kwargs)[0]
    #用户报名
    def SetUserInfo(self,session,name,phone):
        obj = self.query_user.FilterQuery(session = session)
        self.query_user.Update(obj,user_name=name,phone=phone)
        return True
    def GetAppPPT(self,app_id):
        return self.query_file.Filter(app__app_id = app_id)
    def GetAppPPTTagList(self,app_id):
        return self.query_file_tag.Filter(app__app_id = app_id)

if __name__ == "__main__":
    import os,django
    django.setup()
    a = ActionMy()
    print a.GetAppPPT("9GEUS5/0FMeW2hnRpBOBzg==")
















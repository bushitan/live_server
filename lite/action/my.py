# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from lite.query.company import *
from lite.query.user import *
from lite.query.file_library import *


class ActionMy():
    def __init__(self):
        self.query_company = QueryCompany()
        self.query_user = QueryUser()
        self.query_file = QueryFileLibrary()
    def GetCompanyInfo(self):
        return self.query_company.Get()

    #微信用户注册
    def WXRegisterUserInfo(self,session,*args,**kwargs):
        obj = self.query_user.FilterQuery(session = session)
        return self.query_user.Update(obj,*args,**kwargs)[0]
    #用户报名
    def SetUserInfo(self,session,name,phone):
        obj = self.query_user.FilterQuery(session = session)
        self.query_user.Update(obj,name=name,phone=phone)
        return True
    def GetUserPPT(self,session):
        return self.query_file.Filter(user__session = session)
if __name__ == "__main__":
    import os,django
    django.setup()
    a = ActionMy()
    print a.GetUserPPT("9GEUS5/0FMeW2hnRpBOBzg==")
















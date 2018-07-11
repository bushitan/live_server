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
class ActionDaily():
    def __init__(self):
        self.query_theme = QuerySpeakTheme()
        self.query_speak_user = QuerySpeakUser()
        self.query_user = QueryUser()
        self.query_file = QueryFileLibrary()
        self.qiniu = QiNiu()

    #获取主题列表
    def getThemeList(self):
        _query = self.query_theme.FilterQuery()
        _list = []
        for theme in _query:
            _node = self.getTheme(theme.id)
            _list.append( _node )
        return _list

    #获取主题
    def getTheme(self,theme_id):
        _theme = self.query_theme.Get(id = theme_id)
        _student_list = self.query_speak_user.Filter(theme_id = _theme['id'])
        _visitor_list = self.query_speak_user.Filter(theme_id = _theme['id'])
        return {
            "theme":_theme,
            "student_list":_student_list,
            "visitor_list":_visitor_list,
        }

    # 上传录音
    def addVoice(self,session,voice_url,theme_id):
        with transaction.atomic():
            user = self.query_user.GetQuery(session=session)
            _voice = self.query_file.Add(
                url = voice_url,
                style = FILE_AUDIO,
            )
            self.query_speak_user.Add(
                user = user,
                voice_id = _voice['file_id'],
                theme_id = theme_id,
            )
        return True

    def getQiniuToken(self,session,suffix):
        _user = self.query_user.Get(session = session)
        _user_id = _user["user_id"]
        _file_name = "speak_" + str(_user_id) + "_" + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "." + suffix
        _token,_key = self.qiniu.getTokenNoPolicy(_file_name)
        return _token,_key


if __name__ == "__main__":

    import django
    django.setup()
    a = ActionDaily()
    # print a.GetTagList()
    # print a.addVoice('9GEUS5/0FMeW2hnRpBOBzg==','httpwoiqewo',1)
    print a.getThemeList()
    # print login.CheckSession('2w321321' , "12321321")
















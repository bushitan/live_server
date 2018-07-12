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
    def addVoice(self,session,voice_url,voice_key,theme_id):
        with transaction.atomic():
            user = self.query_user.GetQuery(session=session)
            _voice = self.query_file.Add(
                url = voice_url,
                style = FILE_AUDIO,
                name = voice_key,
            )
            self.query_speak_user.Add(
                user = user,
                voice_id = _voice['file_id'],
                theme_id = theme_id,
            )
        return True
    # 删除录音
    def deleteVoice(self,session,theme_id):
        with transaction.atomic():
            user = self.query_user.GetQuery(session=session)
            _query = self.query_speak_user.FilterQuery(user = user,theme_id=theme_id)
            for s in _query:
                _voice_file = self.query_file.GetQuery(id=s.voice_id)
                self.qiniu.delete(_voice_file.name)  #根据key删除七牛的音频文件
                self.query_file.Delete(_voice_file ) #删除音频文件
            self.query_speak_user.Delete(_query) #删除房间的上传记录
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
















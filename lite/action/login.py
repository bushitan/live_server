# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from lite.query.user import *

app_id = APP_ID
app_secret = APP_SECRET

class ActionLogin():
    q_user = None
    def __init__(self):
        self.q_user = QueryUser()

    def _GetOpenID(self,js_code):
        _js_code = js_code
        _wx_url = "https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code "  %(app_id,app_secret,_js_code )
        req = urllib2.Request(_wx_url)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req)
        _json =  json.loads(response.read())
        return  _json

    def CheckSession(self,str_js_code,str_session):
        if self.q_user.IsExists(session = str_session) is True:  #session存在，返回用户
            _d_user = self.q_user.Get(session = str_session)
        else:#session不存在，获取open_id判断
            # _json = WxHttp(_js_code)
            _json = self._GetOpenID(str_js_code)
            _open_id = _json["openid"]
            if self.q_user.IsExists( wx_open_id = _open_id ) is True: #open_id 存在，
                _d_user = self.q_user.Get( wx_open_id = _open_id)
            else: #open_id 不存在，增加用户
                _d_user = self.q_user.Add(
                    wx_open_id = _json["openid"],
                    session =  _json["session_key"],
                )
        return _d_user


if __name__ == "__main__":
    login = ActionLogin()
    print login.CheckSession('2w321321' , "12321321")
















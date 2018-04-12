#coding:utf-8

from django.views.generic import ListView
from lib.message import *
from action.login import *
from action.my import *

# 登陆
class Login( ListView):
    def __init__(self):
        self.action_login = ActionLogin()
        super(Login,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            # print 11111
            _s_js_code = request.GET.get('js_code',"")
            _s_session = request.GET.get('session',"")
            _app_id = request.GET.get('app_id',"")
            # print _app_id
            _dict = {
                'dict_user':self.action_login.CheckSession(_s_js_code,_s_session,_app_id)
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

class WXRegister( ListView):
    def __init__(self):
        self.action_my = ActionMy()
        super(WXRegister,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _s_session = request.GET.get('session',"")
            _user_dict = self.action_my.WXRegisterUserInfo(
                _s_session ,
                nick_name = request.GET.get('nickName',""),
                avatar_url = request.GET.get('avatarUrl',""),
                gender = request.GET.get('gender',""),
                province = request.GET.get('province',""),
                city = request.GET.get('city',""),
                country = request.GET.get('country',""),
            )
            _dict = {
                'user_dict':_user_dict
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 登陆
class CompanyGetInfo( ListView):
    def __init__(self):
        self.action_my = ActionMy()
        super(CompanyGetInfo,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _dict = {
                'company_dict':self.action_my.GetCompanyInfo()
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


# 登陆
class UserSetInfo( ListView):
    def __init__(self):
        self.action_my = ActionMy()
        super(UserSetInfo,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _s_session = request.GET.get('session',"")
            _name = request.GET.get('name',"")
            _phone = request.GET.get('phone',"")
            _dict = {
                'msg':self.action_my.SetUserInfo(_s_session ,_name ,_phone)
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 登陆
class UserGetPPT( ListView):
    def __init__(self):
        self.action_my = ActionMy()
        super(UserGetPPT,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _app_id = request.GET.get('app_id',"")
            _dict = {
                'ppt_list':self.action_my.GetAppPPT(_app_id ),
                'ppt_tag_list':self.action_my.GetAppPPTTagList(_app_id ),
            }
            # print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )





















class Index( ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        return super(Index, self).get_context_data(**kwargs)

    def get_queryset(self):
        pass

    # def get(self, request, *args, **kwargs):
    #     try:
    #         print 11111
    #         _s_js_code = request.GET.get('js_code',"")
    #         _s_session = request.GET.get('session',"")
    #         _login = ActionLogin()
    #         _login.CheckSession(_s_js_code,_s_session)
    #         _dict = {
    #             'MSG':u'登录初始化成狗',
    #         }
    #         print _dict
    #         return MESSAGE_RESPONSE_SUCCESS(_dict)
    #     except Exception as e :
    #         a = Exception
    #         print Exception
    #         print e
    #         return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

    def post(self, request, *args, **kwargs):
        try:
            _str_hash = request.POST['hash']
            _dict = {
                'MSG':u'登录初始化成狗',
            }
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception,e :
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
#coding:utf-8

from django.views.generic import ListView
from lib.message import *
from action.login import *
from action.company import *

# 登陆
class Login( ListView):
    def __init__(self):
        self.action_login = ActionLogin()
        super(Login,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            print 11111
            _s_js_code = request.GET.get('js_code',"")
            _s_session = request.GET.get('session',"")
            _dict = {
                'dict_user':self.action_login.CheckSession(_s_js_code,_s_session)
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )


# 登陆
class CompanyGetInfo( ListView):
    def __init__(self):
        self.action_company = ActionCompany()
        super(CompanyGetInfo,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _dict = {
                'dict_company':self.action_company.GetCompanyInfo()
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
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
# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^get/theme_list/$', GetThemeList.as_view()),
    url(r'^get/theme/$', GetTheme.as_view()),
    # url(r'^register/$', WXRegister.as_view()),
    # url(r'^company/get/info/$', CompanyGetInfo.as_view()),
    # url(r'^user/set/info/$', UserSetInfo.as_view()),
    # url(r'^user/get/ppt/$', UserGetPPT.as_view()),


    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]
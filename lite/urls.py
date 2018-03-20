# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    # url(r'^index/$', Index.as_view()),
    url(r'^login/$', Login.as_view()),
    url(r'^register/$', WXRegister.as_view()),
    url(r'^company/get/info/$', CompanyGetInfo.as_view()),
    url(r'^user/set/info/$', UserSetInfo.as_view()),
    url(r'^user/get/ppt/$', UserGetPPT.as_view()),


    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]
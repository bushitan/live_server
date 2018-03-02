# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^tag/get_list/$', TagGetList.as_view()),
    url(r'^news/get_list/$', NewsGetListByTagID.as_view()),
    url(r'^article/get/$', ArticleGetDictByID.as_view()),


    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]
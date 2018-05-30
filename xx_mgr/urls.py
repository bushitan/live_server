# -*- coding: utf-8 -*-


from django.conf.urls import url
from views import *



urlpatterns = [

    url(r'^ym/index/$', YMIndexView.as_view()),
    url(r'^ym/country/(?P<nav_index>\w+)/(?P<pid>\w+)/$', YMCountryView.as_view()),
    url(r'^ym/cover/(?P<nav_index>\w+)/(?P<tag_id>\w+)/$', YMCoverView.as_view()),
    url(r'^ym/article/(?P<nav_index>\w+)/(?P<article_id>\w+)/$', YMArticleView.as_view()),
    url(r'^about_me/(?P<nav_index>\w+)/$', AboutMeView.as_view()),


    url(r'^lx/index/$', LXIndexView.as_view()),
    url(r'^lx/country/(?P<nav_index>\w+)/(?P<pid>\w+)/$', LXCountryView.as_view()),

    url(r'^lx/study/(?P<nav_index>\w+)/$', LXStudyView.as_view()),
    url(r'^lx/success/(?P<nav_index>\w+)/$', LXSuccessView.as_view()),

    # url(r'^tag/delete/$', TagAdd.as_view()),
    # url(r'^tag/get_list/$', TagAdd.as_view()),
    # url(r'^tag/update/$', TagAdd.as_view()),
]
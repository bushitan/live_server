# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from lib.message import *
from action.news import *

# 登陆
class TagGetList( ListView):
    def __init__(self):
        self.action_news = ActionNews()
        super(TagGetList,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _dict = {
                'list_tag':self.action_news.GetTagList()
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )

# 登陆
class NewsGetListByTagID( ListView):
    def __init__(self):
        self.action_news = ActionNews()
        super(NewsGetListByTagID,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _tag_id = request.GET.get('tag_id',"")
            _dict = {
                'list_cover':self.action_news.GetCoverListByTagID( _tag_id )
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )
# 登陆
class ArticleGetDictByID( ListView):
    def __init__(self):
        self.action_news = ActionNews()
        super(ArticleGetDictByID,self).__init__()
    def get(self, request, *args, **kwargs):
        try:
            _article_id = request.GET.get('article_id',"")
            _dict = {
                'dict_article':self.action_news.GetArticleContentByID( _article_id )
            }
            print _dict
            return MESSAGE_RESPONSE_SUCCESS(_dict)
        except Exception as e :
            a = Exception
            print Exception
            print e
            return MESSAGE_RESPONSE_NET_ERROR( self.__class__.__name__ ,e )







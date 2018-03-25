# -*- coding: utf-8 -*-
from lib.util import *
import json
import urllib2
from cover.query.tag import *
from cover.query.articel import *
from cover.query.news import *

class ActionNews():
    def __init__(self):
        self.query_news = QueryNews()
        self.query_article = QueryArticle()
        self.query_tag = QueryTag()

    def GetTagList(self,app_id):
        print self.query_tag.Filter(is_show = YES,app__app_id = app_id)
        return self.query_tag.Filter(is_show = YES,app__app_id = app_id)
    def GetCoverListByTagID(self,tag_id):
        # a = self.query_tag.FilterQuery(id=1)
        return self.query_news.Filter(tag = tag_id)
        # return   self.query_news.Get(name = 'zhuanlan')
        # return   self.query_news.Get(tag_id = '1')
    def GetArticleContentByID(self,article_id):
        return self.query_article.Get(id = article_id)

if __name__ == "__main__":
    a = ActionNews()
    # print a.GetTagList()
    print a.GetArticleContentByID(1)
    # print login.CheckSession('2w321321' , "12321321")
















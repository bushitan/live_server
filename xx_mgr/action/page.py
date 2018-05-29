# -*- coding: utf-8 -*-

from xx_mgr.query.tag import *
from xx_mgr.query.article import *

PID_YM_INDEX = 11
class ActionPage():
	def __init__(self):
		self.query_tag = QueryTag()
		self.query_article = QueryArticle()


	def GetYMNav(self):
		return  self.query_tag.FilterQuery(web_site = 1,father = None)

	def GetYMIndex(self):
		one_tag_list = self.query_tag.FilterQuery(father__pid = PID_YM_INDEX,pid = 1)
		one_article_list = []
		for t in one_tag_list:
			if  self.query_article.IsExists(tag = t) is True:
				one_article_list.append( self.query_article.GetQuery(tag = t) )
			else:
				one_article_list.append({})



		two_tag = self.query_tag.GetQuery(father__pid = PID_YM_INDEX,pid = 2)
		two_article_list = self.query_article.FilterQuery(tag = two_tag)[0:8]


		three_tag = self.query_tag.GetQuery(father__pid = PID_YM_INDEX,pid = 3)
		three_article_list = self.query_article.FilterQuery(tag = three_tag)[0:9]


		four_tag = self.query_tag.GetQuery(father__pid = PID_YM_INDEX,pid = 4)
		four_article_list = self.query_article.FilterQuery(tag = four_tag)[0:8]


		return one_tag_list,one_article_list,\
			   two_tag,two_article_list ,\
				three_tag, three_article_list ,\
			   four_tag,four_article_list

if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionPage()
	# print a.GetYMIndex()
	print a.GetYMNav()
	# a.pvpRoomDict
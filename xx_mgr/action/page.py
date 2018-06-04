# -*- coding: utf-8 -*-

from xx_mgr.query.tag import *
from xx_mgr.query.article import *

PID_YM_INDEX = 11
PID_YM_AMERICAN = 12


class ActionPage():
	def __init__(self):
		self.query_tag = QueryTag()
		self.query_article = QueryArticle()


	def GetNav(self,web_site):
		return  self.query_tag.FilterQuery(web_site = web_site,father = None)

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


	# 国家子类
	def GetYMCountryAd(self):
		return self.getOnly(PID_YM_AMERICAN,1)
	def GetYMCountryInfo(self):
		return self.queryOnly(PID_YM_AMERICAN,3,8)
	def GetYMCountryDetail(self):
		return self.queryMore(PID_YM_AMERICAN,4)

# 	#留学首页
# 	def GetLXIndex1(self):
# PID_LX_INDEX


	def getOnly(self,father_pid,pid):
		if  self.query_tag.IsExists(father__pid = father_pid,pid = pid) is False:
			return {},{}
		print father_pid,pid
		_tag = self.query_tag.GetQuery(father__pid = father_pid,pid = pid)
		print _tag
		_article = {}
		if  self.query_article.IsExists(tag = _tag):
			_article = self.query_article.FilterQuery(tag = _tag)[0]
		return _tag,_article

	def queryOnly(self,father_pid,pid,range):
		_tag = self.query_tag.GetQuery(father__pid = father_pid,pid = pid)
		_article_list = self.query_article.FilterQuery(tag = _tag)[0:range]
		return _tag,_article_list
	def queryMore(self,father_pid,pid):
		one_tag_list = self.query_tag.FilterQuery(father__pid = father_pid,pid = pid)
		one_article_list = []
		for tag in one_tag_list:
			if  self.query_article.IsExists(tag = tag) is True:
				one_article_list.append( self.query_article.FilterQuery(tag = tag)[0] )
			else:
				one_article_list.append({})
		return one_tag_list,one_article_list


	def GetArticleListByTagID(self,tag_id):
		_tag = self.query_tag.GetQuery(id = tag_id)
		_article_list = self.query_article.FilterQuery(tag = tag_id)
		return _tag,_article_list
	def GetArticleByID(self,article_id):
		if self.query_article.IsExists() is True:
			return self.query_article.GetQuery(id = article_id)
		else:
			return False



	#################小程序API#################
	def GetFatherTag(self,website):
		return self.query_tag.Filter(father = None,web_site = website)
	def GetSonTagByFather(self,father_id):
		return self.query_tag.Filter(father = father_id)

	def GetCoverByTag(self,tag_id):
		# _son_query = self.query_tag.FilterQuery(father = father_id)
		# _son_list = []
		_tag = self.query_tag.Get(id = tag_id)
		_article_list =  self.query_article.Filter(tag_id = tag_id)[0:4]
		_dict = {
			"tag":_tag,
			"article_list":_article_list,
		}
		return _dict
	def GetArticleMatrixByFather(self,father_id):
		_son_query = self.query_tag.FilterQuery(father = father_id)
		_page_list = []
		for son in _son_query:
			_cover = self.GetCoverByTag(son.id)
			_page_list.append(_cover)
		return _page_list
	def GetArticle(self,article_id):
		if self.query_article.IsExists() is True:
			return self.query_article.Get(id = article_id)
		else:
			return False
		# for son in _son_query:
			# _son_list.append(_article_list)




if __name__ == "__main__":
	import os,django
	django.setup()
	a = ActionPage()
	# print a.GetYMIndex()
	# print a.getOnly(12,1)
	# a.pvpRoomDict
	# print a.GetSonTagByFather(81)
	print a.GetCoverByTag(81)
# -*- coding: utf-8 -*-
from lib.query_base import *
from xx_mgr.models import *
class QueryArticle(QueryBase):
	def __init__(self):
		super(QueryArticle,self).__init__(MGRArticle)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"article_id":obj.id,
			"tag_id":obj.tag_id,
			"cover_url" : obj.cover.url if obj.cover is not None else "",
			"title":obj.title,
			"subtitle":obj.subtitle,
			"content":obj.content,
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
			# "web_site":obj.web_site,
			# "father_id":obj.father_id,
			# "pid":obj.pid,
		}
	#
	# def _PackCover(self,obj):
	# 	return {
	# 		"title",obj.title,
	# 		"subtitle",obj.subtitle,
	# 	}
	# def Cover(self,*args,**kwargs):
	# 	obj= self.model.objects.filter(*args,**kwargs)
	# 	print obj
	# 	return self._PackList( self._PackCover,obj)


if __name__ == "__main__":
	import os,django
	django.setup()
	q = QueryArticle()
	print q.Filter(	)
	# print q.Cover()
	# print query_user.GetDict(session = "12321321")
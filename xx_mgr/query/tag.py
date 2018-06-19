# -*- coding: utf-8 -*-
from lib.query_base import *
from xx_mgr.models import *
class QueryTag(QueryBase):
	def __init__(self):
		super(QueryTag,self).__init__(MGRTag)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"id":obj.id,
			"name":obj.name,
			"name_mobile":obj.name_mobile,
			"web_site":obj.web_site,
			"father_id":obj.father_id,
			"pid":obj.pid,
			# "create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
	# def Cover(self):

if __name__ == "__main__":
	import os,django
	django.setup()
	q = QueryTag()
	print q.Filter(	pid=11)
	# print query_user.GetDict(session = "12321321")
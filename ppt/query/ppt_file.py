# -*- coding: utf-8 -*-
from lib.query_base import *
from ppt.models import *
class QueryPPTFile(QueryBase):
	def __init__(self):
		super(QueryPPTFile,self).__init__(PPTFile)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"file_url":obj.url,



			# "create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryPPTFile()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")
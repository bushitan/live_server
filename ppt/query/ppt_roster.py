# -*- coding: utf-8 -*-
from lib.query_base import *
from ppt.models import *
class QueryPPTRoster(QueryBase):
	def __init__(self):
		super(QueryPPTRoster,self).__init__(PPTRoster)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"name":obj.name,
			"phone":obj.phone,
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryPPTRoster()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")
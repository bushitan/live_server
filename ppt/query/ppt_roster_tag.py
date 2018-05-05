# -*- coding: utf-8 -*-
from lib.query_base import *
from ppt.models import *
class QueryPPTRosterTag(QueryBase):
	def __init__(self):
		super(QueryPPTRosterTag,self).__init__(PPTRosterTag)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"name":obj.name,
			"roster_tag_id":obj.id,
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryPPTRosterTag()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")
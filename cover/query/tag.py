# -*- coding: utf-8 -*-
from lib.query_base import *
from cover.models import *
class QueryTag(QueryBase):
	def __init__(self):
		super(QueryTag,self).__init__(Tag)


	#获取文章详细内容
	def _PackDict(self,obj):
		return {
			"tag_id":obj.id,
			"name":obj.name,
		}

if __name__ == "__main__":
	q = QueryTag()
	print q.Filter(
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")
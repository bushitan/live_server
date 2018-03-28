# -*- coding: utf-8 -*-
from lib.query_base import *
from pvp.models import *
class QueryStageTag(QueryBase):
	def __init__(self):
		super(QueryStageTag,self).__init__(StageTag)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"stage_tag_id":obj.id,
			"description":obj.description,


			# "create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryStageTag()
	print q.FilterQuery()
	# print query_user.GetDict(session = "12321321")
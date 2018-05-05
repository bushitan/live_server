# -*- coding: utf-8 -*-
from lib.query_base import *
from ppt.models import *
class QueryPPTTeam(QueryBase):
	def __init__(self):
		super(QueryPPTTeam,self).__init__(PPTTeam)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"team_id":obj.id,
			"team_name":obj.name,
			"create_user_id":obj.create_user_id,
			# "create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryPPTTeam()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")
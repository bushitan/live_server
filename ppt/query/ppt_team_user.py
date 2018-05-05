# -*- coding: utf-8 -*-
from lib.query_base import *
from ppt.models import *
class QueryPPTTeamUser(QueryBase):
	def __init__(self):
		super(QueryPPTTeamUser,self).__init__(PPTTeamUser)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"team_id":obj.team_id,
			"member_user_id":obj.member_user_id,
			# "create_time":obj.create_time.strftime("%Y-%m-%d"),
		}
if __name__ == "__main__":
	# import os,django
	# django.setup()
	q = QueryPPTTeamUser()
	print q.Filter(	)
	# print query_user.GetDict(session = "12321321")
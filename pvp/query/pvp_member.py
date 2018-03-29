# -*- coding: utf-8 -*-
from lib.query_base import *
from pvp.models import *
class QueryPVPMember(QueryBase):
	def __init__(self):
		super(QueryPVPMember,self).__init__(PVPMember)

	#用于封面展示的数据
	def _PackDict(self,obj):
		return {
			"pvp_member_id":obj.id,
			"user_id":obj.user_id,

		}
if __name__ == "__main__":
	import os,django
	django.setup()
	q = QueryPVPMember()
	print q.IsExists(user__session = "ylbBSYYcHPocFzdW+HNEYg==")
	# print query_user.GetDict(session = "12321321")
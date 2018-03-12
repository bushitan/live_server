# -*- coding: utf-8 -*-
from lib.query_base import *
from order.models import *
class QueryMember(QueryBase):
	def __init__(self):
		super(QueryMember,self).__init__(Member)


	#获取文章详细内容
	def _PackDict(self,obj):
		return {
			"user_id":obj.user_id,
			"cost_id":obj.cost_id,
			"is_alive":obj.is_alive,
			"start_time": obj.create_time.strftime("%Y-%m-%d"),
			"end_time": obj.create_time.strftime("%Y-%m-%d"),
			"create_time": obj.create_time.strftime("%Y-%m-%d"),
		}

if __name__ == "__main__":
	q = QueryMember()
	print q.Filter()
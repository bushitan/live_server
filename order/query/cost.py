# -*- coding: utf-8 -*-
from lib.query_base import *
from order.models import *
class QueryCost(QueryBase):
	def __init__(self):
		super(QueryCost,self).__init__(Cost)


	#获取文章详细内容
	def _PackDict(self,obj):
		return {
			"name":obj.name,
			"name_admin":obj.name_admin,
			"description":obj.description,
			"unit_price": obj.unit_price,
			"duration": obj.duration,
		}

if __name__ == "__main__":
	q = QueryCost()
	print q.Filter()
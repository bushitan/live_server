# -*- coding: utf-8 -*-
from lib.query_base import *
from order.models import *
class QueryDiscount(QueryBase):
	def __init__(self):
		super(QueryDiscount,self).__init__(Discount)


	#获取文章详细内容
	def _PackDict(self,obj):
		print 21
		return {
			"user_id":obj.user_id,
			"discount_id":obj.id,
			"discount_name":obj.template.name if obj.template is not None else "",
			"discount_price":obj.template.price if obj.template is not None else "",
			"discount_limit_price":obj.template.limit_price,
			"start_time":obj.start_time.strftime("%Y-%m-%d"),
			"end_time":obj.end_time.strftime("%Y-%m-%d"),
			"create_time":obj.create_time.strftime("%Y-%m-%d"),
		}

if __name__ == "__main__":
	q = QueryDiscount()
	print q.Filter()
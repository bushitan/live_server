# -*- coding: utf-8 -*-
from lib.query_base import *
from order.models import *
class QueryOrder(QueryBase):
	def __init__(self):
		super(QueryOrder,self).__init__(Order)


	#获取文章详细内容
	def _PackDict(self,obj):
		return {
			"order_id":obj.id,
			"member_id":obj.member_id,
			"discount_id":obj.discount_id,
			"is_alive":obj.is_alive,
			"is_pay":obj.is_pay,
			"wx_out_trade_no":obj.wx_out_trade_no,
			"origin_price":obj.origin_price,
			"pay_price":obj.pay_price,
			"remark":obj.remark,
			"create_time": obj.create_time.strftime("%Y-%m-%d"),
		}

if __name__ == "__main__":
	q = QueryOrder()
	print q.Filter()
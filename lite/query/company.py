# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
class QueryCompany(QueryBase):
	def __init__(self):
		super(QueryCompany,self).__init__(Company)

	def _PackDict(self,query_get):
		_dict = {
			'name':query_get.name,
			'phone':query_get.phone,
			'introduction':query_get.introduction,
			'address':query_get.address,
			'latitude':query_get.latitude,
			'longitude':query_get.longitude,
		}
		return _dict

if __name__ == "__main__":
	q = QueryCompany()
	print q.Filter(
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")
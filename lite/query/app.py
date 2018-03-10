# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
class QueryLite(QueryBase):
	def __init__(self):
		super(QueryLite,self).__init__(App)

	def _PackDict(self,query_get):
		_dict = {
			'app_id':query_get.app_id,
			'longitude':query_get.longitude,
			'latitude':query_get.latitude,
			'taste_qr':query_get.taste_qr,
		}
		return _dict

if __name__ == "__main__":
	q = QueryLite()
	print q.Filter(
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")
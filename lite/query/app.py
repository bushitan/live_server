# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
class QueryApp(QueryBase):
	def __init__(self):
		super(QueryApp,self).__init__(App)

	def _PackDict(self,query_get):
		_dict = {
			'id':query_get.id,
			'app_id':query_get.app_id,
			'app_secret':query_get.secret_key,
			'app_name':query_get.name,
			# 'longitude':query_get.longitude,
			# 'latitude':query_get.latitude,
			# 'taste_qr':query_get.taste_qr,
		}
		return _dict

if __name__ == "__main__":
	q = QueryApp()
	print q.Filter(
		# session = "12321321"
	)
	# print query_user.GetDict(session = "12321321")
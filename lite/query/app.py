# -*- coding: utf-8 -*-
from lib.query_base import *
from lite.models import *
class QueryApp(QueryBase):
	def __init__(self):
		super(QueryApp,self).__init__(App)

	def _PackDict(self,obj):
		_dict = {
			'id':obj.id,
			'app_id':obj.app_id,
			'app_secret':obj.secret_key,
			'app_name':obj.name,
			"im_num":obj.im_num,
			"pusher_url":obj.pusher,
			"player_url":obj.player,
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